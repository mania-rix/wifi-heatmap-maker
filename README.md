# Wi‑Fi Heat‑Map Maker

Turn any Linux laptop into a floor‑plan Wi‑Fi survey kit in **<10 minutes**.

![demo](docs/demo.gif)

---
## Quick Start
```bash
pip install -r requirements.txt
python -m wifi_heatmap.cli parse --csv survey.csv      # walk & press ENTER
python -m wifi_heatmap.cli render survey.csv heatmap.svg
```

## Why?
Existing open‑source tools are bulky, GUI‑only, or Windows‑centric. This repo stays CLI‑first, pure‑Python, and MIT‑licensed so anyone can fork & extend.

## Contributing
See CONTRIBUTING.md. Good first issues are tagged `help‑wanted`.

## License
MIT
