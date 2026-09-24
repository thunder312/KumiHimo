# KumiHimo – Kumihimo Planner

A planner for kumihimo on the round disk with 32 slots (Kongo Gumi, 8 or 16 strands) and the square plate (1–12 / A–H; flat braid and square braid with 8 strands each).
From a pattern it works out the starting setup, the braiding moves and the thread requirements; the braiding plan can be exported as a PDF.

## Contents of the folder

| File | Purpose |
|---|---|
| `kumihimo-planer.html` | The program. Double-click to open it in the browser; it also works offline. |
| `kumihimo_modell.py` | The same model in Python, for checking and further development. |
| `Muster/` | Saved patterns as JSON files. |
| `README.en.md` / `README.en.html` | This guide (as text or for the browser). |
| `README.md` / `README.html` | The guide in German. |
| `kumihimo-planer.zip` | Everything above in one package, always the current version. |

The planner keeps “My patterns” in the browser you use.
Only the files in the `Muster` folder are permanent.

## Running it at home in the browser

The planner is a single HTML file and needs no installation and no server.

1. **Download and unpack the ZIP**, for example to `Documents\KumiHimo`. Important: really unpack it, do not open it from inside the ZIP.
2. **Double-click `kumihimo-planer.html`.** It opens in your default browser (current Chrome, Edge or Firefox).
3. **Load patterns:** under “Export” or “Patterns” click “Open files” and choose files from the `Muster` folder (several at once work).
4. **Keep patterns:** “Save as file” puts a JSON file in your downloads folder; move it into the `Muster` folder.

Good to know:

- **Offline:** planner, editor and braiding guide work without internet. Only the PDF export loads the PDF library jsPDF from the internet the first time; without a connection, fallback fonts are also shown.
- **“My patterns” lives in the browser**, not in the folder. A different browser, a different location of the HTML file or clearing browser data shows an empty list. Only the files in the `Muster` folder are permanent.
- **Guide:** `README.en.html` in the same folder; the “Guide” button in the planner opens it.
- **Tablet or phone:** local HTML files are often awkward to open there. It is easier to put the folder on a web server, for example with GitHub Pages in the repository [thunder312/KumiHimo](https://github.com/thunder312/KumiHimo) (Settings → Pages → branch `main`). Then you open the planner through a normal web address.
- **New version:** simply unpack the new ZIP over the old folder. The `Muster` folder stays as long as you do not overwrite your own files.

## How to use it

Top right you switch the language (**DE** / **EN**); the browser remembers your choice. At the top you choose the tool (**Round disk** or **Square plate**), below that the work steps:

1. **Patterns**: templates, your own patterns and (round disk) the pattern catalogue. A click loads the pattern and opens the editor; all later steps are updated.
2. **Editor**: choose strand count and colours and paint in the grid (round disk) or on the braid faces (square plate). On the right you see the braidable result and “How well it fits”. “Apply to disk” jumps to the braiding guide.
3. **Braiding guide** (view only, colours come from Patterns and Editor): numbering direction, disk move by move, cord and pattern image, setup and braiding plan, thread requirements.
4. **Export**: save patterns (My patterns, file, code) and the braiding plan as PDF.

Each large section (e.g. Pattern editor, Disk and cord, Thread requirements) can be collapsed with the arrow on the right; the browser remembers this, as well as the last open work step.
For the PDF export the PDF library jsPDF is loaded from the internet once.

## Square plate tab (first version)

- Plate with slots 1–12 at the top and bottom, A–H on the left and right (from top to bottom); the plate is not turned.
- Braid type “Flat braid, 8 strands” with the moves after Fire Mountain Gems (steps 5–18): 14 moves per pass, 8 of them across the plate, 6 resets.
- Braid type “Square braid, 8 strands” after Fire Mountain Gems (Square Braids): 12 moves per pass, 8 across, 4 resets; the braid image shows all four faces.
- Pattern editor: paint freely on all braid faces (columns = target slots of that face, row groups = passes); the planner finds the braidable setup (majority per strand) and applies it with “Apply to plate”.
- In the braiding guide the plate is view only; setup templates: Top/bottom, Alternating, Outer/inner, Single colour.
- Step through move by move, braiding plan for two passes, thread requirements.
- Export: save patterns (My patterns, file, code) and the braiding plan as A4 PDF (plate image, setup, moves for two passes, thread requirements). Saved patterns appear under “1 Patterns” → “My patterns”.
- “Open files” accepts round and square patterns in both tabs and sorts them correctly.
- The braid image is schematic (stitch on the face the strand moves to) and has not yet been checked against a real braid.

## Kongo Gumi rules (result of the model)

- **Move:** top right to bottom right, bottom left to top left, then turn the disk anticlockwise until the next pair is at the top.
- **Stitches:** each move lays two stitches. The strands move in a fixed order, the pattern chain.
- **Repeat:** in the grid every pattern repeats every 4 rows.
- **Twin stitch:** row r+2 is row r shifted by half a round. Each strand supplies exactly these two stitches.
- **Lengthwise:** stripes in up to 4 colours are possible, each colour appears twice, opposite each other. On the cord they become spirals.
- **Crosswise:** full rings are only possible in 2 alternating colours.
- **Check:** 16 strands in 2 colours give 1162 different patterns, as in the article “Changing Spots” (Bridges 2022).

The stitch shape in the previews is schematic. The take-up factor for the thread requirements (default 1.5) should be measured with a sample.

## Pattern file format

```json
{
  "kumihimo": 1,
  "name": "Band rot-orange-gelb-weiß",
  "n": 16,
  "neck": "0321032103210321",
  "pal": ["#C0392B", "#E67E22", "#F1C40F", "#F7F4EC"],
  "names": ["Rot", "Orange", "Gelb", "Weiß"],
  "matrix": ["01230123", "..."]
}
```

- `n`: number of strands (8 or 16).
- `neck`: colour number for each position of the pattern chain (index into `pal`).
- `pal`, `names`: colours as hex codes and their names.
- `matrix` (optional): the editor drawing, rows from top to bottom, `.` is an empty cell.

Square plate patterns have `"typ": "eckig"`, plus `struct` (`flach8` or `vierkant8`), `col` (colour number per strand in setup order) and optionally `editor` with the drawings per braid face.

## Python model

```
python kumihimo_modell.py muster Muster/band-rot-orange-gelb-weiss.json
python kumihimo_modell.py zeichnung 16 "ABCDABCD/ABCDABCD/ABCDABCD/ABCDABCD"
python kumihimo_modell.py katalog 16
```

The Python model prints its output in German.

## Download and contact

- Current version as ZIP: “Download ZIP” at the top right of the planner (contains planner, guide, Python model and the sample patterns).
- Guide in the browser: `README.en.html`.
- Voluntary support: the planner is free. If you like, you can [buy me a coffee](https://buymeacoffee.com/dertl).

© 2026 Daniel Ertl · [daniel-ertl.de](https://daniel-ertl.de) · [GitHub: thunder312](https://github.com/thunder312) · dertl@web.de
