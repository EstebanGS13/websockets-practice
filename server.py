import asyncio
import websockets
import os
import random
from google_images_search import GoogleImagesSearch


DEV_API_KEY = os.environ.get('GCS_DEVELOPER_KEY')
PROJECT_CX = os.environ.get('GCS_CX')
PORT = 65000
NUM_IMG = 10    # Number of images to search


async def handle_client(websocket, path):
    async for message in websocket:
        print(f"> {message}")

        if message and message != "Cliente conectado.":
            _search_params["q"] = message   # Set the message as the query
            gis.search(search_params=_search_params)    # Search for images
            img_url = random.choice(gis.results()).url  # Get the URL of random image on the list

            await websocket.send(img_url)


if __name__ == "__main__":
    # Provide the API key and CX
    gis = GoogleImagesSearch(DEV_API_KEY, PROJECT_CX)

    # Define search params:
    _search_params = {
        'q': None,
        'num': NUM_IMG,
        # 'safe': 'high',
    }

    start_server = websockets.serve(handle_client, "localhost", PORT)
    print("Servidor iniciado.")

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
