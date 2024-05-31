
---
# Packet Sniffer GUI

A simple packet sniffer GUI tool built with Python, Tkinter, and Pyshark. This tool allows users to capture network packets on a specified network interface and display packet information in real-time.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Contributing](#contributing)

## Overview

The Packet Sniffer GUI tool captures network packets on a specified network interface and displays detailed packet information in a user-friendly interface. It is built using Python's Tkinter for the GUI and Pyshark for packet capturing.

## Features

- **Start/Stop Packet Capture:** Easily start and stop packet capturing on a specified network interface.
- **Real-time Packet Display:** View detailed packet information in real-time within the GUI.
- **Responsive GUI:** The interface is designed to be responsive and user-friendly.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Anandkp21/PRODIGY_CS_TASK_05.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd packet-sniffer-gui
   ```

3. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

   Alternatively, you can install dependencies individually:
   ```sh
   pip install tkinter
   pip install pyshark
   ```

## Usage

1. **Run the packet sniffer GUI:**
   ```sh
   python packet_sniffer_tool.py
   ```

2. **Specify the network interface:**
   - Enter the name of the network interface you want to capture packets from in the "Interface" entry field.

3. **Start and stop capturing:**
   - Click "Start Capture" to begin capturing packets.
   - Click "Stop Capture" to stop capturing packets.

4. **View captured packets:**
   - Packet information will be displayed in real-time in the text area of the GUI.

## Example

### Running the Packet Sniffer GUI
```sh
$ python packet_sniffer_tool.py
```

### Using the GUI
1. Enter the network interface (e.g., `eth0`, `wlan0`) in the "Interface" field.
2. Click "Start Capture" to begin capturing packets.
3. Packet information will be displayed in the text area.
4. Click "Stop Capture" to end the capture session.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



