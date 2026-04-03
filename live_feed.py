import requests
from google.transit import gtfs_realtime_pb2

def get_feed(api_key=None):
    url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace"
    headers = {"x-api-key": api_key}
    try:
        response = requests.get(url, headers=headers)
        data = response.content 
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
    return feed
