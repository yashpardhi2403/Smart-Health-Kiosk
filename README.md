````markdown
# AD8232 ECG Filter Project

This repository contains filtering code and resources for processing ECG signals using the AD8232 module.

## Overview

The **AD8232** is a single-lead heart rate monitor front end designed to extract, amplify, and filter small bioelectric signals. This project focuses on post-processing the analog output of the AD8232 module to produce a clean ECG waveform suitable for analysis and visualization.

## Features

- Raw ECG signal acquisition from AD8232
- Digital signal filtering (e.g., low-pass, high-pass, bandpass)
- Real-time processing pipeline (if used with microcontroller or embedded platform)
- Preprocessing for heart rate analysis or QRS detection

## Usage

### Hardware Requirements

- AD8232 ECG Module
- Microcontroller (e.g., ESP32, Arduino)
- ECG electrodes and leads
- Optional: Serial plotter or visualization tool (e.g., Python + Matplotlib, Processing)

### Software Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ex2uply/ad8232-filter.git
   cd ad8232-filter
````

2. Follow the instructions in the relevant script (e.g., Arduino `.ino`, Python `.py`, or C file) to load and run filtering logic.

3. Connect AD8232 output to the microcontroller's analog input pin.

4. Upload the code and start visualizing the filtered ECG waveform.

## File Structure

```
ad8232-filter/
├── filters/            # Filter implementations (e.g., moving average, Butterworth)
├── src/                # Main application logic
├── test_signals/       # Sample raw ECG signals for offline testing
└── README.md           # Project documentation
```

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss proposed modifications.

## Final Output
![IMG-20250506-WA0007 1](https://github.com/user-attachments/assets/530b3804-ac0d-4642-b6b3-f70985975f81)


## License

MIT License

## References

* [Analog Devices AD8232 Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/AD8232.pdf)
* Biomedical Signal Processing literature for filter design
