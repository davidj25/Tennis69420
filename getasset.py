import requests
from frameioclient import FrameioClient
import os

#get the name of the file

#file_name = 

def url(file_name):
    client = FrameioClient("fio-u-FHtWy9PLoivouhMtkpTj3LnN9_a-4dsyow-WO6WPEd9uEMMk1ZKPwNMZ4TRnCBfS")

    data = client.assets.upload("6d9aa811-fc85-4d80-a208-1b10716567d0", "test.mp4") #file_name goes here

    asset_id = data['id']

    link = client.review_links.create(
                project_id="6d9aa811-fc85-4d80-a208-1b10716567d0",
                name="review_link"
            )

    client.review_links.update_assets(
                link_id = link['id'],
                asset_ids = [asset_id]
            )

    return link['short_url']
#print(link['short_url'])

