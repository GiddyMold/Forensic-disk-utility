# Forensic Drive Backup Tool

A powerful and secure utility for duplicating drives with integrity checks and forensic-level data preservation. This tool ensures the accurate copying of data, verifies file authenticity, and logs essential metadata to maintain the integrity of your files and system during backup.

## Features

- **Drive Duplication**: Copy drives with full file system integrity checks.
- **File Integrity Verification**: Perform cryptographic hash comparisons to ensure the source and destination files are identical.
- **Authenticity Check**: Ensure the files remain authentic throughout the backup process.
- **File Tree & Metadata Collection**: Generates a complete file tree and collects metadata of the destination directory.
- **Read-Only Drive Management**: Set drives to read-only mode to prevent modification during the process.
- **Logging and Results**: Automatically generate a results folder containing detailed logs with timestamps, drive parameters, and file integrity data.
- **Cross-Platform Compatibility**: Works across different platforms with special handling for Unix-based systems.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/forensic-drive-backup.git
```

Run the Program

To use the tool, simply execute the script:

bash
Copy
Edit
python main.py
Input the Required Information

You will be prompted to enter the following details:

Name of the operation
Source path (the location of the drive you want to back up)
Source drive letter
Destination path (the location where the backup will be stored)
Process Overview

The tool will start by gathering information about the source drive and its file system.
It will perform the initial copy of the drive to the destination.
Hashes will be generated for file integrity checks.
After duplicating the drive, the file tree and metadata of the destination folder will be collected.
All results and logs will be saved for future reference.
Result Logs

After completing the process, the tool will output detailed logs including:

Start and end timestamps
Running time
Drive parameters
File hashes for integrity verification
Metadata of the destination folder
