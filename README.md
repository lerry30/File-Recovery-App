# FrankensFile

A desktop application that recovers files from flash drives or other types of
drives. Implemented a user interface that allows users to select specified file types for
recovery.

!['FrankensFile UI'](/assets/frankensfile.png)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

To install required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python main.py
```

### Usage steps:

1. Choose the Disk (C:, E:, F:, etc.) that you want to recover.
2. Select file extensions to recover specific files only.
3. Add the destination folder where recovered files will be stored.

## Features

- Recovers the following file types:
    - PNG
    - JPG, JPEG
    - PDF