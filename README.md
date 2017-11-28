# Galactus

Finds all big files and compresses them.

## Setup

Python version should be same as specificed in `runtime.txt`

Create a virtual environment with `python3 -m venv venv`

Activate the virtual environment created with `source venv/bin/activate`

Install all dependencies with `pip install -r requirements.txt`

## Run

```
python app.py
```

## Todo

- [ ] Sort all files with size from a given directory.
- [ ] Compress files above a given size.
- [ ] Move the compressed file to s3(or any other place).
- [ ] Delete the big files.
