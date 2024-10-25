import tkinter as tk
from tkinter import filedialog  # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# Implement your classes here


class InfoBar(AbstractGrid):
    def __init__(self, master: tk.Tk or tk.Frame) -> None:
        super().__init__(
            master, (2, 3), (FARM_WIDTH + INVENTORY_WIDTH, INFO_BAR_HEIGHT)
        )
        self.annotate_position((0, 0), "Day:", font=HEADING_FONT)
        self.annotate_position((0, 1), "Money:", font=HEADING_FONT)
        self.annotate_position((0, 2), "Energy:", font=HEADING_FONT)
        self.annotate_position((1, 0), "1")
        self.annotate_position((1, 1), "$0")
        self.annotate_position((1, 2), "100")

    def redraw(self, day: int, money: int, energy: int) -> None:
        self.clear()

        self.annotate_position((0, 0), "Day:", font=HEADING_FONT)
        self.annotate_position((0, 1), "Money:", font=HEADING_FONT)
        self.annotate_position((0, 2), "Energy:", font=HEADING_FONT)
        self.annotate_position((1, 0), str(day))
        self.annotate_position((1, 1), "$" + str(money))
        self.annotate_position((1, 2), str(energy))


class FarmView(AbstractGrid):
    def __init__(
        self,
        master: tk.Tk or tk.Frame,
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs,
    ) -> None:
        super().__init__(master, dimensions=dimensions, size=size)
        # create an empty dictionary as cache
        self._image_cache = {}
        for path in IMAGES.values():
            picture_path = "images/" + path
            get_image(picture_path, self.get_cell_size(), self._image_cache)

        """for value in IMAGES:
            path = images/ + value
            get_image(path, self.get_cell_size(), self._a)"""

    def redraw(
        self,
        ground: list[str],
        plants: dict[tuple[int, int], "Plant"],
        player_position: tuple[int, int],
        player_direction: str,
    ) -> None:
        self.clear()
        for horizontal_index, row in enumerate(ground):
            x_coordinate = horizontal_index
            row_element = row
            for vertical_index, column in enumerate(row_element):
                y_coordinate = vertical_index
                final_ground_element = column
                (pixel_x, pixel_y) = self.get_midpoint((x_coordinate, y_coordinate))
                what_picture_here = IMAGES[final_ground_element]
                picture_path = "images/" + what_picture_here
                final_image = get_image(
                    picture_path, self.get_cell_size(), self._image_cache
                )
                self.create_image((pixel_x, pixel_y), image=final_image)

        for key, value in plants.items():
            (pixel_x, pixel_y) = self.get_midpoint(key)
            plants_picture_path = "images/" + get_plant_image_name(value)
            final_plants_image = get_image(
                plants_picture_path, self.get_cell_size(), self._image_cache
            )
            self.create_image((pixel_x, pixel_y), image=final_plants_image)

        # 根據player_direction獲取玩家圖片名稱
        player_image_path = "images/player_" + player_direction + ".png"
        player_picture = get_image(
            player_image_path, self.get_cell_size(), self._image_cache
        )
        (pixel_x, pixel_y) = self.get_midpoint(player_position)
        self.create_image((pixel_x, pixel_y), image=player_picture)


class ItenView(tk.Frame):
    def __init__(
        self,
        master: tk.Frame,
        item_name: str,
        amount: int,
        select_command: Optional[Callable[[str], None]] = None,
        sell_command: Optional[Callable[[str], None]] = None,
        buy_command: Optional[Callable[[str], None]] = None,
    ):
        super().__init__(master)

        self._item_name = item_name
        self._amount = amount  # store the value

        self._text_frame = tk.Frame(self)
        self._text_frame.pack(side=tk.LEFT)

        self._button_frame = tk.Frame(self)
        self._button_frame.pack(
            side=tk.LEFT
        )  # create two child frames for text and button.

        self._item_amount = tk.Label(
            self._text_frame, text=f"{self._item_name}: {self._amount}"
        )
        self._item_amount.pack(side=tk.TOP)
        self._item_sell_price = tk.Label(
            self._text_frame, text=f"Sell price: ${SELL_PRICES[self._item_name]}"
        )
        self._item_sell_price.pack(side=tk.TOP)

        if self._item_name in BUY_PRICES:  # determine an item could be bought or not.
            self._item_buy_price = tk.Label(
                self._text_frame, text=f"Buy price: ${BUY_PRICES[self._item_name]}"
            )
            self._item_buy_price.pack(side=tk.TOP)
            self._buy_button = tk.Button(
                self._button_frame, text="Buy", command=buy_command
            )
            self._buy_button.pack(fill=tk.BOTH, expand=True)
            self._sell_button = tk.Button(
                self._button_frame, text="Sell", command=select_command
            )
            self._sell_button.pack(fill=tk.BOTH, expand=True)
        else:
            self._item_buy_price = tk.Label(self._text_frame, text="Buy price: $N/A")
            self._item_buy_price.pack(side=tk.TOP)
            self._sell_button = tk.Button(
                self._button_frame, text="Sell", command=sell_command
            )
            self._sell_button.pack(side=tk.LEFT)
            # no buy button.

        self.bind("<buy_button>", select_command)
        self.bind("<sell_button>", select_command)

    def update(self, amount: int, selected: bool = False):
        self._item_amount.config(text=f"{self._item_name}: {amount}")
        if selected is True:
            self.configure(bg=INVENTORY_SELECTED_COLOUR)
        elif self._amount > 0:
            self.configure(bg=INVENTORY_COLOUR)
        else:
            self.configure(bg=INVENTORY_EMPTY_COLOUR)  # 可能需要修改


class FarmGame:
    def __init__(self, master: tk.Tk, map_file: str) -> None:
        self._master = master
        self._master.title("Farm Game")

        self._banner_picture = get_image(
            "images/header.png", ((FARM_WIDTH + INVENTORY_WIDTH), BANNER_HEIGHT)
        )

        banner = tk.Label(master, image=self._banner_picture)
        banner.pack(side=tk.TOP)

        self._model = FarmModel(map_file)
        self._player = self._model.get_player()
        self._inventory = self._player.get_inventory()
        dimensions = self._model.get_dimensions()

        frame_for_main_part = tk.Frame(master)
        frame_for_main_part.pack(side=tk.TOP)
        frame_for_farmview = tk.Frame(frame_for_main_part)
        frame_for_farmview.pack(side=tk.LEFT)
        frame_for_itemview = tk.Frame(frame_for_main_part)
        frame_for_itemview.pack(side=tk.RIGHT)

        self._farmview = FarmView(
            frame_for_main_part, dimensions=dimensions, size=(FARM_WIDTH, FARM_WIDTH)
        )
        self._farmview.pack(side=tk.LEFT)

        for item in ITEMS:
            self._itemview = ItenView(
                frame_for_itemview, item, self._inventory.get(item, 0), None, None, None
            )
            self._itemview.pack(side=tk.TOP)  # 有錯的話看a.33 一個一個寫出來

        self._infobar = InfoBar(master)
        self._infobar.pack(side=tk.TOP)

        self._next_day_button = tk.Button(
            master, text="Next day", command=self._model.new_day
        )
        self._next_day_button.pack(side=tk.BOTTOM)

        master.bind("<KeyPress>", self.handle_keypress)  #
        master.bind("<Motion>", self.handle_keypress)
        self.redraw()

    def redraw(self):
        self._infobar.redraw(
            self._model.get_days_elapsed(),
            self._player.get_money(),
            self._player.get_energy(),
        )
        self._farmview.redraw(
            self._model.get_map(),
            self._model.get_plants(),
            self._model.get_player_position(),
            self._model.get_player_direction(),
        )

    def handle_keypress(self, event: tk.Event):
        if event == event.char:  # 判別event是鍵盤輸入
            key = event.char.lower()
            player_position = self._model.get_player_position()
            plant_at_player_position = self._model.get_plants().get(player_position)
            if key == UP or key == DOWN or key == LEFT or key == RIGHT:
                self._model.move_player(key)
            elif key == "p":
                if self._player.get_selected_item() != None:
                    if self._player.get_selected_item() in SEEDS:
                        # 一個if判別式,拿到player_position後去map找,如果對應map的位置是GRASS, return None
                        if self._model.get_plants().get(player_position) != None:
                            return None
                        else:
                            if self._player.get_selected_item() == "Potato Seed":
                                potatoplant = PotatoPlant
                                self._model.add_plant(player_position, potatoplant)
                            elif self._player.get_selected_item() == "Kale Seed":
                                kaleplant = KalePlant
                                self._model.add_plant(player_position, kaleplant)
                            elif self._player.get_selected_item() == "Berry Seed":
                                berryplant = BerryPlant
                                self._model.add_plant(player_position, berryplant)
            elif key == "h":
                if plant_at_player_position == None:
                    return None
                else:
                    if plant_at_player_position.can_harvest() is False:
                        return None
                    else:
                        harvested_plant = plant_at_player_position.harvest()
                        self._player.add_item(harvested_plant)
            elif key == "r":
                self._model.remove_plant(plant_at_player_position)
            elif key == "t":
                pass
                # 一個if判別式,拿到player_position後去map找,如果對應map的位置不是UNTILLED, return None
                # 是的話,self.model.till_soil(plant_at_player_position)
            elif key == "u":
                if plant_at_player_position != None:
                    return None
                else:
                    pass
                    # 一個if判別式,拿到player_position後去map找,如果對應map的位置不是SOIL, return None
                    # 是的話,self._model.untill_soil(player_position)
        elif event.type == 2:
            pixel_x = event.x
            pixel_y = event.y
            # 根據當下位置,判別是屬於哪一個item的itemview, item = potatoitemview, kaleitemview...
            self.select_item(item)
        elif event.type == 4:
            pass
            # 把select_item, buy_item, sell_item法傳到itemview的button裡,button config.

    def select_item(self, item_name):
        if self._player.get_inventory().get(item) > 0:
            self._player.select_item(item)

    def buy_item(self, item_name):
        self._player.buy(item_name)

    def sell_item(self, item_name):
        self._player.sell(item_name)


def play_game(root: tk.Tk, map_file: str) -> None:
    game = FarmGame(root, map_file)
    root.mainloop()


def main() -> None:
    root = tk.Tk()
    map_file = "maps/map1.txt"
    play_game(root, map_file)


if __name__ == "__main__":
    main()
