import tkinter as tk
from tkinter import filedialog  # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# Implement your classes here


class InfoBar(AbstractGrid):
    """The InfoBar should span the entire width of the farm and inventory combined.
    An example of a completed InfoBar in the game is shown in Figure 3."""

    def __init__(self, master):
        """
        Sets up this InfoBar to be an AbstractGrid with the appropriate number of rows and columns,
        and the appropriate width and height (see constants.py).
        """
        super().__init__(
            master, (2, 3), (FARM_WIDTH + INVENTORY_WIDTH, INFO_BAR_HEIGHT)
        )

    def draw_string(self, row, col, text1):
        """
        Helper method to draw the text
        """
        self.create_text(self.get_midpoint((row, col)), text=text1, font=HEADING_FONT)

    def redraw(self, day, money, energy):
        """
        Clears the InfoBar and redraws it to display the provided day, money, and energy.
        """
        self.clear()

        self.draw_string(0, 0, "Day:")
        self.draw_string(1, 0, day)

        self.draw_string(0, 1, "Money:")
        self.draw_string(1, 1, "$" + str(money))

        self.draw_string(0, 2, "Energy:")
        self.draw_string(1, 2, energy)


class FarmView(AbstractGrid):
    """
    The FarmView is a grid displaying the farm map, player, and plants
    """

    def __init__(
        self,
        master: tk.Tk | tk.Frame,
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs
    ) -> None:
        """
        Sets up the FarmView to be an AbstractGrid with the appropriate dimensions and size,
        and creates an instance attribute of an empty dictionary to be used as an image cache.
        """
        super().__init__(master, dimensions, size, **kwargs)
        self.img_dict = {}

        self.tile_size = self.get_cell_size()

    def draw_ground(self, pos: tuple[int, int], tile_id: str):
        """Helper Method for ground drawing"""
        img_str = "images/" + IMAGES[tile_id]
        img = get_image(img_str, self.tile_size, self.img_dict)
        self.create_image(pos, image=img)

    def draw_plants(self, pos: tuple[int, int], plant: "Plant"):
        """Helper Method  for plants drawing"""
        img_str = "images/" + get_plant_image_name(plant)
        img = get_image(img_str, self.tile_size, self.img_dict)
        self.create_image(pos, image=img)

    def draw_player(self, pos: tuple[int, int], player_direction: str):
        """Helper Method for player drawing"""
        img_str = "images/player_" + player_direction + ".png"
        img = get_image(img_str, self.tile_size, self.img_dict)
        self.create_image(pos, image=img)

    def redraw(
        self,
        ground: list[str],
        plants: dict[tuple[int, int], "Plant"],
        player_position: tuple[int, int],
        player_direction: str,
    ) -> None:
        """Clears the farm view, then creates (on the FarmView instance) the images for the ground,
        then the plants, then the player. That is, the player and plants should render in front of the
        ground, and the player should render in front of the plants"""
        self.clear()
        row = 0
        for line in ground:
            for i in range(0, len(line)):
                self.draw_ground(self.get_midpoint((row, i)), line[i])
            row += 1

        for key, values in plants.items():
            self.draw_plants(self.get_midpoint(key), values)

        self.draw_player(self.get_midpoint(player_position), player_direction)


class ItemView(tk.Frame):
    """The ItemView is a frame displaying relevant information and buttons for a single item"""

    def __init__(
        self,
        master: tk.Frame,
        item_name: str,
        amount: int,
        select_command: Optional[Callable[[str], None]] = None,
        sell_command: Optional[Callable[[str], None]] = None,
        buy_command: Optional[Callable[[str], None]] = None,
    ) -> None:
        """Sets up ItemView to operate as a tk.Frame, and creates all internal widgets"""
        super().__init__(master, width=INVENTORY_WIDTH, height=FARM_WIDTH / 6)
        self.pack_propagate(False)
        self.item_name = item_name

        self.item_label = tk.Label(self, text="text")
        self.item_label.pack(side=tk.LEFT)

        # helper method for the further event binding
        def select_func(event):
            select_command(item_name)

        def sell_func():
            sell_command(item_name)

        def buy_func():
            buy_command(item_name)

        if item_name in BUY_PRICES.keys():
            buy_button = tk.Button(self, text="Buy", command=buy_func)
            buy_button.pack(side=tk.LEFT)

        sell_button = tk.Button(self, text="Sell", command=sell_func)
        sell_button.pack(side=tk.LEFT)

        self.item_label.bind("<Button-1>", select_func)
        self.bind("<Button-1>", select_func)

        self.update(amount, False)

    def update(self, amount: int, selected: bool = False) -> None:
        """Updates the text on the label, and the colour of this ItemView appropriately"""

        col = INVENTORY_COLOUR
        if selected:
            col = INVENTORY_SELECTED_COLOUR
        if amount == 0:
            col = INVENTORY_EMPTY_COLOUR

        self.config(bg=col)
        self.item_label.configure(bg=col)

        # Update the text of item_label so that the amount would be updated
        text = self.item_name + ": " + str(amount) + "\n"
        text += "Sell price: ${}\n".format(SELL_PRICES[self.item_name])
        if self.item_name in BUY_PRICES.keys():
            text += "Buy price: ${}\n".format(BUY_PRICES[self.item_name])
        else:
            text += "Buy price: ${}\n".format("N/A")

        self.item_label.configure(text=text)


class FarmGame:
    """FarmGame is the controller class for the overall game. The controller is responsible for creating and
    maintaining instances of the model and view classes, event handling,
    and facilitating communication between the model and view classes"""

    def __init__(self, master: tk.Tk, map_file: str) -> None:
        self.master = master
        self.map_file = map_file
        self.itemViews: list[ItemView] = []
        self.farmModel = FarmModel(map_file)

        print("see the map name: " + map_file)
        for l in self.farmModel.get_map():
            print(l)

        self.master.title("Farm Game")

        self.img_header = get_image(
            "images/header.png", (FARM_WIDTH + INVENTORY_WIDTH, BANNER_HEIGHT)
        )
        label_img = tk.Label(master, image=self.img_header)
        label_img.pack(side=tk.TOP)

        frame_for_upper = tk.Frame(master)
        self.farm = FarmView(
            frame_for_upper, self.farmModel.get_dimensions(), (FARM_WIDTH, FARM_WIDTH)
        )
        self.farm.pack(side=tk.LEFT)

        frame_for_items = tk.Frame(frame_for_upper)
        for i in range(0, 6):
            name = ITEMS[i]
            itemView = ItemView(
                frame_for_items,
                ITEMS[i],
                i,
                self.select_item,
                self.sell_item,
                self.buy_item,
            )
            itemView.pack(side=tk.TOP)
            self.itemViews.append(itemView)
        frame_for_items.pack(side=tk.RIGHT)

        frame_for_upper.pack(side=tk.TOP)

        self.info = InfoBar(master)
        self.info.pack(side=tk.TOP)

        button = tk.Button(master, text="Next day", command=self.new_day)
        # button.bind('<ButtonPress>', self.newday)
        button.pack(side=tk.TOP)

        master.bind("<KeyPress>", self.handle_keypress)

        self.redraw()

    def redraw(self) -> None:
        """Redraws the entire game based on the current model state"""
        self.farm.redraw(
            self.farmModel.get_map(),
            self.farmModel.get_plants(),
            self.farmModel.get_player_position(),
            self.farmModel.get_player_direction(),
        )

        self.info.redraw(
            self.farmModel.get_days_elapsed(),
            self.farmModel.get_player().get_money(),
            self.farmModel.get_player().get_energy(),
        )

        for itemView in self.itemViews:
            name = itemView.item_name
            count = 0
            selected = self.farmModel.get_player().get_selected_item() == name
            if name in self.farmModel.get_player().get_inventory():
                count = self.farmModel.get_player().get_inventory().get(name)

            itemView.update(count, selected)

    def handle_keypress(self, event: tk.Event) -> None:
        """An event handler to be called when a keypress event occurs"""
        print("handle_keypress: " + event.char)
        if event.char in MOVE_DELTAS:
            self.farmModel.move_player(event.char)
            self.redraw()

        if event.char == "p":
            seed_name = self.farmModel.get_player().get_selected_item()
            if (
                seed_name is not None
                and seed_name in SEEDS
                and seed_name in self.farmModel.get_player().get_inventory().keys()
            ):
                plant = None
                if seed_name == SEEDS[0]:
                    plant = PotatoPlant()
                elif seed_name == SEEDS[1]:
                    plant = KalePlant()
                elif seed_name == SEEDS[2]:
                    plant = BerryPlant()
                self.farmModel.add_plant(self.farmModel.get_player_position(), plant)
                self.farmModel.get_player().remove_item((seed_name, 1))
                self.redraw()

        if event.char == "h":
            plant = self.farmModel.harvest_plant(self.farmModel.get_player_position())
            if plant is not None:
                self.farmModel.get_player().add_item(plant)
            self.redraw()

        if event.char == "r":
            self.farmModel.remove_plant(self.farmModel.get_player_position())
            self.redraw()

        if event.char == "t":
            print("handle_keypress: event.char == t")
            self.farmModel.till_soil(self.farmModel.get_player_position())
            self.redraw()

        if event.char == "u":
            self.farmModel.untill_soil(self.farmModel.get_player_position())
            self.redraw()

    def select_item(self, item_name: str) -> None:
        """The callback to be given to each ItemView for item selection"""
        self.farmModel.get_player().select_item(item_name)
        self.redraw()

    def buy_item(self, item_name: str) -> None:
        """The callback to be given to each ItemView for buying items"""
        self.farmModel.get_player().buy(item_name, BUY_PRICES[item_name])
        self.redraw()

    def sell_item(self, item_name: str) -> None:
        """The callback to be given to each ItemView for selling items"""
        self.farmModel.get_player().sell(item_name, SELL_PRICES[item_name])
        self.redraw()

    def new_day(self):
        """The new day callback that handles the new day button function"""
        self.farmModel.new_day()
        self.redraw()


def play_game(root: tk.Tk, map_file: str) -> None:
    farmGame = FarmGame(root, map_file)
    root.mainloop()


def main() -> None:
    play_game(tk.Tk(), "maps/map2.txt")


if __name__ == "__main__":
    main()
