# primes - C++ Prime Utilities for Python (pybind11 + scikit-build-core)

This project provides a small, fast C++ implementation of prime number utilities (`is_prime`, `nth_prime`) that is callable from Python using **pybind11** and built/installed with **scikit-build-core**.

## Quick Start (30 seconds)

```bash
# From the repo root
python3 -m pip install --user -U pip
python3 -m pip install --user -U scikit-build-core pybind11 cmake ninja
python3 -m pip install --user -e .

# Test
python3 -c "import primes; print(primes.nth_prime(1000))"
```

The instructions below describe a **clean, repeatable, user-level editable install** on a Linux system (e.g., a shared server), using Python and CMake.

---

## Features

- C++ implementation for performance
- Python bindings via pybind11
- Modern build system using CMake + scikit-build-core
- Editable install (`pip install -e .`) into **user site-packages**
- Clean Python API:

```python
import primes

print(primes.is_prime(97))  # True
print(primes.nth_prime(1000))  # 7919
```

---

## Project Layout

```
primes/
├── CMakeLists.txt
├── pyproject.toml
├── README.md
├── src/
│   └── primes_module.cpp
└── primes/
    └── __init__.py
```

### Naming Convention

- The **Python package** is named: `primes`
- The **compiled extension module** is named: `_primes`

This avoids name collisions and follows standard Python packaging practice.

---

## Requirements

- Python ≥ 3.9
- CMake ≥ 3.18
- A C++17 compiler
- pip

The build system will install:
- `scikit-build-core`
- `pybind11`
- `ninja`

---

## Installation (Editable, User Site-Packages)

These steps install the module into your **user-level Python environment** while keeping it editable for development.

> **Note on multi-Python systems**  
> If your system has more than one Python installation, replace `python3` in the commands below with the full path to the interpreter you want to use (e.g., `/usr/local/bin/python3`). This guarantees `pip` installs into the same environment you run.

### 1) Verify Python

```bash
python3 -c "import sys; print(sys.executable); print(sys.version)"
```

Make sure this is the Python you want to install into.

---

### 2) Install build dependencies

```bash
python3 -m pip install --user -U pip
python3 -m pip install --user -U scikit-build-core pybind11 cmake ninja
```

---

### 3) Editable install

From the **repo root**:

```bash
python3 -m pip install --user -e .
```

This will:
- Compile `_primes` using CMake
- Install an editable package into `~/.local/lib/pythonX.Y/site-packages/`

---

## Testing

```bash
python3 -c "import primes; print(primes.nth_prime(1000)); print(primes.is_prime(7919))"
```

Expected output:

```
7919
True
```

---

## Development Workflow

### Rebuilding after C++ changes

After editing `src/primes_module.cpp`:

```bash
# From the repo root
python3 -m pip install --user -e . -v
```

This forces a rebuild and reinstalls the extension.

---

### Clean rebuild (start fresh)

If you run into strange build or import issues, a full clean rebuild often helps:

```bash
# From the repo root
python3 -m pip uninstall -y primes
python3 -m pip install --user -e . --force-reinstall -v
```

This removes all cached CMake state and forces scikit-build-core to reconfigure and recompile from scratch.

---

## Debugging & Inspection

### Where is Python importing from?

```bash
python3 -c "import primes, inspect; print(inspect.getfile(primes))"
```

### Show installed packages

```bash
/usr/local/bin/python3 -m pip list
```

---

## Design Notes

- The compiled module is named `_primes` and lives inside the `primes` package
- `__init__.py` re-exports symbols to provide a clean API
- Exceptions thrown in C++ (`std::invalid_argument`) are mapped to Python `ValueError`

---

## License

This project is licensed under the MIT License.  
Copyright (c) 2026 Carl Salvaggio.

See the [LICENSE](LICENSE) file for details.

---

## Contact

**Carl Salvaggio, Ph.D.**  
Email: carl.salvaggio@rit.edu

[Chester F. Carlson Center for Imaging Science](https://www.rit.edu/science/chester-f-carlson-center-imaging-science)  
[Rochester Institute of Technology](https://www.rit.edu)  
Rochester, New York 14623  
United States
