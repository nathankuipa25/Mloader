
# Mloader - Smart Kivy/KivyMD KV Loader

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Kivy](https://img.shields.io/badge/kivy-2.x-green.svg)](https://kivy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Mloader is an intelligent utility that automates KV file loading for Kivy/KivyMD widgets. It eliminates hard-coded file references and reduces errors from misspelled KV filenames, making your widgets truly self-contained and portable.

## Features

- 🔍 **Auto-detection** - Automatically finds and loads the matching KV file for your Python class
- 📁 **Fallback loading** - Loads all KV files in the directory if no match is found
- 🚫 **Duplicate prevention** - Prevents loading the same KV file multiple times
- 🛡️ **Error handling** - Graceful handling of missing files with clear logging
- 📦 **Zero configuration** - Works out of the box with any project structure

## Installation

```bash
pip install mloader
```

Or simply copy `mloader.py` into your project directory.

## Quick Start

```python
from kivymd.uix.screen import MDScreen
from mloader import load_kv

# Auto-detects and loads the matching .kv file!
load_kv()

class MyCustomScreen(MDScreen):
    pass
```

## How It Works

Mloader uses Python's `inspect` module to trace the calling file, then:

1. **Looks for a matching KV file** - Searches for `[your_filename].kv` in the same directory
2. **Falls back to glob loading** - If no match, loads all KV files in the directory
3. **Prevents duplicates** - Checks `Builder.files` before loading
4. **Returns loaded files** - Provides a list of successfully loaded KV files

## Advanced Usage

### Manual File Specification

```python
from mloader import load_kv

# Specify the Python file manually
load_kv(mainfile="/path/to/your/file.py")
```

### Check Loaded Files

```python
loaded = load_kv()
print(f"Loaded KV files: {loaded}")
```

### Directory Structure Example

```
project/
├── main.py
├── widgets/
│   ├── custom_button.py      # load_kv() loads custom_button.kv
│   ├── custom_button.kv
│   ├── custom_label.py       # load_kv() loads all .kv files
│   └── custom_label.kv
```

## Why Mloader?

| Without Mloader | With Mloader |
|----------------|--------------|
| `Builder.load_file('mywidget.kv')` | `load_kv()` |
| Hard-coded filenames | Auto-detection |
| Risk of typos | Zero spelling errors |
| Manual file tracking | Automatic duplicate prevention |
| Fragile imports | Portable widgets |

## Requirements

- Python 3.x
- Kivy ≥ 2.0.0 (for KivyMD support)

## Contributing

Found a bug or have a feature request? Please open an issue on [GitHub](https://github.com/yourusername/mloader).

## License

MIT © Nathan R.K

## Support

If you find mloader helpful, consider starring the repository or sharing it with other Kivy developers!
