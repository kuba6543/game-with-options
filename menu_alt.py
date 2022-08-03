from turtle import down, left, right, up


def main_menu():
    import os
    import time
    print("Menu główne:")
    print("[1] Rozpocznij grę")
    print("[2] Ustawienia")
    print("[0] Wyjście")
    print("Wprowadź opcję z przedziału 0-9:")
    opt = int(input())
    os.system('cls')
    if opt == 1:
        core()
    elif opt == 2:
        settings()

    elif opt == 0:
        print("Dzięki za grę!")
        time.sleep(3)
        quit()

    else:
        print("Niewłaściwa opcja")
        print()
        main_menu()

def settings():
    import os

    print("Ustawienia:")
    print("[1] Sterowanie")
    print("[2] Dźwięk")
    print("[3] Obraz")
    print("[4] Rozgrywka")
    print("[0] Powrót")
    print("Wprowadź opcję z przedziału 0-9:")
    opt = int(input())
    os.system('cls')
    if opt == 1:
        settings_controls()
    elif opt == 2:
        settings_sound()
    elif opt == 3:
        settings_disp()
    elif opt == 4:
        settings_gameplay()
    elif opt == 0:
        main_menu()
    else:
        print("Niewłaściwa opcja")
        print()
        settings()

def settings_controls():
    import os, sys
    from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(os.path.join(sys.path[0], "settings.ini"))
    print("[1] Ruch w górę:", parser.get('CONTROLS','up'))
    print("[2] Ruch w dół:", parser.get('CONTROLS','down') )
    print("[3] Ruch w lewo:", parser.get('CONTROLS','left') )
    print("[4] Ruch w prawo:", parser.get('CONTROLS','right') )
    print("[0] Powrót")
    print("Wprowadź opcję z przedziału 0-9:")
    opt = int(input())
    if opt == 0:
        os.system('cls')
        settings()
    elif opt == 1 or opt == 2 or opt == 3 or opt == 4:    
        print("Wciśnij dowolny przycisk by przypisać klawisz do funkcji.")
        value=str(input())
        print(value)
        if len(value)==1:
            if opt == 1:
                parser.set('CONTROLS', 'up', value)
            if opt == 2:
                parser.set('CONTROLS', 'down', value)
            if opt == 3:
                parser.set('CONTROLS', 'left', value)
            if opt == 4:
                parser.set('CONTROLS', 'right', value)
            os.system('cls')
            print("Przypisano przycisk ", value, " do funkcji nr", opt,".")
        else:
            print("Za długi ciąg znaków")
            settings_controls()
    else:
        print("Niewłaściwa opcja")
        settings_controls()
    with open(os.path.join(sys.path[0], "settings.ini"), 'w') as configfile:
        parser.write(configfile)
    settings_controls()

def settings_sound():
    import os, sys
    from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(os.path.join(sys.path[0], "settings.ini"))
    print("[1] Poziom głośności muzyki:", parser.getint('SOUND','music'))
    print("[2] Poziom głośności dźwięku:", parser.getint('SOUND','sfx'))
    print("[0] Powrót")
    print("Wprowadź opcję z przedziału 0-9:")
    opt = int(input())
    if opt == 0:
        os.system('cls')
        settings()
    elif opt == 1:
        print("Podaj wartość głośności muzyki w przedziale 0-100.")
        value=int(input())
        value_str=str(value)
        if 0<=value<=100:
            parser.set('SOUND', 'music', value_str)
            os.system('cls')
            print("Przypisano wartość ", value, " jako głośność muzyki.")
        else:
            print("Wartość nie mieści się w przedziale.")
    elif opt == 2:
        print("Podaj wartość głośności dźwięku w przedziale 0-100.")
        value=int(input())
        value_str=str(value)
        if 0<=value<=100:
            parser.set('SOUND', 'sfx', value_str)
            os.system('cls')
            print("Przypisano wartość ", value, " jako głośność dźwięku.")
        else:
            print("Wartość nie mieści się w przedziale.")
    else:
        print("Niewłaściwa opcja")
        settings_sound()
    with open(os.path.join(sys.path[0], "settings.ini"), 'w') as configfile:
        parser.write(configfile)           
    settings_sound()    
        
def settings_disp():
    import os, sys
    from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(os.path.join(sys.path[0], "settings.ini"))
    print("[1] Rozdzielczość w poziomie:", parser.getint('DISPLAY','x'))
    print("[2] Rozdzielczość w pionie:", parser.getint('DISPLAY','y'))
    if parser.getint('DISPLAY','fullscreen')==1:
        print("[3] Tryb pełnego ekranu: Włączone")
    else:
        print("[3] Tryb pełnego ekranu: Wyłączone")
    print("[0] Powrót")
    print("Wprowadź opcję z przedziału 0-9:")
    opt = int(input())
    if opt == 0:
        os.system('cls')
        settings()
    elif opt == 1:
        print("Podaj wartość rozdzielczości poziomej w przedziale 0-100.")
        value=int(input())
        value_str=str(value)
        parser.set('DISPLAY', 'x', value_str)
        os.system('cls')
        print("Przypisano wartość ", value, " jako rozdzielczość poziomą.")
    elif opt == 2:
        print("Podaj wartość rozdzielczości pionowej w przedziale 0-100.")
        value=int(input())
        value_str=str(value)
        parser.set('DISPLAY', 'y', value_str)
        os.system('cls')
        print("Przypisano wartość ", value, " jako rozdzielczość pionową.")
    elif opt == 3:
        print("Wybierz tryb pełnego ekranu wpisując odpowiadającą cyfrę:")
        print("0 - wyłączony, 1 - włączony")
        value=int(input())
        value_str=str(value)
        if value==0 or value==1:
            parser.set('DISPLAY', 'fullscreen', value_str)
            os.system('cls')
            print("Przypisano wartość ", value, " jako tryb pełnoekranowy.")
        else:
            print("Niewłaściwa opcja")
            settings_disp()   
    else:
        print("Niewłaściwa opcja")
        settings_disp()
    with open(os.path.join(sys.path[0], "settings.ini"), 'w') as configfile:
        parser.write(configfile) 
    settings_disp()

def settings_gameplay():
    import os, sys
    from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(os.path.join(sys.path[0], "settings.ini"))
    if parser.getint('GAMEPLAY','difficulty')==0:
        print("[1] Poziom trudności: Łatwy")
    elif parser.getint('GAMEPLAY','difficulty')==1:
        print("[1] Poziom trudności: Normalny")
    elif parser.getint('GAMEPLAY','difficulty')==2:
        print("[1] Poziom trudności: Trudny")
    print("[0] Powrót")
    print("Wprowadź opcję z przedziału 0-9:")
    opt = int(input())
    if opt == 0:
        os.system('cls')
        settings()
    elif opt == 1:
        print("Wybierz poziom trudności wpisując odpowiadającą cyfrę:")
        print("0 - Łatwy, 1 - Normalny, 2 - Trudny")
        value=int(input())
        value_str=str(value)
        if 0<=value<=2:
            parser.set('GAMEPLAY', 'difficulty', value_str)
            os.system('cls')
            print("Przypisano wartość ", value, " jako poziom trudności.")
        else:
            print("Niewłaściwa opcja")
            settings_gameplay()
    else:
        print("Niewłaściwa opcja")
        settings_gameplay()
    with open(os.path.join(sys.path[0], "settings.ini"), 'w') as configfile:
        parser.write(configfile) 
    settings_gameplay()

def core():
    import arcade, os, sys, random
    from configparser import ConfigParser
    from pyglet.math import Vec2
    parser = ConfigParser()
    parser.read(os.path.join(sys.path[0], "settings.ini"))
    WIDTH=parser.getint('DISPLAY','x')
    HEIGHT=parser.getint('DISPLAY','y')
    #up=(parser.get('CONTROLS','up'))
    #down=(parser.get('CONTROLS','down'))
    #left=(parser.get('CONTROLS','left'))
    #right=(parser.get('CONTROLS','right'))
    #bind_up=("arcade.key", str.upper(up))
    #bind_down=("arcade.key", str.upper(down))
    #bind_left=("arcade.key", str.upper(left))
    #bind_right=("arcade.key", str.upper(right))
    #arcade.key.UP=".".join(bind_up)
    #arcade.key.DOWN=".".join(bind_down)
    #arcade.key.LEFT=".".join(bind_left)
    #arcade.key.RIGHT=".".join(bind_right)

    SCREEN_TITLE = "Gra"
    CAMERA_SPEED = 0.5

    # How fast the character moves
    PLAYER_MOVEMENT_SPEED = 8-parser.getint('GAMEPLAY','difficulty')


    class MyGame(arcade.Window):
        """ Main application class. """

        def __init__(self, width, height, title):
            """
            Initializer
            """
            super().__init__(width, height, title, resizable=True)

            # Sprite lists
            self.player_list = None
            self.wall_list = None
            self.coin_list = None
            # Set up the player
            self.player_sprite = None
            self.score=0
            # Physics engine so we don't run into walls.
            self.physics_engine = None

            # Track the current state of what key is pressed
            self.left_pressed = False
            self.right_pressed = False
            self.up_pressed = False
            self.down_pressed = False

            # Create the cameras. One for the GUI, one for the sprites.
            # We scroll the 'sprite world' but not the GUI.
            self.camera_sprites = arcade.Camera(WIDTH, HEIGHT)
            self.camera_gui = arcade.Camera(WIDTH, HEIGHT)

        def setup(self):
            """ Set up the game and initialize the variables. """
            # Sprite lists
            self.player_list = arcade.SpriteList()
            self.wall_list = arcade.SpriteList()
            self.coin_list = arcade.SpriteList()
            self.score=0
            # Set up the player
            self.player_sprite = arcade.Sprite(os.path.join(sys.path[0], "bin/player.png"),
                                               scale=0.125)
            self.player_sprite.center_x = 0
            self.player_sprite.center_y = 0
            self.player_list.append(self.player_sprite)

            #granice mapy
            for x in (-2048, 2048):
                for y in range(-1024, 1088, 64):
                    wall = arcade.Sprite(os.path.join(sys.path[0], "bin/crate.png"), 0.125)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
            for x in range(-2048, 2112, 64):
                for y in (-1024, 1024):
                    wall = arcade.Sprite(os.path.join(sys.path[0], "bin/crate.png"), 0.125)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
            #losowe skrzynie
            for x in range(-2048, 2112, 64):
                for y in range(-1024, 1088, 64):
                    if random.randrange(128)>125:
                        wall = arcade.Sprite(os.path.join(sys.path[0], "bin/crate.png"), 0.125)
                        wall.center_x = x
                        wall.center_y = y
                        self.wall_list.append(wall)

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

            # Set the background color
            arcade.set_background_color(arcade.color.AMAZON)
            # Create the coins
            for i in range(100):

            # Create the coin instance
            # Coin image from kenney.nl
                coin = arcade.Sprite(os.path.join(sys.path[0], "bin/blob.png"), 1)

            # Position the coin
                coin.center_x = random.randrange(-2000,2000)
                coin.center_y = random.randrange(-976,976)

                self.coin_list.append(coin)

        def on_draw(self):
            """ Render the screen. """

            # This command has to happen before we start drawing
            self.clear()

            # Select the camera we'll use to draw all our sprites
            self.camera_sprites.use()

            # Draw all the sprites.
            self.wall_list.draw()
            self.player_list.draw()
            self.coin_list.draw()
            # Select the (unscrolled) camera for our GUI
            self.camera_gui.use()

            # Draw the GUI
            arcade.draw_rectangle_filled(self.width // 2,
                                         20,
                                         self.width,
                                         40,
                                         arcade.color.ALMOND)
            text = f"Position: {self.player_sprite.position}, Exp: {self.score} "
            arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        def on_key_press(self, key, modifiers):
            """Called whenever a key is pressed. """

            if key ==  arcade.key.UP:
                self.up_pressed = True
            elif key == arcade.key.DOWN:
                self.down_pressed = True
                self.player_sprite.turn_left(180)
            elif key == arcade.key.LEFT:
                self.left_pressed = True
                self.player_sprite.turn_left(90)
            elif key == arcade.key.RIGHT:
                self.right_pressed = True
                self.player_sprite.turn_right(90)

        def on_key_release(self, key, modifiers):
            """Called when the user releases a key. """

            if key ==  arcade.key.UP:
                self.up_pressed = False
            elif key == arcade.key.DOWN:
                self.down_pressed = False
                self.player_sprite.turn_right(180)
            elif key == arcade.key.LEFT:
                self.left_pressed = False
                self.player_sprite.turn_right(90)
            elif key == arcade.key.RIGHT:
                self.right_pressed = False
                self.player_sprite.turn_left(90)

        def on_update(self, delta_time):
            """ Movement and game logic """

            # Calculate speed based on the keys pressed
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0

            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.physics_engine.update()

            # Scroll the screen to the player
            self.scroll_to_player()
            # Generate a list of all sprites that collided with the player.
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

        def scroll_to_player(self):
            """
            Scroll the window to the player.

            if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
            Anything between 0 and 1 will have the camera move to the location with a smoother
            pan.
            """

            position = Vec2(self.player_sprite.center_x - self.width / 2,
                            self.player_sprite.center_y - self.height / 2)
            self.camera_sprites.move_to(position, CAMERA_SPEED)

        def on_resize(self, width, height):
            """
            Resize window
            Handle the user grabbing the edge and resizing the window.
            """
            self.camera_sprites.resize(int(width), int(height))
            self.camera_gui.resize(int(width), int(height))


    def main():
        """ Main function """
        window = MyGame(WIDTH, HEIGHT, SCREEN_TITLE)
        window.setup()
        arcade.run()

    if __name__ == "__main__":
        main()    
    

main_menu()