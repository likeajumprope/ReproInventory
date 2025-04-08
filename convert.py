import pandas as pd

def csv_to_md(csv_file, output_md):
    df = pd.read_csv(csv_file)
    df = df.iloc[:, 2:]
    # Wrap entries in the second column (index 1) with backticks
    second_col = df.columns[2]
    df.loc[1:, second_col] = df.loc[1:, second_col].apply(lambda x: f"`{x}`")

  # Modify the column headers to include HTML styling
    df.columns = [f'<span style="color:blue">{col}</span>' for col in df.columns]
    # Save to markdown
    with open(output_md, "w") as f:
       
        f.write(df.to_markdown(index=False))
        
csv_to_md("Tagged.csv", "output.md")