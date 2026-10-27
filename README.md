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
    ├─→ Classical Engine: LightGBM GBDT (Calibrated Threshold τ = 0.830)
    │     (99.17% Phishing Recall on Domain-Disjoint Unseen Hosts)
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
3. **Classical ML Engine**: LightGBM Gradient Boosted Decision Trees tuned via validation threshold calibration to minimize false negatives and maximize phishing recall.
4. **Quantum VQC Engine**: Parameterized 4-qubit quantum circuit simulator utilizing Pauli rotation encodings ($R_y(\theta), R_z(\theta)$) and parameter-shift gradients.
5. **Threat Intelligence Integration**: AlienVault OTX / PhishTank campaign indicators for real-world threat correlation.
6. **Interactive Dashboard**: Modern dark-mode SOC dashboard on Vercel + local Streamlit application with interactive Quantum Lab.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.11 / 3.12 / 3.14+ |
| **Quantum Simulation** | NumPy Statevector Engine & Aer-compatible Parameter-Shift Circuits |
| **Classical ML** | LightGBM, scikit-learn, joblib |
| **Data & Feature Engineering** | pandas, numpy, scipy |
| **Web Frontend** | Tailwind CSS, Chart.js, Streamlit |
| **Serverless API** | Vercel Edge Serverless Functions (Python 3.12 runtime) |
| **Threat Intel** | AlienVault OTX & Known Phishing IOC Feeds |
| **Testing** | pytest (42 unit & integration tests) |
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
│   ├── data_loader.py         # PhiUSIIL loader & domain-disjoint splitting
│   ├── model.py               # LightGBM / RF / Logistic pipelines & threshold tuning
│   ├── quantum.py             # Pure NumPy state-vector quantum circuit simulator
│   └── quantum_model.py       # Angle scaler & hybrid VQC training pipeline
├── tests/                     # 42 unit and integration tests
│   ├── test_features.py       # 13 feature extraction tests
│   ├── test_features_extra.py # 4 IP, Punycode & edge-case tests
│   ├── test_data_loader.py    # 8 data loading & validation tests
│   ├── test_model.py          # 7 model training & inference tests
│   └── test_quantum.py        # 10 quantum simulator & VQC gradient tests
├── models/                    # Serialized production models
│   ├── model.joblib           # Trained LightGBM pipeline + calibrated threshold
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

Evaluated on 40,000 URLs from the **PhiUSIIL Phishing URL Websites Dataset** across 7,923 held-out test URLs:

### 📈 Multi-Model & Split Strategy Benchmark

| Split Strategy | Model Architecture | Phishing Recall | Precision | F1-Score | False Positive Rate | Inference Latency |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Domain-Disjoint** | **LightGBM (Production)** | **99.17%** | **99.97%** | **0.9957** | **0.02%** | **0.01 ms** |
| Domain-Disjoint | Random Forest | 99.14% | 100.00% | 0.9957 | 0.00% | 0.08 ms |
| Domain-Disjoint | Logistic Regression | 98.60% | 99.97% | 0.9928 | 0.02% | 0.005 ms |
| Random Stratified | LightGBM | 98.99% | 99.94% | 0.9946 | 0.04% | 0.01 ms |
| Random Stratified | Random Forest | 99.02% | 99.91% | 0.9946 | 0.06% | 0.08 ms |
| Random Stratified | Logistic Regression | 98.96% | 99.88% | 0.9942 | 0.08% | 0.005 ms |
| Random Stratified | VQC (4-Qubit Sim) | 76.72% | 99.97% | 0.8681 | 0.01% | 0.42 ms |

### 🔬 Held-Out Confusion Matrix (Domain-Disjoint: 7,923 Unseen Domain URLs)
* **True Negatives (Legitimate Correctly Passed):** 4,789
* **False Positives (Legitimate Flagged):** 1
* **False Negatives (Missed Phishing):** 26 (down from hundreds in uncalibrated baselines)
* **True Positives (Phishing Correctly Caught):** 3,107
* **Calibrated Decision Threshold ($	au$):** `0.830` | **ROC-AUC:** `0.9978` | **PR-AUC:** `0.9982`

---

## 🌐 Threat Intelligence Integration

Q-Sentinel integrates with **AlienVault OTX & Threat Feeds** to provide real-time domain lookups:

- **Campaign Detection:** Identifies URLs linked to active credential harvesting campaigns
- **Phishing Indicators:** Flags known high-risk domains and malicious top-level domains
- **Zero-SSRF Inspection:** Pure lexical and offline database lookups ensure safe analysis without probing the remote target

The API keys can be securely stored in `.env` (protected by `.gitignore`) and are never exposed to client-side browsers.

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

### 2. Run the 42 Automated Test Suite
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
# Train LightGBM with domain-disjoint splitting:
python train.py --split-mode domain_disjoint

# Train Quantum VQC:
python train_quantum.py --qubits 4 --layers 3

# Run comprehensive comparative benchmark:
python train.py --benchmark
```

---

## 🎬 Demo Video & Working Prototype

- **Live Production App:** [https://qsentinental.vercel.app](https://qsentinental.vercel.app)
- **Demo Video (YouTube):** [Watch the demo](https://youtu.be/LQtrbrABnbw?si=Ebv2eoGLbYADO3tc)
- **Working Prototype (Web Dashboard):** Launch locally with `streamlit run app.py`

- **Interactive Pages:**
  - **URL Scanner:** Single URL analysis with Classical LightGBM + Quantum VQC simulation
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
- [x] 42 automated tests passing (`tests/`) ✅
- [x] Quantum Variational Classifier implemented with parameter-shift gradients ✅
- [x] Model evaluated on 40,000 URLs with domain-disjoint validation and threshold calibration ✅

---

## 📚 Resources

| Resource | Link |
| :--- | :--- |
| ⚛️ Qiskit Documentation | https://docs.quantum.ibm.com/ |
| 🔐 AlienVault OTX | https://otx.alienvault.com/api |
| 📊 Streamlit Docs | https://docs.streamlit.io/ |
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
