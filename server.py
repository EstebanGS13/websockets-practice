import asyncio
import websockets


PORT = 65000    # A port that's not being used

async def handle_client(websocket, path):
    async for message in websocket:
        print(message)
        if message == "[CLT] Cliente conectado.":
            # await websocket.send("[SRV] Ok.")
            pass
            print("[SRV] Ok.")
        elif message == "perro":
           
            await websocket.send("https://cnnespanol.cnn.com/wp-content/uploads/2020/07/200703104728-labrador-retriever-stock-super-169.jpg?quality=100&strip=info")
            # await websocket.send(f"aca te mando la foto del {message}")

        else:
            # await websocket.send(f"Mensaje recibido: {message}")
            pass


start_server = websockets.serve(handle_client, "localhost", PORT)
print("[SRV] Servidor iniciado.")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()