import pandas as pd

class CleanIP:
    def __init__(self, filepath):
        self.filepath = filepath

    def clean_ip(self, ip):
        return ip[::-1].replace('.', '].[', 1)[::-1]

    def process_file(self):
        try:
            df = pd.read_csv(self.filepath)
            if 'IP' not in df.columns:
                raise ValueError("The CSV file is not formatted correctly. Missing 'IP' column.")

            df['Modified_IP'] = df['IP'].apply(self.clean_ip)
            output_path = self.filepath.replace('.csv', '_modified.csv')
            df.to_csv(output_path, index=False)
            print(f"File processed successfully. Output saved to {output_path}")

        except Exception as e:
            print(f"Error: {e}")
