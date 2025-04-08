import pandas as pd

def csv_to_md(csv_file, output_md):
    df = pd.read_csv(csv_file)
    df.to_markdown(output_md, index=False)

csv_to_md("Tagged.csv", "table.md")