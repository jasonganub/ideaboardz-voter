import requests
import threading
import logging
import pdb
import json


cards = []
url = "https://ideaboardz.com/points/8264693/votes.json"
board_id = 3036988
ideaz_board_url = "https://ideaboardz.com/retros/Retro%20/{}/points.json".format(board_id)

def make_call(card):
    while True:

        logging.info("Thread %s: starting")
        data = {"vote[point_id]": str(card)}
        response = requests.post(url, data)

        if response.status_code == 201:
            print("done for %s", card)

        logging.info("Thread %s: finishing")


if __name__ == "__main__":
    threads = []

    response = requests.get(ideaz_board_url)
    if response.status_code == 200:
        json = json.loads(response.content)
        for item in json:
            cards.append(item['id'])

    print(cards)

    for card in cards:
        for i in range(5):
            t = threading.Thread(target=make_call, args=(card,))
            threads.append(t)
            t.start()


