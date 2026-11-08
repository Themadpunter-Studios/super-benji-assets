# Super Benji Assets

Assets for the Super Benji series that can be used to make Super Benji related media.

## How to Use

Open whatever files you need in a vector graphics program. Adobe Illustrator source files can be found in src/ and .svg files
can be found in svg/. SVG files are created automatically from the .AI files.

## Super Benji Assets.sb3

This Scratch project file contains most of the assets used in the Super Benji Show and movies. Most of the assets are updated up to the
spin-offs (Cooper, Banana, A Very Benji Christmas). A lot of assets will be in this file. This file is being migrated to the various
subfolders for organization.

## Other Folders

These folders contain .ai files for use in Adobe Illustrator or VectorCraft (or similar programs). The svg subfolder also contains SVG
versions of each of these files for those who use other programs to make Super Benji content.

### Exporting AI files to SVG

Run `python export_ai_to_svg.py` from any directory to recursively export every `.ai` file in `src` to `svg`, preserving the folder
structure. The script uses the VectorCraft CLI's `convert` command and looks for it on `PATH` or in the standard
`OneDrive\Documents\ArtCraft\vectorcraft` install folder.

If the CLI is not on `PATH`, provide its executable path:

```powershell
python export_ai_to_svg.py --vectorcraft-cli "C:\Users\thema\OneDrive\Documents\ArtCraft\vectorcraft\vectorcraft-cli.exe"
```

You can also set the `VECTORCRAFT_CLI` environment variable or override the folders with `--source` and `--destination`.
