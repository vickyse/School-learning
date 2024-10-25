import tkinter as tk
from tkinter import filedialog  # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# Implement your classes here


class InfoBar(AbstractGrid):
    """InfoBar would display information to the user about the number of days elapsed
    in the game, as well as the player's energy and money.
    """

    def __init__(self, master: tk.Tk or tk.Frame) -> None:
        """
        Sets up this InfoBar to be an AbstractGrid with the appropriate number of rows
        and columns, and the appropriate width and height.

        Parameters:
        master: inforbar's parent window.
        """
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
        """
        Clears the InfoBar and redraws it to display the provided day, money,
        and energy.

        Parameters:
        day: how many days have elapsed.
        money: amount of money that player currently have.
        energy: amount of energy that player currently have.
        """
        self.clear()

        self.annotate_position((0, 0), "Day:", font=HEADING_FONT)
        self.annotate_position((0, 1), "Money:", font=HEADING_FONT)
        self.annotate_position((0, 2), "Energy:", font=HEADING_FONT)
        self.annotate_position((1, 0), str(day))
        self.annotate_position((1, 1), "$" + str(money))
        self.annotate_position((1, 2), str(energy))


class FarmView(AbstractGrid):
    """
    FarmView is a grid displaying the farm map, player, and plants.
    """

    def __init__(
        self,
        master: tk.Tk or tk.Frame,
        dimensions: tuple[int, int],
        size: tuple[int, int],
        **kwargs,
    ) -> None:
        """
        Sets up the FarmView to be an AbstractGrid with the appropriate dimensions
        and size, and creates an instance attribute of an empty dictionary to be used
        as an image cache.

        Paremeter:
        master: farmview's parent window.
        dimension: amount of rows and columns that farnview have.
        size: farmview's size in parent window.
        """
        super().__init__(master, dimensions=dimensions, size=size, **kwargs)

        self._image_cache = {}
        for path in IMAGES.values():
            picture_path = "images/" + path
            get_image(picture_path, self.get_cell_size(), self._image_cache)
            # put every images into the cache.

    def redraw(
        self,
        ground: list[str],
        plants: dict[tuple[int, int], "Plant"],
        player_position: tuple[int, int],
        player_direction: str,
    ) -> None:
        """
        Clears the farm view, then creates the images for the ground, then the plants,
        then the player.

        Parameters: same as __init__.
        """
        self.clear()

        for horizontal_index, row in enumerate(ground):
            x_coordinate = horizontal_index
            row_element = row
            for vertical_index, column in enumerate(row_element):
                y_coordinate = vertical_index
                final_ground_element = column
                # "column" is the precise position of every element in "ground", namely,
                # map file.
                what_picture_here = IMAGES[final_ground_element]
                # get the image of this position.
                (pixel_x, pixel_y) = self.get_midpoint((x_coordinate, y_coordinate))
                picture_path = "images/" + what_picture_here
                final_image = get_image(
                    picture_path, self.get_cell_size(), self._image_cache
                )
                self.create_image(
                    (pixel_x, pixel_y), image=final_image
                )  # draw the ground

        for position, plant in plants.items():
            (pixel_x, pixel_y) = self.get_midpoint(position)
            plants_picture_path = "images/" + get_plant_image_name(plant)
            final_plants_image = get_image(
                plants_picture_path, self.get_cell_size(), self._image_cache
            )
            self.create_image(
                (pixel_x, pixel_y), image=final_plants_image
            )  # draw the plants

        player_image_path = "images/player_" + player_direction + ".png"
        # get player image according to his direction.
        player_picture = get_image(
            player_image_path, self.get_cell_size(), self._image_cache
        )
        (pixel_x, pixel_y) = self.get_midpoint(player_position)
        self.create_image((pixel_x, pixel_y), image=player_picture)


class ItemView(tk.Frame):
    def __init__(
        self,
        master: tk.Frame,
        item_name: str,
        amount: int,
        select_command: Optional[Callable[[str], None]] = None,
        sell_command: Optional[Callable[[str], None]] = None,
        buy_command: Optional[Callable[[str], None]] = None,
    ):
        """
        ItemView is a frame displaying relevant information and buttons for a single item.

        Parameters:
        master: itemview's parent frame.
        amount: amount of the inventory.
        select_command: item name that player prompt to select.
        sell_command: item name that player prompt to buy.
        buy_command: item name that player prompt to sell.
        """
        super().__init__(master)

        self._item_name = item_name
        self._amount = amount  # store the value
        self._itemview_element: list[
            tk.Frame or tk.Button
        ] = []  # for following iterative code.

        def select_method(event):
            select_command(item_name)

        def sell_method():
            sell_command(item_name)

        def buy_method():
            buy_command(item_name)

        # The methods above will let selecet_command, sell_command,
        # buy_command to take the item name, for the futther code.

        if self._amount > 0:
            self._text_frame = tk.Frame(self, bg=INVENTORY_COLOUR)
            self._button_frame = tk.Frame(self, bg=INVENTORY_COLOUR)
            self._text_frame.pack(side=tk.LEFT)
            self._button_frame.pack(side=tk.LEFT)
            self._itemview_element.append(self._text_frame)
            # after creating the conponent, add it into the list for "update" method.
            self._itemview_element.append(self._button_frame)
        else:
            self._text_frame = tk.Frame(self, bg=INVENTORY_EMPTY_COLOUR)
            self._button_frame = tk.Frame(self, bg=INVENTORY_EMPTY_COLOUR)
            self._text_frame.pack(side=tk.LEFT)
            self._button_frame.pack(side=tk.LEFT)
            self._itemview_element.append(self._text_frame)
            self._itemview_element.append(self._button_frame)
        # create two child frames for text and button, and also set the initial colour.

        self._item_amount = tk.Label(
            self._text_frame,
            text=f"{self._item_name}: {str(self._amount)}",
        )
        self._item_sell_price = tk.Label(
            self._text_frame,
            text=f"Sell price: ${SELL_PRICES[self._item_name]}",
        )
        self._item_amount.pack(side=tk.TOP)
        self._item_sell_price.pack(side=tk.TOP)
        self._itemview_element.append(self._item_amount)
        self._itemview_element.append(self._item_sell_price)

        if self._item_name in BUY_PRICES:  # determine an item could be bought or not.
            self._item_buy_price = tk.Label(
                self._text_frame,
                text=f"Buy price: ${BUY_PRICES[self._item_name]}",
            )
            self._buy_button = tk.Button(
                self._button_frame, text="Buy", command=buy_method
            )
            self._sell_button = tk.Button(
                self._button_frame, text="Sell", command=sell_method
            )
            self._item_buy_price.pack(side=tk.TOP)
            self._buy_button.pack(side=tk.LEFT)
            self._sell_button.pack(side=tk.LEFT)
            self._itemview_element.append(self._item_buy_price)
        else:
            self._item_buy_price = tk.Label(self._text_frame, text="Buy price: $N/A")
            self._sell_button = tk.Button(
                self._button_frame, text="Sell", command=sell_method
            )
            self._item_buy_price.pack(side=tk.TOP)
            self._sell_button.pack(side=tk.LEFT)
            self._itemview_element.append(self._item_buy_price)
            # no buy button.

        self.bind("<Button-1>", select_method)
        for element in self._itemview_element:
            element.bind(
                "<Button-1>", select_method
            )  # bind all the conponent in itemview that can select an item.

        self.update(amount, False)  # first draw of the itemview here.

    def update(self, amount: int, selected: bool = False):
        """
        Update the itemview after a single operation is commanded by player in game.

        Parameter:
        amount: item amount of the inventory now.
        selected: if this itemview is selected or not.
        """
        self._item_amount.configure(text=f"{self._item_name}: {str(amount)}")

        if amount > 0:
            if selected == True:
                self.configure(bg=INVENTORY_SELECTED_COLOUR)
                for element in self._itemview_element:
                    element.configure(bg=INVENTORY_SELECTED_COLOUR)
            else:
                self.configure(bg=INVENTORY_COLOUR, pady=8)
                for element in self._itemview_element:
                    element.configure(bg=INVENTORY_COLOUR)
        else:
            self.configure(bg=INVENTORY_EMPTY_COLOUR, pady=8)
            for element in self._itemview_element:
                element.configure(bg=INVENTORY_EMPTY_COLOUR)
        # determine what colour should is this itemview.


class FarmGame:
    def __init__(self, master: tk.Tk, map_file: str) -> None:
        """
        FarmGame is the controller class for the overall game. The controller is
        responsible for creating and maintaining instances of the model and view classes,
        event handling, and facilitating communi- cation between the model and view classes.

        Parameter:
        master: the game window.
        map_file: map player want to play.
        """
        self.set_up(master, map_file)

    def set_up(self, master: tk.Tk, map_file: str):
        """
        Create every conponent of the game(include menu) and bind every command that would
        be used on in.

        Parameter:
        master: the game window.
        map_file: map player want to play.
        """
        self._master = master

        self._master.title("Farm Game")  # title

        self._banner_picture = get_image(
            "images/header.png", ((FARM_WIDTH + INVENTORY_WIDTH), BANNER_HEIGHT)
        )
        self._banner = tk.Label(master, image=self._banner_picture)
        self._banner.pack(side=tk.TOP)  # banner

        self._model = FarmModel(map_file)
        self._player = self._model.get_player()
        self._inventory = self._player.get_inventory()
        # set model and get "inventory" and "player", which will be used in following code.

        frame_for_main_part = tk.Frame(master)
        frame_for_main_part.pack()
        # create child frame in game window to contain farmview and itemview.

        dimensions = self._model.get_dimensions()
        frame_for_farmview = tk.Frame(frame_for_main_part)
        frame_for_farmview.pack(side=tk.LEFT)
        self._farmview = FarmView(
            frame_for_main_part, dimensions=dimensions, size=(FARM_WIDTH, FARM_WIDTH)
        )
        self._farmview.pack(side=tk.LEFT)  # create a child frame for farmview and put
        # faemview into it.

        frame_for_itemview = tk.Frame(frame_for_main_part)
        frame_for_itemview.pack(side=tk.RIGHT)
        self._itemview_list: list[ItemView] = []
        for item in ITEMS:
            itemview = ItemView(
                frame_for_itemview,
                item,
                self._inventory.get(item, 0),
                self.select_item,
                self.sell_item,
                self.buy_item,
            )
            itemview.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self._itemview_list.append(
                itemview
            )  # create a child frame for itemview and put itemview into it.

        self._infobar = InfoBar(master)
        self._infobar.pack(side=tk.TOP)
        # create a child frame for infobar and put infobar into it.

        self._next_day_button = tk.Button(master, text="Next day", command=self.new_day)
        self._next_day_button.pack(side=tk.BOTTOM)

        master.bind("<KeyPress>", self.handle_keypress)

        self._main_menu = tk.Menu(self._master)
        self._master.config(menu=self._main_menu)
        file_menu = tk.Menu(self._main_menu)
        self._main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Quit", command=self.quit)
        file_menu.add_command(label="Map selection", command=self.new_game)
        # create menu and its functionality here.

        self.redraw()  # draw first view itemview, farmview, and infobar.

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
        for item in self._itemview_list:
            name = item._item_name
            item_amount = 0
            if self._player.get_selected_item() == name:
                item_selected = True
            else:
                item_selected = False
            if name in self._player.get_inventory():
                item_amount = self._player.get_inventory().get(
                    name
                )  # get the inventory amount, if amount of it >0.
            item.update(item_amount, item_selected)

    def handle_keypress(self, event: tk.Event):
        """
        Deal every keypress from player.
        """

        player_position = self._model.get_player_position()
        plants = self._model.get_plants()

        if event.char in MOVE_DELTAS:
            self._model.move_player(event.char)
            self.redraw()
        elif event.char == "p":
            if self._player.get_selected_item() != None:
                if self._player.get_selected_item() in SEEDS:
                    (position_x, position_y) = player_position
                    if self._model.get_map()[position_x][position_y] == GRASS:
                        return None  # if player stand on grass, cannot plant a plant.
                    else:
                        if plants.get(player_position) != None:
                            return None  # means there is already a plant here.
                        else:
                            if self._player.get_selected_item() == SEEDS[0]:
                                if SEEDS[0] in self._player.get_inventory().keys():
                                    # check that player have seed to plant.
                                    plant_to_plant = PotatoPlant()
                                    self._model.add_plant(
                                        player_position, plant_to_plant
                                    )
                                    self._player.remove_item((SEEDS[0], 1))
                            elif self._player.get_selected_item() == SEEDS[1]:
                                if SEEDS[1] in self._player.get_inventory().keys():
                                    plant_to_plant = KalePlant()
                                    self._model.add_plant(
                                        player_position, plant_to_plant
                                    )
                                    self._player.remove_item((SEEDS[1], 1))
                            elif self._player.get_selected_item() == SEEDS[2]:
                                if SEEDS[2] in self._player.get_inventory().keys():
                                    plant_to_plant = BerryPlant()
                                    self._model.add_plant(
                                        player_position, plant_to_plant
                                    )
                                    self._player.remove_item((SEEDS[2], 1))
                            self.redraw()
        elif event.char == "h":
            if plants.get(player_position) == None:
                return None  # means no plant here.
            else:
                plant_to_harvest = plants.get(player_position)
                if plant_to_harvest.can_harvest() == False:
                    return None
                else:
                    harvested_item = plant_to_harvest.harvest()
                    self._player.add_item(harvested_item)
                    self._model.harvest_plant(player_position)
                    self.redraw()
        elif event.char == "r":
            self._model.remove_plant(player_position)
            self.redraw()
        elif event.char == "t":
            self._model.till_soil(player_position)
            self.redraw()
        elif event.char == "u":
            self._model.untill_soil(player_position)
            self.redraw()

    def new_day(self):
        """
        method bind on "Next day" button, to set a new day.
        """
        self._model.new_day()
        self.redraw()

    def select_item(self, item_name):
        """
        select the item.
        """
        self._player.select_item(item_name)
        self.redraw()

    def buy_item(self, item_name):
        """
        buy the item.
        """
        self._player.buy(item_name, BUY_PRICES[item_name])
        self.redraw()

    def sell_item(self, item_name):
        """
        sell the item.
        """
        self._player.sell(item_name, SELL_PRICES[item_name])
        self.redraw()

    def quit(self):
        """
        destory the window.
        """
        self._master.destroy()

    def delete(self):
        for widgets in self._master.winfo_children():
            widgets.destroy()

    def new_game(self):
        """
        ask player to choose the map, and start a new game.
        """
        map_file = filedialog.askopenfilename()
        self.delete()
        FarmGame(self._master, map_file)


def play_game(root: tk.Tk, map_file: str) -> None:
    game = FarmGame(root, map_file)
    game._master.mainloop()


def main() -> None:
    root = tk.Tk()
    map_file = "maps/map1.txt"
    play_game(root, map_file)


if __name__ == "__main__":
    main()
