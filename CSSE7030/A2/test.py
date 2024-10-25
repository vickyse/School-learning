from a2_support import *

# Implement your classes here


class Card:
    """Cards are used by player in an encounter to attack monsters, defend themselves,
    or apply status modifires to themselves or monsters. Cards would only be used to
    provide the superclass to the subclasses in the following subclasses and the
    information that a card should have.
    """

    def get_damage_amount(self) -> int:
        """return the damage amount of the card."""
        return 0

    def get_block(self) -> int:
        """return block offer by the card."""
        return 0

    def get_energy_cost(self) -> int:
        """return the energy cost of the card."""
        return 1

    def get_status_modifiers(self) -> dict[str, int]:
        """return the dictionary, which display the changing status and its changing
        amount."""
        return {}

    def get_name(self) -> str:
        """get card's name."""
        return f"{self.__class__.__name__}"

    def get_description(self) -> str:
        """get card's description."""
        return "A card."

    def requires_target(self) -> bool:
        """Show that a card needs a target or not.
        Returns: True means this card need a target. And false otherwise.
        """
        return True

    def __str__(self) -> str:
        """This method would return the representation of the card
        Returns: str: its format would be: "{Card name}: {Card description}"
        """
        return f"{self.__class__.__name__}: {self.get_description()}"

    def __repr__(self) -> str:
        """This method would return class itself, in order to create a new identical
        class or instance.
        Returns:
            str: format: f"{self.__class__.__name__}()"
        """
        return f"{self.__class__.__name__}()"


class Strike(Card):
    """Strike() is an instance of Card and costs 1 energy to deal 6 damage."""

    def __init__(self) -> None:
        """inherit from Card."""
        super().__init__()  # inherit from Card().

    def get_damage_amount(self) -> int:
        """overwrite the damage amount"""
        return 6  # overwrite the return of get_damage_amount of is superclass.

    def get_description(self) -> str:
        return "Deal 6 damage."

    # overwrite the return of get_description of is superclass.


class Defend(Card):
    """Defend() is an instance of Card, it costs 1 energy to gain 5 block"""

    def __init__(self) -> None:
        """inherit from Card."""
        super().__init__()

    def get_block(self) -> int:
        """overwrite block offering as 5."""
        return 5

    def get_description(self) -> str:
        """return its description."""
        return "Gain 5 block."

    def requires_target(self) -> bool:
        """overwrite the target requiring."""
        return False

    # overwrite the require_target of its superclass because Defend() does not need
    # a target.


class Bash(Card):
    """Bash() is an instance of Card, it costs 1 energy to gain 5 block"""

    def __init__(self) -> None:
        """inherit from Card."""
        super().__init__()

    def get_damage_amount(self) -> int:
        """return 7 damage, which means bash would deal 7 damage to the
        target."""
        return 7

    def get_block(self) -> int:
        """return 5 block, which means bash would offer 5 block to
        player."""
        return 5

    def get_energy_cost(self) -> int:
        """return 2, which means bash would cost 2 energy."""
        return 2

    # overwrite from Card because its cost 2 energy to apply instead of 1.

    def get_description(self) -> str:
        return "Deal 7 damage. Gain 5 block."


class Neutralize(Card):
    """Neutralize() is an instance of Card, it costs no energy to deal 3 damage
    and apply 1 weak and 2 vulnerable to  its target."""

    def __init__(self) -> None:
        """inherit from Card."""
        super().__init__()

    def get_damage_amount(self) -> int:
        """overwrite the amount of damage deal."""
        return 3

    def get_energy_cost(self) -> int:
        """overwrite the energy cost from superclass."""
        return 0

    def get_status_modifiers(self) -> dict[str, int]:
        """overwrite the status change from superclass."""
        return {"weak": 1, "vulnerable": 2}

    # overwrite from Card because it change status to its target.

    def get_description(self) -> str:
        return "Deal 3 damage. Apply 1 weak. Apply 2 vulnerable."


class Survivor(Card):
    """Survivor() is an instance of Card, it costs 1 energy to gain 8 block and
    1 strength."""

    def __init__(self) -> None:
        """inherit from Card."""
        super().__init__()

    def get_block(self) -> int:
        """overwrite block offering from superclass."""
        return 8

    def get_status_modifiers(self) -> dict[str, int]:
        """overwrite status changing to it target from superclass."""
        return {"strength": 1}

    def requires_target(self) -> bool:
        """overwrite target requiring from superclass."""
        return False

    def get_description(self) -> str:
        """overwrite its description from superclass."""
        return "Gain 8 block and 1 strength."


class Eruption(Card):
    """Eruption() is an instance of Card, it costs 1 energy to gain 5 block"""

    def __init__(self) -> None:
        """inherit from superclass."""
        super().__init__()

    def get_damage_amount(self) -> int:
        """overwrite damage dealing from superclass."""
        return 9

    def get_energy_cost(self) -> int:
        """overwrite energy cost from superclass."""
        return 2


class Vigilance(Card):
    """Vigilance() is an instance of Card, it costs 2 energy to gain 8 block and
    1 strength."""

    def __init__(self) -> None:
        """inherit from superclass."""
        super().__init__()

    def get_block(self) -> int:
        """overwrite block offering from superclass"""
        return 8

    def get_status_modifiers(self) -> dict[str, int]:
        """overwrite status changing to target from superclass."""
        return {"strength": 1}

    def get_energy_cost(self) -> int:
        """overwrite energy cost from superclass."""
        return 2

    def requires_target(self) -> bool:
        """overwrite target requiring from superclass."""
        return False


class Entity:
    """This is a superclass for all others eneity would inherit."""

    def __init__(self, max_hp: int) -> None:
        """set the important attribute that would be use in following program.
        Parameter = max_hp: entity's max hp.
        """
        self._max_hp = max_hp
        self._hp = self._max_hp
        self._block = 0
        self._strength = 0
        self._weak = 0
        self._vulnerable = 0

    def get_max_hp(self) -> int:
        """return eneuty's max hp."""
        return self._max_hp

    def get_name(self) -> str:
        """return entity's name."""
        return f"{self.__class__.__name__}"

    def reduce_hp(self, damage_amount: int) -> None:
        """Deal damage and reduce hp to other entity. If the target has any block,
        block would be deduct first until block is 0.
        Parameter: damage_amount
        """
        if self._block > 0:
            self._hp = (self._block + self._hp) - damage_amount
            self._block = 0
        elif self._block == 0:  # if entity has no block.
            self._hp = self._hp - damage_amount
        if self._hp < 0:
            self._hp = 0  # if this entity has negative hp, reset it to 0, which
            # means its is defeated.

    def get_hp(self) -> int:
        """return the current of this eneity"""
        return self._hp

    def add_block(self, adding_block_amount: int) -> None:
        """Adds the given amount to block amount to this entuty.
        Parameter: adding_block_amount"""
        self._block = self._block + adding_block_amount

    def get_block(self) -> int:
        """return the block amount of this entity."""
        return self._block

    def add_strength(self, adding_strength_amount: int) -> None:
        """Adds the given amount to strength amount to this entuty.
        Parameter = adding_strength_amount"""
        self._strength = self._strength + adding_strength_amount

    def get_strength(self) -> int:
        """return the strength amount of this entity."""
        return self._strength

    def add_weak(self, adding_weak_amount: int) -> None:
        """Adds the given amount to weak amount to this entuty.
        Parameter: adding_weak_amount"""
        self._weak = self._weak + adding_weak_amount

    def get_weak(self) -> int:
        """return the weak amount of this entity."""
        return self._weak

    def add_vulnerable(self, adding_vulnerable_amount: int) -> None:
        """Adds the given amount to vulnerable amount to this entuty.
        Parameter: adding_vulnerable_amount
        """
        self._vulnerable = self._vulnerable + adding_vulnerable_amount

    def get_vulnerable(self) -> int:
        """return the wulnerable amount of this entity."""
        return self._vulnerable

    def is_defeated(self) -> bool:
        """detect that the entity is defeated(hp = 0) or not.
        Returns: True if entity is defeated, false otherwise.
        """
        if self._hp == 0:
            return True
        else:
            return False

    def new_turn(self) -> None:
        """applies status changes when a new turn begins. The entity's block would
        be reset to 0, and status weak, vulnerable would decline 1 when a new
        turn start.
        """
        self._block = 0
        if self._weak > 0:
            self._weak = self._weak - 1
        if self._vulnerable > 0:
            self._vulnerable = self._vulnerable - 1

    def __str__(self) -> str:
        """This method would return the representation of the card,
        Returns:format: "{entity name}: {current HP}/{max HP}"
        """
        return f"{self.__class__.__name__}: {self._hp}/{self._max_hp} HP"

    def __repr__(self) -> str:
        """This method would return class itself, in order to create a new identical
        class or instance.
        Returns:format f"{self.__class__.__name__}({self._max_hp})"
        """
        return f"{self.__class__.__name__}({self._max_hp})"


class Player(Entity):
    """A Player is controled by user. Despite regular entity functionality, a player
    also has energy and cards. Player's have three sets of card: the deck (cards
    ready to be drawn), hand(playable cards currently), and discard pile (cards
    that have been played already).
    """

    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """inherit from entity, and also define some attributes that would be used
        in following methods."""
        super().__init__(max_hp)
        self._hand = []
        self._discarded = []  # list[Card] is written for type hints in
        # following program.
        self._deck = cards  # The card ready to be drawn is placed in deck at first.
        self._energy = 3  # Plater initialy has 3 energy.

    def get_energy(self) -> int:
        """Obtain the energy player has currently."""
        return self._energy

    def get_hand(self) -> list[Card]:
        """Display the player's hand currently."""
        return self._hand

    def get_deck(self) -> list[Card]:
        """Display the player's deck currently."""
        return self._deck

    def get_discarded(self) -> list[Card]:
        """Display the player's discards pile currently."""
        return self._discarded

    def start_new_encounter(self) -> None:
        """start_new_ecounter places all cards in discard pile to their deck, and
        remove all cards in discard pile. The condition of this method is player's
        hand must be empty.
        """
        if self._hand == []:
            for card in self._discarded:
                self._deck.append(card)  # put the cards in discard pile to deck.
            self._discarded = []

    def end_turn(self) -> None:
        """end_turn add the remaining card in hand to discard pile, and sets it to
        an empty list.
        """
        for remaining_handcard_while_end_turn in self._hand:
            self._discarded.append(remaining_handcard_while_end_turn)
        self._hand = []

    def new_turn(self) -> None:
        """reset player's energy to 3, and drawn 5 cards from deck to their hand."""
        self._block = 0
        if self._weak > 0:
            self._weak = self._weak - 1
        if self._vulnerable > 0:
            self._vulnerable = self._vulnerable - 1
        draw_cards(self._deck, self._hand, self._discarded)
        self._energy = 3

    def play_card(self, card_name: str) -> Card | None:
        """Attempt to play a card from player's hand.
        Parameter: card_name (str): card name user wish to play.
        Returns:Card | None: return Card if it is possible to play. None if
        card player wishes to play is not in hand, or has insufficient energy.
        """
        for card in self._hand:
            if card.__class__.__name__ == card_name:
                if self._energy >= card.get_energy_cost():
                    self._energy = self._energy - card.get_energy_cost()
                    self._hand.remove(card)
                    self._discarded.append(card)
                    return card

    def __str__(self) -> str:
        """return name. hp and max_hp itself format:
        player_name: self_hp/self_max_hp."""
        return f"{self.__class__.__name__}: {self._hp}/{self._max_hp} HP"

    def __repr__(self) -> str:
        """return itself, use for define it again."""
        return f"{self.__class__.__name__}({self._max_hp}, {self._deck})"


class IronClad(Player):
    """This is a player instance that user can choose in game."""

    def __init__(self) -> None:
        """Instance inherit from Player"""
        super().__init__(
            max_hp=80,
            cards=[
                Strike(),
                Strike(),
                Strike(),
                Strike(),
                Strike(),
                Defend(),
                Defend(),
                Defend(),
                Defend(),
                Bash(),
            ],
        )

    def __repr__(self) -> str:
        """return itself, use for define it again."""
        return f"{self.__class__.__name__}()"


class Silent(Player):
    """This is a player instance that user can choose in game."""

    def __init__(self) -> None:
        """Instance inherit from Player"""
        super().__init__(
            max_hp=70,
            cards=[
                Strike(),
                Strike(),
                Strike(),
                Strike(),
                Strike(),
                Defend(),
                Defend(),
                Defend(),
                Defend(),
                Defend(),
                Neutralize(),
                Survivor(),
            ],
        )

    def __repr__(self) -> str:
        """return itself, use for define it again."""
        return f"{self.__class__.__name__}()"


class Watcher(Player):
    """This is a player instance that user can choose in game."""

    def __init__(self) -> None:
        """Instance inherit from Player"""
        super().__init__(
            max_hp=72,
            cards=[
                Strike(),
                Strike(),
                Strike(),
                Strike(),
                Defend(),
                Defend(),
                Defend(),
                Defend(),
                Eruption(),
                Vigilance(),
            ],
        )

    def __repr__(self) -> str:
        """return itself, use for define it again."""
        return f"{self.__class__.__name__}()"


class Monster(Entity):
    """Monster is a super class for Louse, Cultist, and JawWorm."""

    counter = 0

    def __init__(self, max_hp: int) -> None:
        """Inherit from Entity
        Parameter: max_hp (int): Max hp of Monster
        """
        super().__init__(max_hp)
        self._monster_id = Monster.counter
        Monster.counter = Monster.counter + 1

    def get_id(self) -> int:
        """get the monster's id."""
        return self._monster_id

    def action(self) -> dict[str, int]:
        """Performs the current action for this monster.
        Raises:NotImplementedError: Monster is superclass of Louse, Cultist, JawWorm
        Returns:dict[str, int]: _description_
        """
        raise NotImplementedError


class Louse(Monster):
    """Louse is a monster instance that player would encounter."""

    def __init__(self, max_hp: int) -> None:
        """Instance inherit from Monster.
        Parameter: max_hp: nax hp of Louse.
        """
        super().__init__(max_hp)
        self._damage_amount = random_louse_amount()

    def action(self) -> dict[str, int]:
        """Louse will randomly deal 5 to 7 damage to player.
        Returns: dict[str, int]: format {"damage", damage amount}
        """
        return {"damage": self._damage_amount}


class Cultist(Monster):
    """Cultist is a monster instance that player would encounter."""

    def __init__(self, max_hp: int) -> None:
        """Instance inherit from Monster.
        Parameter: max_hp: nax hp of Cultist.
        """
        super().__init__(max_hp)
        self._damage_amount = 6
        self._weak_amount = 0
        self._count = -1

    def action(self) -> dict[str, int]:
        """Cultist will deal no damage and apply no weak to player at first action.
        After that, each action will deal 6 + action time and alternately apply 0
        and 1 weak to player.
        Returns: dict[str, int]: format: {"damage": damage amount, "weak": weak
        amount}
        """
        if self._count == -1:  # first action() of Cultist.
            self._count = self._count + 1
            return {"damage": 0, "weak": 0}
        else:
            if self._count % 2 == 0:
                self._count = self._count + 1
                return {"damage": 6 + self._count, "weak": 1}
            else:
                self._count = self._count + 1
                return {"damage": 6 + self._count, "weak": 0}


class JawWorm(Monster):
    """JawWorm is a monster instance that player would encounter."""

    def __init__(self, max_hp: int) -> None:
        """Instance inherit from Monster.
        Parameter: max_hp: nax hp of JawWorm.
        """
        super().__init__(max_hp)
        self._damage_taken_sofar = 0

    def reduce_hp(self, damage_amount: int) -> None:
        """Half of the amount of damage the JawWorm has taken so dar(rounding up)
        would transfer to its block.
        Parameter: damage_amount: import every damage JawWorm has taken.
        """
        if self._block > 0:
            self._hp = (self._block + self._hp) - damage_amount
            self._block = 0
        elif self._block == 0:
            self._hp = self._hp - damage_amount  # until here is ruglar method
            # reduce_hp
        self._damage_taken = 0
        self._damage_taken = damage_amount
        self._damage_taken_sofar = self._damage_taken_sofar + damage_amount
        # cumulate damage taken.
        self.add_block(-(-self._damage_taken // 2))
        # Gain corresponded block after every damage takes.

    def action(self) -> dict[str, int]:
        """
        Half of the amount of damage the jaw worm has taken so far (rounding down)
        would be its damage.
        Returns: dict[str, int]: format : {"damage": damage amount}
        """
        return {"damage": (self._damage_taken_sofar // 2)}


class Encounter:
    """Encounter would handle all situation of interaction between player and
    monster."""

    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """This class manages one player and a set of 1 to 3 monsters, and
        facilitates the interactions between the player and monsters.
        Parameters: player (Player): Player() in this encounter
        monsters (list[tuple[str, int]]): player would face 1 to 3 monster(s).
        """
        self._player = player
        self._monster_list = []
        self._player_turn = False
        for monster in monsters:
            if monster[0] == "Louse":  # detect the name (type) of monster.
                monster_louse = Louse(monster[1])  # gain its max_hp.
                self._monster_list.append(monster_louse)  # creat the monster.
            elif monster[0] == "Cultist":
                monster_cultist = Cultist(monster[1])
                self._monster_list.append(monster_cultist)
            elif monster[0] == "JawWorm":
                monster_jawworm = JawWorm(monster[1])
                self._monster_list.append(monster_jawworm)  # code until here is to
                # add every monster into monster list to deal with the following
                # interaction.
        self._player.start_new_encounter()
        self.start_new_turn()

    def start_new_turn(self) -> None:
        """this method ste it to be player's turn, and call player.new_turn() to
        apply the new turn's change(reset block to 0, decline 1 weak and vulnerable
        value.)
        """
        self._player_turn = True
        self._player.new_turn()

    def end_player_turn(self) -> None:
        """This method would end player's trun, put remaining hand card to discard
        pile, then put cards in discard pile back to deck, and start monsters' turn.
        """
        self._player_turn = False
        self._player.end_turn()
        for monster in self._monster_list:
            monster.new_turn()  # respectively start monster's turn.

    def get_player(self) -> Player:
        """get player instance itself."""
        return self._player

    def get_monsters(self) -> list[Monster]:
        """this method is to get monster(s) in this encounter.
        Returns: list[Monster]: the monster(s) would be displayed orderly here.
        """
        return self._monster_list

    def is_active(self) -> bool:
        """check if at least a monster is not dead.
        Returns: True means it does, otherwise, false.
        """
        if len(self._monster_list) >= 1:
            return True
        else:
            return False

    def player_apply_card(self, card_name=str, target_id: int | None = None) -> bool:
        """This method attempt to deploy the first card with given name in player's
        card.
        Parameter:
            card_name: card player want to apply.
            target_id: give player's target.
        Returns: Ture means card is successfully applied, otherwise, false.
        """
        if self._player_turn == False:
            return False  # Check if it is player's turn or not.
        for cards in self._player.get_hand():
            if card_name == cards.get_name():
                if (
                    cards.requires_target() == True
                ):  # choose those cards which requires a target.
                    if target_id == None:
                        return False
                    list_for_monster_id = []
                    for monster in self._monster_list:
                        list_for_monster_id.append(
                            monster.get_id()
                        )  # obtain all monsters' id in this encounter
                    if target_id not in list_for_monster_id:
                        return False
        play_card_result = self._player.play_card(
            card_name
        )  # check if it is possible for player to play the card he want.
        if play_card_result == None:
            return False
        elif play_card_result.get_name() == "Strike":
            for monster in self._monster_list:
                if monster.get_id() == target_id:
                    if self._player.get_strength() > 0:
                        if monster.get_vulnerable() > 0:
                            if self._player.get_weak() > 0:
                                monster.reduce_hp(
                                    int(6 + self._player.get_strength()) * 1.5 * 0.75
                                )
                            else:
                                monster.reduce_hp(
                                    int(6 + self._player.get_strength()) * 1.5
                                )
                        else:
                            monster.recude_hp(int(6 + self._player.get_strength()))
                    else:
                        monster.reduce_hp(6)
        elif play_card_result.get_name() == "Defend":
            self._player.add_block(5)
        elif play_card_result.get_name() == "Bash":
            self._player.add_block(5)
            for monster in self._monster_list:
                if monster.get_id() == target_id:
                    if self._player.get_strength() > 0:
                        if monster.get_vulnerable() > 0:
                            if self._player.get_weak() > 0:
                                monster.reduce_hp(
                                    int(7 + self._player.get_strength()) * 1.5 * 0.75
                                )
                            else:
                                monster.reduce_hp(
                                    int(7 + self._player.get_strength()) * 1.5
                                )
                        else:
                            monster.recude_hp(int(7 + self._player.get_strength()))
                    else:
                        monster.reduce_hp(7)
        elif play_card_result.get_name() == "Neutralize":
            for monster in self._monster_list:
                monster.add_vulnerable(1)
                monster.add_weak(1)
                if monster.get_id() == target_id:
                    if self._player.get_strength() > 0:
                        if monster.get_vulnerable() > 0:
                            if self._player.get_weak() > 0:
                                monster.reduce_hp(
                                    int(3 + self._player.get_strength()) * 1.5 * 0.75
                                )
                            else:
                                monster.reduce_hp(
                                    int(3 + self._player.get_strength()) * 1.5
                                )
                        else:
                            monster.recude_hp(int(3 + self._player.get_strength()))
                    else:
                        monster.reduce_hp(3)
        elif play_card_result.get_name() == "Survivor":
            self._player.add_block(8)
            self._player.add_strength(1)
        elif play_card_result.get_name() == "Eruption":
            for monster in self._monster_list:
                if monster.get_id() == target_id:
                    if self._player.get_strength() > 0:
                        if monster.get_vulnerable() > 0:
                            if self._player.get_weak() > 0:
                                monster.reduce_hp(
                                    int(9 + self._player.get_strength()) * 1.5 * 0.75
                                )
                            else:
                                monster.reduce_hp(
                                    int(9 + self._player.get_strength()) * 1.5
                                )
                        else:
                            monster.recude_hp(int(9 + self._player.get_strength()))
                    else:
                        monster.reduce_hp(9)
        elif play_card_result.get_name() == "Vigilance":
            self._player.add_block(8)
            self._player.add_strength(1)
        for monster in self._monster_list:
            if monster.is_defeated() == True:
                self._monster_list.remove(monster)
        return True

    def enemy_turn(self) -> None:
        """This method attempts to allow all remaining monsters in the encounter
        to take an action.
        """
        if self._player_turn == True:
            return None  # it means now is still player's turn.
        else:
            for monster in self._monster_list:
                if monster.get_name() == "Louse":
                    try:  # this section is only for online test, because in fact
                        # a monster would never get any strength in this game (?
                        # anyway, see code after except Keyerror.
                        monster.add_strength(monster.action()["strength"])
                        if monster.get_strength() > 0:
                            if monster.get_weak() > 0:
                                if self._player.get_vulnerable() > 0:
                                    self._player.reduce_hp(
                                        (
                                            monster.action()["damage"]
                                            + monster.get_strength()
                                        )
                                        * 0.75
                                        * 1.5
                                    )
                                else:
                                    self._player.reduce_hp(
                                        (
                                            monster.action()["damage"]
                                            + monster.get_strength()
                                        )
                                        * 0.75
                                    )
                            else:
                                self._player.reduce_hp(
                                    monster.action()["damage"] + monster.get_strength()
                                )
                        else:
                            self._player.reduce_hp(monster.action()["damage"])
                    except KeyError:
                        if monster.get_weak() > 0:
                            if self._player.get_vulnerable() > 0:
                                self._player.reduce_hp(
                                    (monster.action()["damage"]) * 0.75 * 1.5
                                )  # this is the damage that player would take
                                # if he has vulnerable, Louse monster got weak.
                            else:
                                self._player.reduce_hp(
                                    (monster.action()["damage"]) * 0.75
                                )  # this is the damage that player would take if
                                # Louse monster got weak.
                        else:
                            self._player.reduce_hp(
                                monster.action()["damage"]
                            )  # this is the damage that player would take if both
                            # side have no any status.
                elif monster.get_name() == "Cultist":
                    try:
                        monster.add_strength(monster.action()["strength"])
                        if monster.get_strength() > 0:
                            if monster.get_weak() > 0:
                                if self._player.get_vulnerable() > 0:
                                    self._player.reduce_hp(
                                        (
                                            monster.action()["damage"]
                                            + monster.get_strength()
                                        )
                                        * 0.75
                                        * 1.5
                                    )
                                    self._player.add_weak(monster.action()["weak"])
                                else:
                                    self._player.reduce_hp(
                                        (
                                            monster.action()["damage"]
                                            + monster.get_strength()
                                        )
                                        * 0.75
                                    )
                                    self._player.add_weak(monster.action()["weak"])
                            else:
                                self._player.reduce_hp(
                                    monster.action()["damage"] + monster.get_strength()
                                )
                                self._player.add_weak(monster.action()["weak"])
                        else:
                            (monster.action()["damage"])
                            self._player.add_weak(monster.action()["weak"])
                    except KeyError:
                        if monster.get_weak() > 0:
                            if self._player.get_vulnerable() > 0:
                                self._player.reduce_hp(
                                    (monster.action()["damage"]) * 0.75 * 1.5
                                )  # this is the damage that player would take
                                # if he has vulnerable, Cultist monster got weak.
                                self._player.add_weak(monster.action()["weak"])
                            else:
                                self._player.reduce_hp(
                                    (monster.action()["damage"]) * 0.75
                                )  # this is the damage that player would take
                                # if Cultist monster got weak.
                                self._player.add_weak(monster.action()["weak"])
                        else:
                            self._player.reduce_hp(
                                monster.action()["damage"]
                            )  # never happen.
                            self._player.add_weak(monster.action()["weak"])
                            # this is the damage that player would take if both
                            # side have no any status.
                        self._player.add_weak(monster.action()["weak"])
                    # Cultist's attack some time would apply weak to player.
                elif monster.get_name() == "JawWorm":
                    try:
                        monster.add_strength(monster.action()["strength"])
                        if monster.get_strength() > 0:
                            if monster.get_weak() > 0:
                                if self._player.get_vulnerable() > 0:
                                    self._player.reduce_hp(
                                        (
                                            monster.action()["damage"]
                                            + monster.get_strength()
                                        )
                                        * 0.75
                                        * 1.5
                                    )
                                else:
                                    self._player.reduce_hp(
                                        (
                                            monster.action()["damage"]
                                            + monster.get_strength()
                                        )
                                        * 0.75
                                    )
                            else:
                                self._player.reduce_hp(
                                    monster.action()["damage"] + monster.get_strength()
                                )
                        else:
                            (monster.action()["damage"])
                    except KeyError:
                        if monster.get_weak() > 0:
                            if self._player.get_vulnerable() > 0:
                                self._player.reduce_hp(
                                    (monster.action()["damage"]) * 0.75 * 1.5
                                )  # this is the damage that player would take
                                # if he has vulnerable, JawWorm monster got weak.
                            else:
                                self._player.reduce_hp(
                                    (monster.action()["damage"]) * 0.75
                                )  # this is the damage that player would take
                                # if JawWorm monster got weak.
                        else:
                            self._player.reduce_hp(
                                monster.action()["damage"]
                            )  # this is the damage that player would take if both
                            # side have no any status.
            self.start_new_turn()  # with a player turn and a monster turn,
            # start a whole new turn.


def main():
    # Implement this only once you've finished and tested ALL of the required
    # classes.

    player_user_select = input("Enter a player type: ")
    ironclad = (
        player_user_select[:1].upper()
        + player_user_select[1:4]
        + player_user_select[4:5].upper()
        + player_user_select[5:]
    )
    # transfer ironclad tp IronClad.
    if ironclad == IronClad().get_name():
        player = IronClad()
    elif (
        player_user_select.capitalize() == Silent().get_name()
    ):  # tranfer the first letter to capital.
        player = Silent()
    elif player_user_select.capitalize() == Watcher().get_name():
        player = Watcher()
    game_file_player_select = input(
        "Enter a game file: "
    )  # Obtain what game user want to play.
    read_game_file(game_file_player_select)

    encounter = Encounter(
        player, read_game_file(game_file_player_select)[0]
    )  # read_game_file(game_file_player_select) would return a list of instances of Monster().
    for (
        monster
    ) in (
        encounter._monster_list
    ):  # for the number of monster(s) it would vary the encounter time. The following code is for a single encounter.
        print("New encounter!")
        print("")
        print("MONSTERS")
        print("-" * 15)
        print("Monster", monster.get_id())
        print(monster.__str__())
        print("-" * 15)
        print("")
        print("")
        print("")
        print("PLAYER")
        print("-" * 62)
        print(player.get_name())
        print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
        print("Energy:", player.get_energy())
        print("Hand:", player.get_hand())
        print(
            "Block:",
            player.get_block(),
            "Strength:",
            player.get_strength(),
            "Vulnerable:",
            player.get_vulnerable(),
            "Weak:",
            player.get_weak(),
        )
        print("-" * 62)
        while monster.is_defeated() == False:
            players_move = input(
                "Enter a move: "
            )  # if monster doesn't be defeat, keep the loop
            if players_move == "end turn":
                encounter.end_player_turn()
                encounter.enemy_turn()
                if (
                    player.is_defeated() == True
                ):  # if you are defeated in enermy's turn print losing message and end the loop.
                    print("You have lost the game")
                    break
                print("MONSTERS")
                print("-" * 15)
                print("Monster", monster.get_id())
                print(monster.__str__())
                print("-" * 15)
                print("")
                print("")
                print("")
                print("PLAYER")
                print("-" * 56)
                print(player.get_name())
                print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                print("Energy:", player.get_energy())
                print("Hand:", player.get_hand())
                print(
                    "Block:",
                    player.get_block(),
                    "Strength:",
                    player.get_strength(),
                    "Vulnerable:",
                    player.get_vulnerable(),
                    "Weak:",
                    player.get_weak(),
                )
                print("-" * 56)
            elif players_move == "inspect deck":
                print("")
                print(player.get_deck())
                print("")
            elif players_move == "inspect discard":
                print("")
                print(player.get_discarded())
                print("")
            elif players_move == "inspect discard":
                print("")
                print(player.get_discarded())
                print("")
            elif players_move == "describe Strike":
                print("")
                print(Strike().get_description())
                print("")
            elif players_move == "describe Defend":
                print("")
                print(Defend().get_description())
                print("")
            elif players_move == "describe Bash":
                print("")
                print(Bash().get_description())
                print("")
            elif players_move == "describe Neutralize":
                print("")
                print(Neutralize().get_description())
                print("")
            elif players_move == "describe Survivor":
                print("")
                print(Survivor().get_description())
                print("")
            elif players_move == "describe Eruption":
                print("")
                print(Eruption().get_description())
                print("")
            elif players_move == "describe Vigilance":
                print("")
                print(Vigilance().get_description())
                print("")
            elif players_move == "play Defend":
                if (
                    encounter.player_apply_card("Defend") == True
                ):  # check if player can appliy the card successful.
                    print("MONSTERS")
                    print("-" * 15)
                    print("Monster", monster.get_id())
                    print(monster.__str__())
                    print("-" * 15)
                    print("")
                    print("")
                    print("")
                    print("PLAYER")
                    print("-" * 46)
                    print(player.get_name())
                    print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                    print("Energy:", player.get_energy())
                    print("Hand:", player.get_hand())
                    print(
                        "Block:",
                        player.get_block(),
                        "Strength:",
                        player.get_strength(),
                        "Vulnerable:",
                        player.get_vulnerable(),
                        "Weak:",
                        player.get_weak(),
                    )
                    print("-" * 46)
                else:  # if player cannot apply the card for certain reason, print fail message.
                    print("")
                    print("Card application failed.")
                    print("")
            elif players_move == "play Survivor":
                if encounter.player_apply_card("Survivor") == True:
                    print("MONSTERS")
                    print("-" * 15)
                    print("Monster", monster.get_id())
                    print(monster.__str__())
                    print("-" * 15)
                    print("")
                    print("")
                    print("")
                    print("PLAYER")
                    print("-" * 46)
                    print(player.get_name())
                    print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                    print("Energy:", player.get_energy())
                    print("Hand:", player.get_hand())
                    print(
                        "Block:",
                        player.get_block(),
                        "Strength:",
                        player.get_strength(),
                        "Vulnerable:",
                        player.get_vulnerable(),
                        "Weak:",
                        player.get_weak(),
                    )
                    print("-" * 46)
                else:
                    print("")
                    print("Card application failed.")
                    print("")
            elif players_move == "play Vigilance":
                if encounter.player_apply_card("Vigilance") == True:
                    print("MONSTERS")
                    print("-" * 15)
                    print("Monster", monster.get_id())
                    print(monster.__str__())
                    print("-" * 15)
                    print("")
                    print("")
                    print("")
                    print("PLAYER")
                    print("-" * 46)
                    print(player.get_name())
                    print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                    print("Energy:", player.get_energy())
                    print("Hand:", player.get_hand())
                    print(
                        "Block:",
                        player.get_block(),
                        "Strength:",
                        player.get_strength(),
                        "Vulnerable:",
                        player.get_vulnerable(),
                        "Weak:",
                        player.get_weak(),
                    )
                    print("-" * 46)
                else:
                    print("")
                    print("Card application failed.")
                    print("")
            elif (
                players_move[:12] == "play Strike "
            ):  # ensure the player wan to apply the card "Strike"
                target_id = int(
                    players_move[12:]
                )  # gain the target number from player's command. from position 12 in "play Strike {target_id}", it would be a number. define it as target id player want to attack.
                if encounter.player_apply_card("Strike", target_id) == True:
                    print("MONSTERS")
                    print("-" * 15)
                    print("Monster", monster.get_id())
                    print(monster.__str__())
                    print("-" * 15)
                    print("")
                    print("")
                    print("")
                    print("PLAYER")
                    print("-" * 46)
                    print(player.get_name())
                    print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                    print("Energy:", player.get_energy())
                    print("Hand:", player.get_hand())
                    print(
                        "Block:",
                        player.get_block(),
                        "Strength:",
                        player.get_strength(),
                        "Vulnerable:",
                        player.get_vulnerable(),
                        "Weak:",
                        player.get_weak(),
                    )
                    print("-" * 46)
                else:
                    print("")
                    print("Card application failed.")
                    print("")
            elif players_move[:10] == "play Bash ":
                target_id = int(players_move[10:])
                if encounter.player_apply_card("Bash", target_id) == True:
                    print("MONSTERS")
                    print("-" * 15)
                    print("Monster", monster.get_id())
                    print(monster.__str__())
                    print("-" * 15)
                    print("")
                    print("")
                    print("")
                    print("PLAYER")
                    print("-" * 46)
                    print(player.get_name())
                    print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                    print("Energy:", player.get_energy())
                    print("Hand:", player.get_hand())
                    print(
                        "Block:",
                        player.get_block(),
                        "Strength:",
                        player.get_strength(),
                        "Vulnerable:",
                        player.get_vulnerable(),
                        "Weak:",
                        player.get_weak(),
                    )
                    print("-" * 46)
                else:
                    print("")
                    print("Card application failed.")
                    print("")
            elif players_move[:16] == "play Neutralize ":
                target_id = int(players_move[16:])
                if encounter.player_apply_card("Neutralize", target_id) == True:
                    print("MONSTERS")
                    print("-" * 15)
                    print("Monster", monster.get_id())
                    print(monster.__str__())
                    print("-" * 15)
                    print("")
                    print("")
                    print("")
                    print("PLAYER")
                    print("-" * 46)
                    print(player.get_name())
                    print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                    print("Energy:", player.get_energy())
                    print("Hand:", player.get_hand())
                    print(
                        "Block:",
                        player.get_block(),
                        "Strength:",
                        player.get_strength(),
                        "Vulnerable:",
                        player.get_vulnerable(),
                        "Weak:",
                        player.get_weak(),
                    )
                    print("-" * 46)
                else:
                    print("")
                    print("Card application failed.")
                    print("")
            elif players_move[:14] == "play Eruption ":
                target_id = int(players_move[14:])
                if encounter.player_apply_card("Eruption", target_id) == True:
                    print("MONSTERS")
                    print("-" * 15)
                    print("Monster", monster.get_id())
                    print(monster.__str__())
                    print("-" * 15)
                    print("")
                    print("")
                    print("")
                    print("PLAYER")
                    print("-" * 46)
                    print(player.get_name())
                    print("HP:", f"{player.get_hp()}/{player.get_max_hp()}")
                    print("Energy:", player.get_energy())
                    print("Hand:", player.get_hand())
                    print(
                        "Block:",
                        player.get_block(),
                        "Strength:",
                        player.get_strength(),
                        "Vulnerable:",
                        player.get_vulnerable(),
                        "Weak:",
                        player.get_weak(),
                    )
                    print("-" * 46)
                else:
                    print("")
                    print("Card application failed.")
                    print("")
        else:  # if the monster in this encounter is defeated, end the loop.
            print("You have won the encounter!")
            break
    if (
        encounter._monster_list == []
    ):  # if all monster is defeated, print win message and end the loop
        print("OMG you win the game!")


if __name__ == "__main__":
    main()
    main()
