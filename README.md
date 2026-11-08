# Super Benji Assets

Assets for the Super Benji series that can be used to make Super Benji related media.

## How to Use

Open whatever files you need in a vector graphics program. Adobe Illustrator source files can be found in src/, .svg files
in svg/, and .png files in png/. SVG and PNG files are created automatically from the .AI files.

## Scaling

For scaling purposes, Benji is 6'0". Therefore, 25.855333 pixels is equal to 1 foot. All source files should be reflective of this.
See Scaling.ai for various things in scale.

## Making New Human Characters

Most humans have two main colors for their scheme: A main gradient and a dark gradient. The main gradient is used in the body, cape,
and both shoes. The dark gradient is used in both arms. The main gradient is usually a gradient between two similar colors, and the
dark gradient is a version of that gradient with the lower color darker. Characters also have different eye colors and hair styles.

## Super Benji Assets.sb3

This Scratch project file contains most of the assets used in the Super Benji Show and movies. Most of the assets are updated up to the
spin-offs (Cooper, Banana, A Very Benji Christmas). A lot of assets will be in this file. This file is being migrated to the various
subfolders for organization.

## Other Folders

These folders contain .ai files for use in Adobe Illustrator or VectorCraft (or similar programs). The svg and png subfolders also
contain exported versions of these files for those who use other programs to make Super Benji content.

### Exporting AI files to SVG and PNG

Run `python export_ai_to_svg.py` from any directory to recursively export every `.ai` file in `src` to both `svg` and `png`,
preserving the folder structure. The script uses the VectorCraft CLI's `convert` command and looks for it on `PATH` or in the standard
`OneDrive\Documents\ArtCraft\vectorcraft` install folder.

If the CLI is not on `PATH`, provide its executable path:

```powershell
python export_ai_to_svg.py --vectorcraft-cli "C:\Users\thema\OneDrive\Documents\ArtCraft\vectorcraft\vectorcraft-cli.exe"
```

You can also set the `VECTORCRAFT_CLI` environment variable or override the folders with `--source`, `--destination` (SVG),
and `--png-destination` (PNG).
