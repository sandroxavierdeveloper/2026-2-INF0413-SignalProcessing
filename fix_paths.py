import json
import glob
import os

notebooks = glob.glob("/home/deck/dev/sentinela/assets-main/labs/**/*.ipynb", recursive=True)

for nb_path in notebooks:
    if ".ipynb_checkpoints" in nb_path:
        continue
    
    with open(nb_path, "r", encoding="utf-8") as f:
        try:
            nb = json.load(f)
        except:
            continue
            
    modified = False
    for cell in nb.get("cells", []):
        if cell["cell_type"] == "code":
            new_source = []
            for line in cell.get("source", []):
                if "sys.path.append('/home/kuntur/Documents" in line or "sys.path.append('.')" in line or "sys.path.append('/content/drive/" in line:
                    new_source.append("sys.path.append('../../')\n")
                    modified = True
                else:
                    new_source.append(line)
            if modified:
                cell["source"] = new_source

    if modified:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print(f"Fixed paths in {os.path.basename(nb_path)}")

