# CSV Enrichment with YouTube Channel Information and Content Type

This Python script enriches a CSV file with YouTube channel information and identifies the content type based on video links provided in a specified column.

## Requirements

- Python 3.x installed
- Required libraries: `pytube`, `pandas`

You can install the necessary libraries using pip:

```bash
pip install pytube pandas
```

## Usage

1. **Running the Script:**

   - Open your terminal or command prompt.
   - Navigate to the directory containing the script (`getYoutubeInfo.py`) and your CSV file.
   - Run the script using the command:

     ```bash
     python getYoutubeInfo.py "input_csv_file.csv" "column_name"
     ```

     Replace `"input_csv_file.csv"` with the name of your CSV file and `"column_name"` with the column name containing YouTube video links in your CSV file.

2. **Example:**

   ```bash
   python getYoutubeInfo.py "Gate YouTube testing - Sheet1.csv" "Final Link"
   ```

   This command will enrich the specified column in the CSV file named `"Gate YouTube testing - Sheet1.csv"` with YouTube channel information. The enriched data will be saved to a new CSV file named `"Enriched_Gate YouTube testing - Sheet1.csv"` in the same directory.

3. **Notes:**

   - Ensure that the CSV file is in the same directory as the script.
   - The script fetches YouTube channel information based on the video links provided in the specified column.
   - The output file will contain additional columns 'channel_name', 'channel_id', and 'content_type' with the retrieved information.

## Troubleshooting

If you encounter any issues or errors while running the script, feel free to ask for assistance!
