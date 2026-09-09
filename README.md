# Filament Inventory

A small command-line inventory tracker for 3D printer filament spools.

## Requirements

- Python 3
- A terminal
- A barcode scanner that acts as a keyboard (optional)

## Run

From the project directory:

```sh
python3 app.py
```

The program repeatedly asks for a barcode. A barcode scanner can type directly into the barcode prompt.

## First Scan

When a barcode is not known, enter:

1. Manufacturer
2. Material
3. Color
4. Full spool weight in grams
5. Empty spool weight in grams

The spool type is then saved for future scans.

## Add Inventory

At the `Amount` prompt:

- Enter `s` for a complete spool.
- Enter the measured weight in grams for a used spool. The empty spool weight is subtracted automatically.

Data is saved after every scan.

## Data Files

The script creates these files in the project directory:

- `spools.csv`: saved spool types and their weights
- `inventory.csv`: full spool count, loose filament, and total weight

These files are ignored by Git when added to the local `.gitignore`.

## Notes

- The application currently runs continuously until interrupted with `Ctrl+C`.
- Success and error sounds use the `chime` package. If no audio device is available, the inventory logic still works, but no sound will play.
