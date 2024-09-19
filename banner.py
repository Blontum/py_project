# banner.py
def display_banner(name):
    message = f" WELCOME TO STREET FIGHTER: {name} "
    banner_width = 70  
    print("#" * banner_width)
    print("#" + " " * (banner_width - 2) + "#")

    message_line = "#" + message.center(banner_width - 2) + "#"
    print(message_line)
    print("#" + " " * (banner_width - 2) + "#")
    print("#" * banner_width)
display_banner("Bo")

def display_banne(name):
    messa = f" WE DON'T USE : {name}"
    banne_width = 44 
    print("#" * banne_width)
    print("#" + " " * (banne_width - 2 ) + "#")
    print("#" + messa.center(banne_width - 2 ) + "#")
    print("#" + " " * (banne_width - 2 ) + "#")
    print("#" * banne_width)
display_banne("GUN")

def display(name):
    mesage = f"HHAHAHAHAHHAHAH: {name}"
    baner_width = 24

    print("#" * baner_width)
    print("#" + " " * (baner_width -2 ) + "#")
    print("#" + mesage.center(baner_width -2 ) + "#")
    print("#" + " " * (baner_width -2 ) + "#")
    print("#" * baner_width)
display("Bobo")