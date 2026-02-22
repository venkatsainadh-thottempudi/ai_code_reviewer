# 🤖 AI Code Reviewer & Quality Assistant

An AI-powered static analysis tool that analyzes Python projects for:

- 📊 Docstring coverage
- 🧠 Cyclomatic complexity
- 📏 PEP 257 style compliance
- 🚨 Severity ranking
- ⚡ Parallel scanning with caching
- 📄 HTML report generation
- 🌐 Streamlit dashboard (with ZIP upload)

---

## 🚀 Features

### 🔍 Code Analysis
- Function & class parsing
- Docstring detection
- Coverage calculation
- Complexity scoring (via radon)
- Severity classification (INFO / WARNING / CRITICAL)

### ⚡ Performance Optimized
- Parallel file processing
- Smart SHA256-based caching
- Incremental analysis

### 📄 Reporting
- CLI output
- Downloadable HTML report
- Coverage metrics
- Severity breakdown charts

### 🌐 Web Dashboard
- Upload ZIP project
- File-wise coverage chart
- Severity distribution pie chart
- Downloadable report
- Clean professional UI (Streamlit)

### 🛠 DevOps Ready
- Pre-commit hook integration
- GitHub Actions CI
- Installable via pip
- Configurable via `pyproject.toml`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai_code_reviewer.git
cd ai_code_reviewer