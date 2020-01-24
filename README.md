# Youtube-Scraper

Youtube scraper can be used to get JSON data from Youtube. It has 2 scripts i.e. keyword search and comment and reply extraction. Both the scripts are built on the top of Youtube API.

## Keyword Search

A search result contains information about a YouTube videos that matches the keywords in an API request. The command line script keyword-search-script.py contains the following parameters.

* First Parameter: Private API Key (************)
* Second Parameter: Keywords
* Third Parameter: Number of results needed (Enter a multiple of 50)

If all the results are needed then just enter 'all' in case of third parameter.
Example:

```bash
python keyword-search-script.py ************ "Green Day" all
```

The JSON data gets saved as keyword_search.json in the same directory.

## Comments and Replies

This fetches all the comment and replies associated with particulare Youtube video ID. The command line script get-comments-script.py contains the following parameters.

* First Parameter: Private API Key (************)
* Second Parameter: Video ID

Example:

```bash
python get-comments-script.py ************ i-2zY4BdP1s
```

The JSON data gets saved as comments.json in the same directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
