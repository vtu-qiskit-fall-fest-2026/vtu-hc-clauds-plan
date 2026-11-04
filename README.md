<div align="center">

# Q-Sentinel

**VTU-QFF-HC-0191**  |  Tier: **Online**

</div>

---

<div align="center">

| | |
| :--- | :--- |
| **Team** | Q-Sentinel |
| **Team ID** | VTU-QFF-HC-0030 |
| **Tier** | Online |
| **Live Interactive Web Platform** | [🌐 **https://qsentinental.vercel.app/**](https://qsentinental.vercel.app/) |
| **Repository** | [vtu-hc-clauds-plan](https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-clauds-plan) |
| **Organisation** | [vtu-qiskit-fall-fest-2026](https://github.com/vtu-qiskit-fall-fest-2026) |
| **Event** | VTU-QFF Hackathon — VTU-Qiskit Fall Fest 2026 |

</div>

---

## 📌 Table of Contents

- [Team Members](#-team-members-github-ids)
- [Problem Statement](#-problem-statement)
- [Proposed Solution](#-proposed-solution)
- [Real-World Impact & Security Utility](#-real-world-impact--security-utility)
- [Approach & Architecture](#-approach--architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Benchmark Results & Performance Findings](#-benchmark-results--performance-findings)
- [Threat Intelligence Integration](#-threat-intelligence-integration)
- [How to Run](#-how-to-run)
- [Demo Video & Working Prototype](#-demo-video--working-prototype)
- [How to Push Code](#-how-to-push-code)
- [Submission Checklist](#-submission-checklist)
- [Resources](#-resources)
- [License & Attribution](#-license--attribution)

---

## 👥 Team Members (GitHub IDs)

| # | Name | GitHub Username | Role |
| :-- | :--- | :--- | :--- |
| 1 | Narasimha Kulkarni | [@narasimhakulkarni393-dotcom](https://github.com/narasimhakulkarni393-dotcom) | Team Lead |
| 2 | Kartik Dhamanekar | [@kartikdhamanekar123-wq](https://github.com/kartikdhamanekar123-wq) | Devloper |

---

## ❓ Problem Statement

<!--
State the problem you are solving. Be specific: what is broken or missing,
who experiences it, and why does it matter. Link to the official problem
statement from the brief if one applies.
-->

*Problem:* Phishing links are becoming harder to identify, and many people unknowingly click on them and risk their personal information. Our project, Q-Sentinel, aims to identify such links using machine learning and explore whether combining it with quantum computing can improve detection.

*Why it matters:* We built Q-Sentinel, a system that aims to identify suspicious links and help users stay safe from phishing attacks. It uses machine learning to analyze URLs, and we are exploring how quantum computing can be combined with it to improve detection.

*Track / Category:* Online / Offline(both)· Track 1 / Track 2 · <Quantum + AI ML>

---

## 💡 Proposed Solution

<!--
Describe your solution. Keep it concrete: the core idea, the user flow, and
the quantum/ML technique you are applying.
-->

*Solution:* We built Q-Sentinel, a phishing URL detection prototype that uses machine learning to analyze URL features and identify potentially suspicious links. We are also exploring a hybrid quantum-classical approach to assess how quantum methods may enhance detection performance.

*Key idea:* Hybrid quantum-classical phishing detection using URL feature extraction, classical machine learning, and a Qiskit-based quantum kernel model for performance comparison.

*Why this works:* Q-Sentinel addresses phishing by analyzing URL features with machine learning to identify potentially malicious links before users trust them. By comparing a classical model with a hybrid quantum-classical approach, we aim to evaluate whether quantum techniques can improve detection while measuring accuracy and false positives.

---


## 🧩 Approach & Architecture

```
Hybrid Quantum-Classical Threat Intelligence Pipeline:

URL Input (Single Web Input, Batch CSV, or REST API)
    ↓
URL Parsing & Invariant Normalization
    (Scheme & Apex Domain Alignment, IDN/Punycode, Port/Path Extraction)
    ↓
25 Invariant Lexical & Structural Features
(Shannon Entropy, Digit Ratios, Subdomain Hierarchy, Brand Spoofing, TLD Risk)
    ↓
    ├─→ Classical Engine: XGBoost GBDT, GPU-trained (Calibrated Threshold τ = 0.43)
    │     (75.86% Phishing Recall / 76.23% Precision on Domain-Disjoint Unseen Hosts)
    │
    ├─→ Quantum Engine: Variational Quantum Classifier (VQC)
    │     (Hilbert Space Feature Mapping via Ry/Rz Angles + Entangling CNOT Layers)
    │
    └─→ Threat Intel Path: OTX & IOC Telemetry Cache
    ↓
Ensemble Decision Engine
    ├─ Classical Calibrated Risk Probability
    ├─ Quantum Hilbert State Verification
    └─ Known Campaign IOC Signatures
    ↓
Output: Risk Level (🟢 LOW / 🟡 MEDIUM / 🔴 CRITICAL) + Explainable ML Evidence
```

1. **URL Ingestion & Normalization**: Accepts URL strings from web input, REST API, or batch CSV. Normalizes schemes and apex hostnames to eliminate `www.` biases.
2. **Feature Extraction**: Extracts 25 lexical, structural, and information-theoretic indicators (Shannon entropy, brand spoofing in subdomains, suspicious TLDs, IP literals).
3. **Classical ML Engine**: XGBoost Gradient Boosted Decision Trees trained on an NVIDIA GPU (CUDA), with a validation-calibrated decision threshold to balance phishing recall against false positives.
4. **Quantum VQC Engine**: Parameterized 4-qubit quantum circuit simulator utilizing Pauli rotation encodings ($R_y(\theta), R_z(\theta)$) and parameter-shift gradients.
5. **Threat Intelligence Integration**: AlienVault OTX / PhishTank campaign indicators for real-world threat correlation.
6. **Interactive Dashboard**: Modern dark-mode SOC dashboard on Vercel + local Streamlit application with interactive Quantum Lab.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.11 / 3.12 / 3.14+ |
| **Quantum Simulation** | NumPy Statevector Engine & Aer-compatible Parameter-Shift Circuits |
| **Classical ML** | XGBoost (CUDA GPU training), LightGBM, scikit-learn, joblib |
| **Data & Feature Engineering** | pandas, numpy, scipy |
| **Web Frontend** | Tailwind CSS, Chart.js, Streamlit |
| **Serverless API** | Vercel Edge Serverless Functions (Python 3.12 runtime) |
| **Threat Intel** | AlienVault OTX & Known Phishing IOC Feeds |
| **Testing** | pytest (87 unit & integration tests) |
| **Deployment** | Vercel (Production) + GitHub CI |

---

## 📁 Project Structure

```
vtu-hc-clauds-plan/
├── README.md                  # Hackathon documentation
├── requirements.txt           # Lean serverless production dependencies (Vercel)
├── requirements-dev.txt       # Local development & testing dependencies
├── pytest.ini                 # Pytest configuration
├── vercel.json                # Vercel serverless deployment routing
├── app.py                     # Streamlit local web dashboard
├── train.py                   # Classical training & multi-model benchmark CLI
├── train_quantum.py           # Variational Quantum Classifier (VQC) training CLI
├── RUN.bat                    # Windows batch launcher
├── RUN.ps1                    # PowerShell launcher
├── api/                       # Vercel Serverless REST API
│   ├── index.py               # Main API handler & routing
│   ├── scan.py                # POST /api/scan endpoint
│   ├── batch.py               # POST /api/batch endpoint
│   ├── metrics.py             # GET /api/metrics endpoint
│   └── health.py              # GET /api/health endpoint
├── public/                    # Production Web Application
│   └── index.html             # Responsive SOC threat scanner & benchmark dashboard
├── pages/                     # Streamlit multi-page app
│   └── 1_Quantum_Lab.py       # Interactive Quantum VQC comparison page
├── src/                       # Core Detection Engine
│   ├── __init__.py
│   ├── features.py            # 25-feature invariant lexical extractor
│   ├── data_loader.py         # Dataset loader (generic CSV & PhiUSIIL) & domain grouping
│   ├── model.py               # XGBoost (GPU) / LightGBM / RF / Logistic pipelines & threshold tuning
│   ├── tree_ensemble.py       # Pure-NumPy XGBoost/LightGBM inference (no native library needed)
│   ├── quantum.py             # Pure NumPy state-vector quantum circuit simulator
│   └── quantum_model.py       # Angle scaler & hybrid VQC training pipeline
├── tests/                     # 87 unit and integration tests
│   ├── test_features.py       # 13 feature extraction tests
│   ├── test_features_extra.py # 4 IP, Punycode & edge-case tests
│   ├── test_data_loader.py    # 8 data loading & validation tests
│   ├── test_model.py          # 7 model training & inference tests
│   ├── test_quantum.py        # 10 quantum simulator & VQC gradient tests
│   └── test_tree_ensemble.py  # URL canonicalisation & NumPy XGBoost/LightGBM export tests
├── models/                    # Serialized production models
│   ├── model.joblib           # Trained XGBoost (NumPy export) + scaler + calibrated threshold
│   ├── quantum_model.joblib   # Trained VQC circuit weights + angle scaler
│   └── feature_names.json     # 25-feature schema
└── results/                   # Verified evaluation artifacts
    ├── metrics.json           # Production model test metrics
    ├── quantum_metrics.json   # Quantum VQC training history & loss
    ├── benchmark_comparison.json # Multi-model cross-split benchmark
    └── test_predictions.csv   # Predictions on held-out test split
```

---

## 📊 Benchmark Results & Performance Findings

**Dataset:** 450,176 labelled URLs (345,738 legitimate / 104,438 phishing), reduced to **443,115** after de-duplication. Evaluated on held-out test data; the headline split is **domain-disjoint** (84,293 test URLs from domains never seen in training).

### ⚠️ Removing dataset shortcuts

Raw URL datasets often contain collection artifacts that a model learns instead of real phishing signals:

- **Scheme / `www.`:** 99.8% of legitimate URLs start with `https://www.` versus 0.7% of phishing URLs. Left in, the model learns *"https ⇒ safe"*, which is false in practice (most modern phishing sites use HTTPS).
- **HTML escaping:** some phishing URLs contain `&amp;` instead of `&`.
- **Duplicates:** 7,061 URLs become identical once the scheme/`www.` is removed (3 with conflicting labels). These are de-duplicated so the same URL can't appear in both train and test sets.

Every URL is therefore canonicalised by `model_input_url()` in `src/features.py` (scheme and leading `www.` removed, HTML entities decoded, **full host + path + query kept**) both at training and at scan time. An earlier version trained on the PhiUSIIL dataset reported ~99% scores, but PhiUSIIL contains no legitimate URLs with a path, so that model flagged real pages such as `https://en.wikipedia.org/wiki/Phishing` as phishing. The numbers below are lower, but they reflect real-world behaviour.

### ⚡ GPU training

The production model is **XGBoost trained on an NVIDIA GPU** (CUDA, `tree_method="hist"`). On an RTX 3050 Laptop GPU, fitting 300 trees on 309,613 URLs takes **~4 seconds**. `train.py` uses the GPU automatically when one is available and falls back to CPU otherwise.

### 📈 Multi-Model & Split Strategy Benchmark

| Split Strategy | Model Architecture | Phishing Recall | Precision | F1-Score | False Positive Rate | Inference Latency |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Domain-Disjoint** | **XGBoost (Production, GPU-trained)** | **75.86%** | **76.23%** | **0.7604** | **7.15%** | **0.17 ms** |
| Domain-Disjoint | LightGBM | 74.04% | 75.70% | 0.7486 | 7.18% | 0.10 ms |
| Domain-Disjoint | Random Forest | 70.92% | 79.68% | 0.7505 | 5.47% | <0.01 ms |
| Domain-Disjoint | Logistic Regression | 56.87% | 62.37% | 0.5949 | 10.37% | <0.01 ms |
| Random Stratified | XGBoost | 85.37% | 77.24% | 0.8110 | 7.09% | 0.18 ms |
| Random Stratified | LightGBM | 81.70% | 75.91% | 0.7870 | 7.30% | 0.16 ms |
| Random Stratified | Random Forest | 85.33% | 76.79% | 0.8084 | 7.26% | <0.01 ms |
| Random Stratified | Logistic Regression | 54.06% | 67.83% | 0.6017 | 7.22% | <0.01 ms |
| Random Stratified | VQC (4-Qubit Sim) | 24.58% | 80.55% | 0.3767 | 1.67% | 0.42 ms |

The 4-qubit VQC uses only four features (`path_length`, `entropy_url`, `entropy_domain`, `num_sensitive_keywords`), so it is precise but misses most phishing; it contributes 20% of the combined score.

### 🔬 Held-Out Confusion Matrix (Domain-Disjoint: 84,293 Unseen-Domain URLs)
* **True Negatives (Legitimate Correctly Passed):** 60,103
* **False Positives (Legitimate Flagged):** 4,627
* **False Negatives (Missed Phishing):** 4,723
* **True Positives (Phishing Correctly Caught):** 14,840
* **Calibrated Decision Threshold ($\tau$):** `0.43` | **ROC-AUC:** `0.9306` | **PR-AUC:** `0.8542`

The production model is exported to a pure-NumPy tree ensemble (`src/tree_ensemble.py`) whose predictions match XGBoost to within 1e-6, so the serverless API needs neither XGBoost/CUDA nor LightGBM's native OpenMP library at runtime.

---

## 🌐 Threat Intelligence Integration

Q-Sentinel integrates with **AlienVault OTX & Threat Feeds** to provide real-time domain lookups:

- **Campaign Detection:** Identifies URLs linked to active credential harvesting campaigns
- **Phishing Indicators:** Flags known high-risk domains and malicious top-level domains
- **Zero-SSRF Inspection:** Pure lexical and offline database lookups ensure safe analysis without probing the remote target

The API keys can be securely stored in `.env` (protected by `.gitignore`) and are never exposed to client-side browsers.

---

## 🕵️ Domain Impersonation & Security Engine

On top of the ML models, Q-Sentinel runs an offline, evidence-based security layer (`src/typosquatting.py`, `src/security.py`, `src/character_evidence.py`):

- **Typosquatting detection:** leetspeak/numeric substitutions (`0→o`, `1→l`, `rn→m`, `vv→w`), character repetition, omission and transposition, scored with Damerau-Levenshtein distance against known brands
- **Homoglyph & IDN attacks:** Unicode look-alike characters (e.g. Cyrillic `о` for Latin `o`) and Punycode (`xn--`) domains
- **Combosquatting & subdomain masquerading:** brand names mixed with lure words, or placed in a subdomain of an unrelated domain
- **SSRF protection:** URL validation and sanitization before any analysis, with no outbound requests to the scanned target
- **Character-level evidence:** every scan returns a `character_evidence` breakdown showing exactly which characters triggered phishing indicators
- **5-tier classification** of results instead of a plain safe/phishing label

---

## 🚀 How to Run

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-clauds-plan.git
cd vtu-hc-clauds-plan

python -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

### 2. Run the 87 Automated Test Suite
```bash
python -m pytest tests/ -v
```

### 3. Launch the Local Streamlit App
```bash
streamlit run app.py
```
The dashboard opens at `http://localhost:8501` featuring the URL Scanner and Quantum Lab.

### 4. Train & Benchmark Models
```bash
# Train the production XGBoost model (uses an NVIDIA GPU automatically if available):
python train.py --data "path/to/URL dataset.csv" --url-col url --label-col type

# Train Quantum VQC:
python train_quantum.py --data "path/to/URL dataset.csv" --url-col url --label-col type --max-train 600

# Run comprehensive comparative benchmark (XGBoost, LightGBM, RF, Logistic Regression x 2 splits):
python train.py --data "path/to/URL dataset.csv" --url-col url --label-col type --benchmark
```

---

## 🎬 Demo Video & Working Prototype

- **Live Production App:** [https://qsentinental.vercel.app](https://qsentinental.vercel.app)
- **Demo Video (YouTube):** [Watch the demo](https://youtu.be/LQtrbrABnbw?si=Ebv2eoGLbYADO3tc)
- **Working Prototype (Web Dashboard):** Launch locally with `streamlit run app.py`

- **Interactive Pages:**
  - **URL Scanner:** Single URL analysis with Classical XGBoost + Quantum VQC simulation
  - **Quantum Lab:** Parameterized circuit schematic, loss convergence, and comparative metrics
  - **Batch Analysis:** Upload CSV or paste multiple URLs and export analysis results
  - **Evaluation:** Model performance metrics, benchmark comparisons, and confusion matrix

- **Sample Test URLs:**
  - ✅ `https://www.google.com` (Expected: 🟢 LOW RISK)
  - ✅ `https://github.com` (Expected: 🟢 LOW RISK)
  - ✅ `http://paypa1-verify.com/login?token=123` (Expected: 🔴 CRITICAL THREAT)
  - ✅ `http://192.168.1.1/admin` (Expected: 🔴 CRITICAL THREAT)

---

## 🔁 How to Push Code

### Configure Git (first time only)

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

### Everyday workflow

```bash
# 1. Get the latest changes
git checkout main
git pull origin main

# 2. Create a branch for your work
git checkout -b feature/my-feature

# 3. Commit your work
git add .
git commit -m "feat: add phishing detection for new URL patterns"

# 4. Push the branch
git push -u origin feature/my-feature

# 5. Open a Pull Request on GitHub and request a review
#    https://github.com/vtu-qiskit-fall-fest-2026/vtu-hc-clauds-plan

# 6. After approval, merge into main
git checkout main
git pull origin main
git branch -d feature/my-feature
```

### Commit message convention

| Prefix | Meaning |
| :--- | :--- |
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `test:` | Adding or fixing tests |
| `refactor:` | Code restructure |
| `chore:` | Build/config changes |

---

## ✅ Submission Checklist

- [x] Repository created and configured ✅
- [x] All team members added as collaborators ✅
- [x] `README.md` updated with real quantum-classical architecture and metrics ✅
- [x] Dependencies committed (`requirements.txt`, `requirements-dev.txt`) ✅
- [x] Source code implemented (`src/`, `tests/`, `models/`, `results/`, `api/`, `public/`) ✅
- [x] Code pushed to `main` and verified ✅
- [x] Interactive web dashboard deployed to production ([https://qsentinental.vercel.app](https://qsentinental.vercel.app)) ✅
- [x] 87 automated tests passing (`tests/`) ✅
- [x] Quantum Variational Classifier implemented with parameter-shift gradients ✅
- [x] Model trained on 443,115 URLs (GPU) with domain-disjoint validation and threshold calibration ✅

---

## 📚 Resources

| Resource | Link |
| :--- | :--- |
| ⚛️ Qiskit Documentation | https://docs.quantum.ibm.com/ |
| 🔐 AlienVault OTX | https://otx.alienvault.com/api |
| 📊 Streamlit Docs | https://docs.streamlit.io/ |
| 🤖 XGBoost Docs | https://xgboost.readthedocs.io/ |
| 🤖 LightGBM Docs | https://lightgbm.readthedocs.io/ |
| 🤖 scikit-learn | https://scikit-learn.org/ |
| 📋 GitHub Docs | https://docs.github.com/ |
| 🐍 Python Official | https://python.org/ |

---

## 📄 License & Attribution

This project is authored and submitted by **Narasimha Kulkarni** for the **VTU-Qiskit Fall Fest Hackathon 2026** (VTU Belagavi in association with IBM Quantum).

All code, documentation, and research are copyright © 2026 and licensed under the [MIT License](LICENSE).

---

<div align="center">

**Q-Sentinel** · Team ID `VTU-QFF-HC-0191` · Tier `Online`

Built with ⚛️ Quantum Machine Learning + ⚡ Gradient Boosted Trees + 🌐 Threat Intelligence for the VTU-QFF Hackathon — Visvesvaraya Technological University, Belagavi

<br/>

<small>

© 2026 Visvesvaraya Technological University, Belagavi, in association with IBM Quantum. All rights reserved.

</small>

<br/><br/>

[⬆ Back to Top](#q-sentinel)

</div>
