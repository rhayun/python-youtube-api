python-youtube-api
==================

BASED ON php-youtube-api from: https://github.com/madcoda/php-youtube-api

A basic Python wrapper for the Youtube Data API v3 ( Non-OAuth ). Designed to let devs easily 
fetch public data (Video, Channel, Playlists info) from Youtube. No 3rd party dependancy. (except PHPUnit)
The reason of returning the decoded JSON response directly is that you only need to read the Google API doc 
to use this library, instead of learning my set of API again (Keep it simple).

```python
youtube = YoutubeAPI('key': '/* Your API key here */')

// Return a dict 
video = youtube.get_video_info('rie-hPVJ7Sw')

// Search playlists, channels and videos
results = youtube.search('Android')

// Search only Videos
video_list = youtube.search_videos('Android')

// Search only Videos in a given channel
video_list = youtube.search_channel_videos('keyword', 'UCk1SpWNzOs4MYmr0uICEntg', 50)

results = youtube.search_advanced({/* params */ })

channel = youtube.get_channel_by_name('xdadevelopers')

channel = youtube.get_channel_by_id('UCk1SpWNzOs4MYmr0uICEntg')

playlist = youtube.get_playlist_by_id('PL590L5WQmH8fJ54F369BLDSqIwcs-TCfs')

playlists = youtube->get_playlists_by_channel_id('UCk1SpWNzOs4MYmr0uICEntg')

playlist_items = youtube.get_playlist_items_by_playlist_id('PL590L5WQmH8fJ54F369BLDSqIwcs-TCfs')

activities = youtube.get_activities_by_channel_id('UCk1SpWNzOs4MYmr0uICEntg')

video_id = youtube.parse_vid_from_url('https://www.youtube.com/watch?v=moSFlvxnbgk')
// result: moSFlvxnbgk
```

## Basic Search Pagination
```python

youtube = YoutubeAPI('key': '/* Your API key here */')

// Set Default Parameters
params = {
    'q': 'Android',
    'type': 'video',
    'part': 'id, snippet',
    'maxResults': 50
}

// Make Intial Call. With second argument to reveal page info such as page tokens.
search = youtube.search_advanced(params, True)

// check if we have a pageToken
if 'nextPageToken' in search['info']:
    params['pageToken'] = search['info']['nextPageToken']


// Make Another Call and Repeat
search = youtube.search_advanced(params, True)          

// add results key with info parameter set
print search['results'] 

/* Alternative approach with new built in paginateResults function */
 
// Same Params as before
params = {
    'q': 'Android',
    'type': 'video',
    'part': 'id, snippet',
    'maxResults': 50
}

// an array to store page tokens so we can go back and forth
page_tokens = {}

// make inital search
search = youtube.paginate_results(params, None)

// store token
page_tokens.append(search['info']['nextPageToken'])

// go to next page in result
search = youtube.paginate_results(params, page_tokens[0])

// store token
pageTokens.append(search['info']['nextPageToken'])

// go to next page in result
search = youtube.paginate_results(params, page_tokens[1])

// store token
pageTokens.append(search['info']['nextPageToken'])

// go back a page
search = youtube.paginate_results(params, page_tokens[0])

// add results key with info parameter set
print search['results']

```

The pagination above is quite basic. Depending on what you are trying to achieve; you may want to create a recurssive function that traverses the results.

## Youtube Data API v3
- [Youtube Data API v3 Doc](https://developers.google.com/youtube/v3/)
- [Obtain API key from Google API Console](http://code.google.com/apis/console)

## Contact
For bugs, complain and suggestions please [file an Issue here](https://github.com/rhayun/python-youtube-api/issues) 
or send email to ronen.hayun@gmail.com :)
