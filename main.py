from tqdm import tqdm
from test.test import log as log
import LLMHandling as LLM
import data.DataHandling as DH


def main():
  data = DH.load_json("epiphanies.json")
  LLM.init()
  
  permutations = {
    "11100",
    "11010",
    "11001",
    "10110",
    "10101",
    "10011",
    "01110",
    "01101",
    "01011",
    "00111"
  }
  for combatant, cards in data.items():
    for i in tqdm(range(len(data)), f"{combatant}"):
      log(f"Combatant: {combatant}\n")

      for card, epiphanies in cards.items():
        log(f"\tCard: {card}")
        for j in tqdm(range(len(permutations)), leave=False):
          for perm in permutations:
              response = LLM.get_response(DH.sample(perm, epiphanies))
              DH.record(combatant, card, response)        
      log(f"{'=' * 20}")


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    log(f"{'=' * 20}")
    log("Process interrupted by user.")
    input("Process Ended\nPress Enter to exit...")
