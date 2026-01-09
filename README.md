# Mini Projects — Learning Collection
This repository is a personal collection of small, focused projects created to learn and demonstrate ideas across Python, GUI toolkits, and mobile development. Each project is self-contained with its own README and an entry point you can run locally.

## Purpose
A hands-on space for short experiments, example apps, and utility scripts that are easy to read, run, and modify.

## Quick Start
- **Python projects:** Create and activate a virtual environment, install dependencies, then run the project's entry point. Example (PowerShell):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt   # if the project has one
python main.py
```

- **JS / React Native projects:** Install node deps with `npm install` (or `yarn`) and follow the specific project's README for platform-specific steps.

## What you'll find here
- **Small, focused demos:** Each folder contains a short project that demonstrates a single idea (CLI tools, simple GUIs, utilities, or small apps).
- **Learn-by-reading:** Code is kept compact so you can read and modify quickly.

## Guidelines for running projects
- Check a project's own `README.md` first for prerequisites and platform-specific instructions.
- Prefer creating a virtual environment for Python projects to avoid global dependency conflicts.
- If a project uses external libraries, install them via the project's `requirements.txt` before running.

## Contributing / Adding Projects
- Add a new folder with a short, descriptive name and include a `README.md` explaining purpose and run steps.
- Keep projects small and focused; include a `requirements.txt` for Python projects where applicable.
- Open a pull request with a brief description and sample usage instructions.

## Troubleshooting & Tips
- If you hit an import error, verify you're running inside the project's virtual environment and that dependencies are installed.
- For GUI projects (Kivy, Tkinter), ensure your environment supports windowed apps and required system libraries are installed.

## Contact / Questions
If you want help running a specific project or want me to expand any README, tell me which project and I’ll update its instructions.