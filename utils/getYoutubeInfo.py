import argparse
from pytube import YouTube
import pandas as pd

def get_channel_info(video_url):
    try:
        yt = YouTube(video_url)
        channel_name = yt.author
        channel_id = yt.channel_id
        return channel_name, channel_id
    except Exception as e:
        print(f"An error occurred: {e}", video_url)
        return None, None

def identify_content_type(video_url):
    if 'watch?v=' in video_url:
        return 'Single Video'
    elif 'list=' in video_url:
        return 'Playlist'
    elif 'channel/' in video_url or 'user/' in video_url:
        return 'Channel'
    else:
        return 'Unknown'

def enrich_csv(csv_file, column_name):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Convert DataFrame to dictionary
    dfdict = df.to_dict('records')

    # Iterate through each row in the dictionary
    for i in range(len(dfdict)):
        print(i)
        # Get channel information from the specified column
        channel_name, channel_id = get_channel_info(dfdict[i][column_name])
        
        # Add new columns 'channel_name' and 'channel_id' with the retrieved information
        dfdict[i]['channel_name'] = channel_name
        dfdict[i]['channel_id'] = channel_id

        # Identify content type and add to a new column 'content_type'
        content_type = identify_content_type(dfdict[i][column_name])
        dfdict[i]['content_type'] = content_type

    # Create a new DataFrame from the enriched dictionary and save it as a new CSV file
    enriched_df = pd.DataFrame(dfdict)
    enriched_df.to_csv("Enriched_" + csv_file, index=False)
    print(f"Enriched CSV created: Enriched_{csv_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enrich a CSV file with YouTube channel information and content type")
    parser.add_argument("input_csv", help="Input CSV file name")
    parser.add_argument("column_name", help="Column name containing YouTube video links")
    args = parser.parse_args()

    # Call the enrich_csv function with the provided CSV filename and column name
    enrich_csv(args.input_csv, args.column_name)
