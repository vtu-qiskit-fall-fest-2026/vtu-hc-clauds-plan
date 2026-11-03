"""Utility to extract fine‑grained phishing character evidence from a URL.

The function examines the raw URL string and the lexical feature vector
and returns a list of human‑readable strings describing suspicious
characters (numeric substitutions, homographs, punycode, unusual ports,
etc.).

This module is deliberately lightweight – it does **not** perform any
network I/O, keeping the API side‑effect free.
"""

import re
from urllib.parse import urlparse

def extract_character_evidence(url: str, features: dict) -> list:
    """Return a list of strings describing suspicious characters in ``url``.

    Parameters
    ----------
    url: str
        The *sanitized* URL that has already passed ``validate_and_sanitize_url``.
    features: dict
        Dictionary of lexical feature values produced by ``extract_features``.

    The function looks for:
    * Numeric substitutions (e.g. ``0`` for ``o``).
    * Leet‑style replacements (1→l/i, 3→e, 5→s, etc.).
    * Homoglyph / punycode indicators.
    * Unusual ports.
    * Repeated or missing characters (simple heuristic).
    """
    evidence = []
    # Normalise to lowercase for pattern checks
    lower = url.lower()

    # 1. Numeric substitutions (common leet patterns)
    leet_map = {
        '0': 'o',
        '1': 'l/i',
        '3': 'e',
        '5': 's',
        '7': 't',
    }
    for digit, repl in leet_map.items():
        if digit in lower:
            evidence.append(f"Numeric substitution: '{digit}' used in place of '{repl}'")

    # 2. Homoglyph / punycode
    if features.get('has_punycode'):
        evidence.append('Punycode (xn--) or non‑ASCII characters detected – possible IDN homograph')

    # 3. Unusual port (if port is present and not standard)
    parsed = urlparse(url)
    if parsed.port and parsed.port not in (80, 443, 8080, 8443):
        evidence.append(f"Non‑standard port: {parsed.port}")

    # 4. Repeated characters (e.g., "aaaa" in domain)
    domain = (parsed.hostname or '')
    repeats = re.findall(r'(.)\1{2,}', domain)
    if repeats:
        evidence.append(f"Repeated character(s) in domain: {', '.join(set(repeats))}")

    # 5. Missing expected characters – heuristic: high digit ratio plus low alpha ratio
    if features.get('digit_ratio_url', 0) > 0.2 and len(re.sub(r'[0-9]', '', lower)) < len(lower) * 0.5:
        evidence.append('High numeric density relative to alphabetic characters')

    return evidence
