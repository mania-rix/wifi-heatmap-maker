# Contributing to Wi‑Fi Heat‑Map Maker

Thanks for helping map the airwaves! This project stays intentionally tiny, so clear PRs and good issues are golden. 🚀

---

## Quick start

```bash
git clone https://github.com/<your‑fork>/wifi-heatmap-maker
cd wifi-heatmap-maker
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -v          # smoke tests should pass
```

---

## Issue labels

| Label              | Meaning                                               |
| ------------------ | ----------------------------------------------------- |
| **help‑wanted**    | Great first tasks for newcomers                       |
| **bug**            | Reproducible defect, needs a fix                      |
| **enhancement**    | New feature or improvement                            |
| **platform‑port**  | Support for Mac, Windows, or alternate tools          |

---

## Open *help‑wanted* tasks

- **5 GHz scanning** – add `iwlist` fallback for dual‑band chipsets.  
- **Mac OS support** – parse output of `airport -s`.  
- **JSON export** – `--json` flag to dump survey data for other tools.  
- **Interpolation** – replace scatter plot with IDW or kriging for smoother maps.  
- **README GIF update** – record demo on a multi‑floor venue.

Feel free to propose more!

---

## Coding guidelines

* **Black** + **isort** for styling (`black . && isort .` before commit).  
* Python 3.11+ typing syntax.  
* Keep the core CLI ≤150 LOC; new logic → helper modules.  
* One feature / bug‑fix per PR; update or add tests in **`tests/`**.

---

## Pull‑request checklist

- [ ] Code formatted with **black** and imports ordered with **isort**.  
- [ ] `pytest -v` passes locally and in CI.  
- [ ] If CLI flags / output change, update **README.md**.  
- [ ] Commit(s) signed‑off (`Signed‑off‑by: Your Name <email>`).

---

## Code of conduct

Be respectful and constructive—reviewers and contributors are volunteers.  
No offensive language or dismissive comments.

Happy surveying! 📡
