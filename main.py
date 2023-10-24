#===IMPORTS===
from tkinter import *
import json
import time
import random
import os
import fileinput
import PIL

#===WINDOWS===
def home_window():
    homewindow = Tk()
    homewindow.title('Hetnikfut | Home')
    homewindow.iconbitmap(r'logo.ico')
    homewindow.geometry("720x1280+30+30")
    homewindow.resizable(False,False)
    background_homewindow_picture = PhotoImage(file="background.png")
    background_homewindow = Label(homewindow, image=background_homewindow_picture)
    background_homewindow.place(x=0, y=0, relwidth=1, relheight=1)

    with open("coins.txt") as f:
        coinsamount = f.read()
    global coinsdisplay
    coinsdisplay = Label(homewindow, text=coinsamount, fg="white", bg="black", font=("Helvetica", 25))
    coinsdisplay.place(x=300,y=45)

    packs_button_picture = PhotoImage(file='packs_btn.png')
    packs_button = Button(homewindow, image=packs_button_picture,borderwidth=0, command=packs_window, highlightthickness=0)
    packs_button.place(x=30, y=180)

    team_button_picture = PhotoImage(file='team_btn.png')
    team_button = Button(homewindow, image=team_button_picture,borderwidth=0, command=lambda: squadordraft('s'), highlightthickness=0)
    team_button.place(x=40, y=480)

    sbc_button_picture = PhotoImage(file='sbc_btn.png')
    sbc_button = Button(homewindow, image=sbc_button_picture,borderwidth=0, command=sbc1_window, highlightthickness=0)
    sbc_button.place(x=25, y=800)

    blackztheking_button_picture = PhotoImage(file='blacktheking.png')
    blackztheking_button = Button(homewindow, image=blackztheking_button_picture,borderwidth=0, command=blackztheking_window, highlightthickness=0)
    blackztheking_button.place(x=230, y=1200)

    homewindow.mainloop()

def blackztheking_window():
    blackzthekingwindow = Toplevel()
    blackzthekingwindow.title('Hetnikfut | Developer Mode')
    blackzthekingwindow.iconbitmap(r'logo.ico')
    blackzthekingwindow.geometry("720x1280+30+30")
    blackzthekingwindow.resizable(False,False)
    background_blackzthekingwindow_picture = PhotoImage(file="cupons.png")
    background_blackzthekingwindow = Label(blackzthekingwindow, image=background_blackzthekingwindow_picture)
    background_blackzthekingwindow.place(x=0, y=0, relwidth=1, relheight=1)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(blackzthekingwindow, image=backtohome_button_picture,borderwidth=0, command=lambda: blackzthekingwindow.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    global code_button
    code_button = Entry(blackzthekingwindow, width=64, bg='#343434', borderwidth=0, fg="white")
    code_button.place(x=165, y=350, height=30)

    subcode_button_picture = PhotoImage(file='submit_btn.png')
    subcode_button = Button(blackzthekingwindow, image=subcode_button_picture,borderwidth=0, command=lambda: get_custom_code(code_button.get()), highlightthickness=0)
    subcode_button.place(x=250, y=400)

    blackzthekingwindow.mainloop()

def packs_window():
    packswindow = Toplevel()
    packswindow.title('Hetnikfut | Packs')
    packswindow.iconbitmap(r'logo.ico')
    packswindow.geometry("720x1280+30+30")
    packswindow.resizable(False,False)
    background_packswindow_picture = PhotoImage(file="packs.png")
    background_packswindow = Label(packswindow, image=background_packswindow_picture)
    background_packswindow.place(x=0, y=0, relwidth=1, relheight=1)

    with open("coins.txt") as f:
        coinsamount = f.read()
    global coindisplay_pack
    coindisplay_pack = Label(packswindow, text=coinsamount, fg="white", bg="black", font=("Helvetica", 25))
    coindisplay_pack.place(x=300,y=45)

    plus80pack_button_picture = PhotoImage(file='80pluspack_btn.png')
    plus80pack_button = Button(packswindow, image=plus80pack_button_picture,borderwidth=0, command=lambda: openpackanimation("plus80"), highlightthickness=0)
    plus80pack_button.place(x=20, y=255)

    goldpack_button_picture = PhotoImage(file='goldpack_btn.png')
    goldpack_button = Button(packswindow, image=goldpack_button_picture,borderwidth=0, command=lambda: openpackanimation("gold"), highlightthickness=0)
    goldpack_button.place(x=13, y=420)

    promopack_button_picture = PhotoImage(file='promopack_btn.png')
    promopack_button = Button(packswindow, image=promopack_button_picture,borderwidth=0, command=lambda: openpackanimation("promo"), highlightthickness=0)
    promopack_button.place(x=353, y=255)

    plus85pack_button_picture = PhotoImage(file='85pluspack_btn.png')
    plus85pack_button = Button(packswindow, image=plus85pack_button_picture,borderwidth=0, command=lambda: openpackanimation("plus85"), highlightthickness=0)
    plus85pack_button.place(x=20, y=575)

    tokenpack_button_picture = PhotoImage(file='tokenpack_btn.png')
    tokenpack_button = Button(packswindow, image=tokenpack_button_picture,borderwidth=0, command=lambda: openpackanimation("token"), highlightthickness=0)
    tokenpack_button.place(x=356, y=575)

    mypacks_button_picture = PhotoImage(file='mypacks_btn.png')
    mypacks_button = Button(packswindow, image=mypacks_button_picture,borderwidth=0, command=lambda: mypacks_window(), highlightthickness=0)
    mypacks_button.place(x=50, y=900)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(packswindow, image=backtohome_button_picture,borderwidth=0, command=lambda: packswindow.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)
    
    packswindow.mainloop()

def pack_animation(option):
    global packanimation
    packanimation = Toplevel()
    packanimation.title('Hetnikfut | Pack')
    packanimation.iconbitmap(r'logo.ico')
    packanimation.geometry("720x1280+30+30")
    packanimation.resizable(False,False)
    background_packanimation_picture = PhotoImage(file="back.png")
    background_packanimation = Label(packanimation, image=background_packanimation_picture)
    background_packanimation.place(x=0, y=0, relwidth=1, relheight=1)

    if option == "plus80":
        with open("coins.txt") as f:
            coinsamount = f.read()
        if int(coinsamount) < 5000:
            packanimation.destroy()
        else:
            coinsamount = int(coinsamount) - 5000
            with open("coins.txt", "w") as f:
                f.write(str(coinsamount))
                f.close()

            with open("coins.txt") as f:
                f.close()
            coinsdisplay['text'] = str(coinsamount)
            coindisplay_pack['text'] = str(coinsamount)

        fodder = [
            ['shtaif.png', '83', 'LW', '3000'],
            ['isar.png', '84', 'CDM', '4000'],
            ['mishuk.png', '84', 'CB', '4000'],
            ['ulitsky.png', '84', 'ST', '4000'],

        ]
        good = [
            ['shoval.png', '87', 'CM', '10000'],
            ['yanchevsky.png', '87', 'CB', '10000'],
            ['bampi.png', '88', 'LM', '15000'],
            ['bensi.png', '88', 'CM', '15000'],
            ['shon.png', '88', 'CAM', '15000'],
            ['ulitsky_rb.png', '85', 'ST', '20000'],
            ['mandel.png', '86', 'GK', '20000'],
            ['avihai.png', '86', 'CB', '60000']
        ]
        rares = [
            ['yahez.png', '94', 'CAM', '200000'],
            ['yakov_i.png', '96', 'CAM', '1100000'],
            ['yotam.png', '96', 'CM', '1100000'],
            ['rotem.png', '95', 'CF', '800000']
        ]


        chance = random.randint(1,50)
        if chance <= 40:
            player = random.choice(fodder)
        if chance >= 40 and chance < 49:
            player = random.choice(good)
        if chance == 50:
            player = random.choice(rares)

        display_80plus = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_80plus.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg= Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0, command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0, command=lambda: save_player(player[0]), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black", font=("Helvetica", 25))

        def setpos():
            display_80plus["text"] = player[2]
        display_80plus.after(500, setpos)
        def setrat():
            display_80plus["text"] = player[1]
        display_80plus.after(1500, setrat)
        def revplayer():
            display_80plus.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_80plus.after(3000, revplayer)

    if option == "gold":
        with open("coins.txt") as f:
            coinsamount = f.read()
        if int(coinsamount) < 10000:
            packanimation.destroy()
        else:
            coinsamount = int(coinsamount) - 10000
            with open("coins.txt", "w") as f:
                f.write(str(coinsamount))
                f.close()

            coinsdisplay['text'] = str(coinsamount)
            coindisplay_pack['text'] = str(coinsamount)

            gold84 = [
                ['shtaif.png', '83', 'LW', '3000'],
                ['isar.png', '84', 'CDM', '4000'],
                ['mishuk.png', '84', 'CB', '4000'],
                ['ulitsky.png', '84', 'ST', '4000'],
                ['yakov.png', '86', 'CB', '7000']
            ]
            gold88 = [
                ['shoval.png', '87', 'CM', '10000'],
                ['yanchevsky.png', '87', 'CB', '10000'],
                ['bampi.png', '88', 'LM', '15000'],
                ['bensi.png', '88', 'CM', '15000'],
                ['shon.png', '88', 'CAM', '15000']
            ]
            gold89 = [
                ['grine.png', '89', 'CDM', '18000'],
                ['morad.png', '89', 'RM', '18000']
            ]
            gold94 = [
                ['yahez.png', '94', 'CAM', '200000']
            ]

            chance = random.randint(1,68)
            if chance <= 30:
                player = random.choice(gold84)
            if chance >= 30 and chance < 50:
                player = random.choice(gold88)
            if chance >= 50 and chance < 65:
                player = random.choice(gold89)
            if chance >= 65 and chance < 67:
                player = random.choice(gold94)

            display_gold = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
            display_gold.place(x=320, y=500)
            playerimg_picture = PhotoImage(file=player[0])
            playerimg= Label(packanimation, image=playerimg_picture)
            sell_button_picture = PhotoImage(file='sell_btn.png')
            sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0, command=lambda: add_coins(player[3], '1'), highlightthickness=0)
            save_button_picture = PhotoImage(file='save_btn.png')
            save_button = Button(packanimation, image=save_button_picture, borderwidth=0, command=lambda: save_player(player[0]), highlightthickness=0)
            valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black", font=("Helvetica", 25))

            def setpos():
                display_gold["text"] = player[2]
            display_gold.after(500, setpos)
            def setrat():
                display_gold["text"] = player[1]
            display_gold.after(1500, setrat)
            def revplayer():
                display_gold.destroy()
                playerimg.place(x=0, y=0, relwidth=1, relheight=1)

                sell_button.place(x=270, y=1000)
                save_button.place(x=270, y=1100)
                valuedisplay.place(x=290, y=45)

            display_gold.after(3000, revplayer)

    if option == "promo":
        with open("coins.txt") as f:
            coinsamount = f.read()
        if int(coinsamount) < 100000:
            packanimation.destroy()
            pass
        else:
            coinsamount = int(coinsamount) - 100000
            with open("coins.txt", "w") as f:
                f.write(str(coinsamount))
                f.close()

            coinsdisplay['text'] = str(coinsamount)
            coindisplay_pack['text'] = str(coinsamount)

        promo86 = [
            ['ulitsky_rb.png', '85', 'ST', '20000'],
            ['mandel.png', '86', 'GK', '20000'],
            ['isar_yc.png', '86', 'CDM', '60000'],
            ['avihai.png', '86', 'CB', '60000']
        ]
        promo88 = [
            ['yakov_rb.png', '87', 'CB', '85000'],
            ['shoval_fba.png', '88', 'CM', '80000']
        ]
        promo89 = [
            ['bampi_rb.png', '89', 'LM', '70000'],
            ['shon_fba.png', '89', 'LW', '70000'],
            ['cohen.png', '89', 'GK', '40000'],
            ['yanchevsky_yc.png', '89', 'CB', '250000'],
            ['bensi_ni.png', '89', 'CF', '100000']
        ]
        promo90 = [
            ['grine_fba.png', '90', 'CDM', '90000'],
            ['bensi_fba.png', '90', 'CAM', '120000'],
            ['cohen_yc.png', '90', 'GK', '80000'],
            ['morad_ni.png', '90', 'RM', '90000']
        ]
        promo91 = [
            ['bensi_yc.png', '91', 'LW', '180000'],
            ['shon_yc.png', '91', 'LW', '170000']
        ]

        promo96 = [
            ['yahez_yc.png', '96', 'CAM', '600000'],
            ['yakov_i.png', '96', 'CAM', '1100000'],
            ['yotam.png', '96', 'CM', '1100000'],
            ['rotem.png', '95', 'CF', '800000']
        ]

        chance = random.randint(1, 86)
        if chance <= 30:
            player = random.choice(promo86)
        if chance >= 30 and chance < 50:
            player = random.choice(promo88)
        if chance >= 50 and chance < 64:
            player = random.choice(promo89)
        if chance >= 64 and chance < 75:
            player = random.choice(promo90)
        if chance >= 75 and chance < 83:
            player = random.choice(promo91)
        if chance >= 83 and chance < 85:
            player = random.choice(promo96)

        display_promo = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_promo.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg = Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0, command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0, command=lambda: save_player(player[0]), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black", font=("Helvetica", 25))

        def setpos():
            display_promo["text"] = player[2]

        display_promo.after(500, setpos)

        def setrat():
            display_promo["text"] = player[1]

        display_promo.after(1500, setrat)

        def revplayer():
            display_promo.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_promo.after(3000, revplayer)

    if option == "plus85":
        with open("coins.txt") as f:
            coinsamount = f.read()
        if int(coinsamount) < 85000:
            packanimation.destroy()
        else:
            coinsamount = int(coinsamount) - 85000
            with open("coins.txt", "w") as f:
                f.write(str(coinsamount))
                f.close()

            with open("coins.txt") as f:
                f.close()
            coinsdisplay['text'] = str(coinsamount)
            coindisplay_pack['text'] = str(coinsamount)

        gold86 = [
            ['yakov.png', '86', 'CB', '7000']
        ]
        gold88 = [
            ['shoval.png', '87', 'CM', '10000'],
            ['yanchevsky.png', '87', 'CB', '10000'],
            ['bampi.png', '88', 'LM', '15000'],
            ['bensi.png', '88', 'CM', '15000'],
            ['shon.png', '88', 'CAM', '15000']
        ]
        gold89 = [
            ['grine.png', '89', 'CDM', '18000'],
            ['morad.png', '89', 'CM', '18000']
        ]
        gold94 = [
            ['yahez.png', '94', 'CAM', '200000']
        ]
        promo86 = [
            ['ulitsky_rb.png', '85', 'ST', '20000'],
            ['mandel.png', '86', 'GK', '20000'],
            ['isar_yc.png', '86', 'CDM', '60000'],
            ['avihai.png', '86', 'CB', '60000']
        ]
        promo88 = [
            ['yakov_rb.png', '87', 'CB', '85000'],
            ['shoval_fba.png', '88', 'CM', '80000']
        ]
        promo89 = [
            ['bampi_rb.png', '89', 'LM', '70000'],
            ['shon_fba.png', '89', 'LW', '70000'],
            ['cohen.png', '89', 'GK', '40000'],
            ['bensi_ni.png', '89', 'CF', '100000']
        ]
        promo90 = [
            ['grine_fba.png', '90', 'CDM', '90000'],
            ['bensi_fba.png', '90', 'CAM', '120000'],
            ['morad_ni.png', '90', 'RM', '90000']
        ]
        promo96 = [
            ['yahez_yc.png', '96', 'CAM', '600000'],
            ['yakov_i.png', '96', 'CAM', '1100000'],
            ['yotam.png', '96', 'CM', '1100000'],
            ['rotem.png', '95', 'CF', '800000']
        ]

        chance = random.randint(1, 108)
        if chance <= 104 and chance < 107:
            player = random.choice(promo96)
        if chance <= 30:
            player = random.choice(gold86)
        if chance >= 30 and chance < 50:
            player = random.choice(gold88)
        if chance >= 50 and chance < 65:
            player = random.choice(gold89)
        if chance >= 66 and chance < 80:
            player = random.choice(promo86)
        if chance >= 80 and chance < 90:
            player = random.choice(promo88)
        if chance >= 90 and chance < 98:
            player = random.choice(promo89)
        if chance == 99 or chance == 100:
            player = random.choice(promo90)
        if chance >= 100 and chance < 104:
            player = random.choice(gold94)


        display_plus85 = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_plus85.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg = Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0, command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0, command=lambda: save_player(player[0]), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black", font=("Helvetica", 25))

        def setpos():
            display_plus85["text"] = player[2]

        display_plus85.after(500, setpos)

        def setrat():
            display_plus85["text"] = player[1]

        display_plus85.after(1500, setrat)

        def revplayer():
            display_plus85.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_plus85.after(3000, revplayer)

    if option == "token":
        with open("coins.txt") as f:
            coinsamount = f.read()
        if int(coinsamount) < 50000:
            packanimation.destroy()
            pass
        else:
            coinsamount = int(coinsamount) - 50000
            with open("coins.txt", "w") as f:
                f.write(str(coinsamount))
                f.close()

            coinsdisplay['text'] = str(coinsamount)
            coindisplay_pack['text'] = str(coinsamount)

        tokens = [
            ['boni.png', '551', 'CM', '5000'],
            ['misi.png', '551', 'CM', '5000'],
            ['lady.png', '551', 'CM', '5000'],
            ['zoey.png', '551', 'CM', '5000'],
            ['joy.png', '551', 'CM', '5000']
        ]

        player = random.choice(tokens)

        display_tokens = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_tokens.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg = Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0, command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0, command=lambda: get_custom_code(code_button.get()), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black", font=("Helvetica", 25))

        def setpos():
            display_tokens["text"] = player[2]

        display_tokens.after(500, setpos)

        def setrat():
            display_tokens["text"] = player[1]

        display_tokens.after(1500, setrat)

        def revplayer():
            display_tokens.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_tokens.after(3000, revplayer)

    if option == "packs_85":

        gold86 = [
            ['yakov.png', '86', 'CB', '7000']
        ]
        gold88 = [
            ['shoval.png', '87', 'CM', '10000'],
            ['yanchevsky.png', '87', 'CB', '10000'],
            ['bampi.png', '88', 'LM', '15000'],
            ['bensi.png', '88', 'CM', '15000'],
            ['shon.png', '88', 'CAM', '15000']
        ]
        gold89 = [
            ['grine.png', '89', 'CDM', '18000'],
            ['morad.png', '89', 'CM', '18000']
        ]
        gold94 = [
            ['yahez.png', '94', 'CAM', '200000']
        ]
        promo86 = [
            ['ulitsky_rb.png', '85', 'ST', '20000'],
            ['mandel.png', '86', 'GK', '20000'],
            ['isar_yc.png', '86', 'CDM', '60000'],
            ['avihai.png', '86', 'CB', '60000']
        ]
        promo88 = [
            ['yakov_rb.png', '87', 'CB', '85000'],
            ['shoval_fba.png', '88', 'CM', '80000']
        ]
        promo89 = [
            ['bampi_rb.png', '89', 'LM', '70000'],
            ['shon_fba.png', '89', 'LW', '70000'],
            ['cohen.png', '89', 'GK', '40000'],
            ['bensi_ni.png', '89', 'CF', '100000']
        ]
        promo90 = [
            ['grine_fba.png', '90', 'CDM', '90000'],
            ['bensi_fba.png', '90', 'CAM', '120000'],
            ['morad_ni.png', '90', 'RM', '90000']
        ]
        promo96 = [
            ['yahez_yc.png', '96', 'CAM', '600000'],
            ['yakov_i.png', '96', 'CAM', '1100000'],
            ['yotam.png', '96', 'CM', '1100000'],
            ['rotem.png', '95', 'CF', '800000']
        ]

        chance = random.randint(1, 108)
        if chance <= 104 and chance < 107:
            player = random.choice(promo96)
        if chance <= 30:
            player = random.choice(gold86)
        if chance >= 30 and chance < 50:
            player = random.choice(gold88)
        if chance >= 50 and chance < 65:
            player = random.choice(gold89)
        if chance >= 66 and chance < 80:
            player = random.choice(promo86)
        if chance >= 80 and chance < 90:
            player = random.choice(promo88)
        if chance >= 90 and chance < 98:
            player = random.choice(promo89)
        if chance == 99 or chance == 100:
            player = random.choice(promo90)
        if chance >= 100 and chance < 104:
            player = random.choice(gold94)


        display_plus85 = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_plus85.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg = Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0, command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0, command=lambda: save_player(player[0]), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black", font=("Helvetica", 25))

        def setpos():
            display_plus85["text"] = player[2]

        display_plus85.after(500, setpos)

        def setrat():
            display_plus85["text"] = player[1]

        display_plus85.after(1500, setrat)

        with open("packs.txt") as f:
            packsamt = f.read()
            newpack = f"{int(packsamt.split('-')[0])-1}-{packsamt.split('-')[1]}-{packsamt.split('-')[2]}-{packsamt.split('-')[3]}"
        with open("packs.txt", "w") as f:
            f.write(newpack)

        def revplayer():
            display_plus85.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_plus85.after(3000, revplayer)

    if option == "packs_87":

        gold88 = [
            ['shoval.png', '87', 'CM', '10000'],
            ['yanchevsky.png', '87', 'CB', '10000'],
            ['bampi.png', '88', 'LM', '15000'],
            ['bensi.png', '88', 'CM', '15000'],
            ['shon.png', '88', 'CAM', '15000']
        ]
        gold89 = [
            ['grine.png', '89', 'CDM', '18000'],
            ['morad.png', '89', 'CM', '18000']
        ]
        gold94 = [
            ['yahez.png', '94', 'CAM', '200000']
        ]
        promo88 = [
            ['yakov_rb.png', '87', 'CB', '85000'],
            ['shoval_fba.png', '88', 'CM', '80000']
        ]
        promo89 = [
            ['bampi_rb.png', '89', 'LM', '70000'],
            ['shon_fba.png', '89', 'LW', '70000'],
            ['cohen.png', '89', 'GK', '40000'],
            ['bensi_ni.png', '89', 'CF', '100000']
        ]
        promo90 = [
            ['grine_fba.png', '90', 'CDM', '90000'],
            ['bensi_fba.png', '90', 'CAM', '120000'],
            ['morad_ni.png', '90', 'RM', '90000']
        ]
        promo96 = [
            ['yahez_yc.png', '96', 'CAM', '600000'],
            ['yakov_i.png', '96', 'CAM', '1100000'],
            ['yotam.png', '96', 'CM', '1100000'],
            ['rotem.png', '95', 'CF', '800000']
        ]

        chance = random.randint(1, 108)
        if chance <= 104 and chance < 107:
            player = random.choice(promo96)
        if chance < 50:
            player = random.choice(gold88)
        if chance >= 50 and chance < 65:
            player = random.choice(gold89)
        if chance >= 66 and chance < 90:
            player = random.choice(promo88)
        if chance >= 90 and chance < 98:
            player = random.choice(promo89)
        if chance == 99 or chance == 100:
            player = random.choice(promo90)
        if chance >= 100 and chance < 104:
            player = random.choice(gold94)

        display_plus87 = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_plus87.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg = Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0,
                                command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0,
                                command=lambda: save_player(player[0]), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black",
                                font=("Helvetica", 25))

        def setpos():
            display_plus87["text"] = player[2]

        display_plus87.after(500, setpos)

        def setrat():
            display_plus87["text"] = player[1]

        display_plus87.after(1500, setrat)

        with open("packs.txt") as f:
            packsamt = f.read()
            newpack = f"{packsamt.split('-')[0]}-{int(packsamt.split('-')[1]) - 1}-{packsamt.split('-')[2]}-{packsamt.split('-')[3]}"
        with open("packs.txt", "w") as f:
            f.write(newpack)

        def revplayer():
            display_plus87.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_plus87.after(3000, revplayer)

    if option == "packs_90":

        gold94 = [
            ['yahez.png', '94', 'CAM', '200000']
        ]
        promo90 = [
            ['grine_fba.png', '90', 'CDM', '90000'],
            ['bensi_fba.png', '90', 'CAM', '120000'],
            ['morad_ni.png', '90', 'RM', '90000']
        ]
        promo96 = [
            ['yahez_yc.png', '96', 'CAM', '600000'],
            ['yakov_i.png', '96', 'CAM', '1100000'],
            ['yotam.png', '96', 'CM', '1100000'],
            ['rotem.png', '95', 'CF', '800000']
        ]

        chance = random.randint(1, 51)
        if chance >= 1 and chance < 43:
            player = random.choice(promo90)
        if chance >= 44 and chance < 47:
            player = random.choice(gold94)
        if chance >= 48 and chance < 50:
            player = random.choice(promo96)

        display_plus90 = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_plus90.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg = Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0,
                                command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0,
                                command=lambda: save_player(player[0]), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black",
                                font=("Helvetica", 25))

        def setpos():
            display_plus90["text"] = player[2]

        display_plus90.after(500, setpos)

        def setrat():
            display_plus90["text"] = player[1]

        display_plus90.after(1500, setrat)

        with open("packs.txt") as f:
            packsamt = f.read()
            newpack = f"{packsamt.split('-')[0]}-{packsamt.split('-')[1]}-{int(packsamt.split('-')[2]) - 1}-{packsamt.split('-')[3]}"
        with open("packs.txt", "w") as f:
            f.write(newpack)

        def revplayer():
            display_plus90.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_plus90.after(3000, revplayer)

    if option == "packs_pr":

        promo88 = [
            ['yakov_rb.png', '87', 'CB', '85000'],
            ['shoval_fba.png', '88', 'CM', '80000']
        ]
        promo89 = [
            ['bampi_rb.png', '89', 'LM', '70000'],
            ['shon_fba.png', '89', 'LW', '70000'],
            ['cohen.png', '89', 'GK', '40000'],
            ['bensi_ni.png', '89', 'CF', '100000']
        ]
        promo90 = [
            ['grine_fba.png', '90', 'CDM', '90000'],
            ['bensi_fba.png', '90', 'CAM', '120000'],
            ['morad_ni.png', '90', 'RM', '90000']
        ]
        promo96 = [
            ['yahez_yc.png', '96', 'CAM', '600000'],
            ['yakov_i.png', '96', 'CAM', '1100000'],
            ['yotam.png', '96', 'CM', '1100000'],
            ['rotem.png', '95', 'CF', '800000']
        ]

        chance = random.randint(1, 86)
        if chance >= 1 and chance < 43:
            player = random.choice(promo88)
        if chance >= 44 and chance < 67:
            player = random.choice(promo89)
        if chance >= 68 and chance < 79:
            player = random.choice(promo90)
        if chance >= 80 and chance < 85:
            player = random.choice(promo90)

        display_pr = Label(packanimation, text="", fg="white", bg="black", font=("Helvetica", 50))
        display_pr.place(x=320, y=500)
        playerimg_picture = PhotoImage(file=player[0])
        playerimg = Label(packanimation, image=playerimg_picture)
        sell_button_picture = PhotoImage(file='sell_btn.png')
        sell_button = Button(packanimation, image=sell_button_picture, borderwidth=0,
                                command=lambda: add_coins(player[3], '1'), highlightthickness=0)
        save_button_picture = PhotoImage(file='save_btn.png')
        save_button = Button(packanimation, image=save_button_picture, borderwidth=0,
                                command=lambda: save_player(player[0]), highlightthickness=0)
        valuedisplay = Label(packanimation, text=f"Value: {player[3]}", fg="white", bg="black",
                                font=("Helvetica", 25))

        def setpos():
            display_pr["text"] = player[2]

        display_pr.after(500, setpos)

        def setrat():
            display_pr["text"] = player[1]

        display_pr.after(1500, setrat)

        with open("packs.txt") as f:
            packsamt = f.read()
            newpack = f"{packsamt.split('-')[0]}-{packsamt.split('-')[1]}-{packsamt.split('-')[2]}-{int(packsamt.split('-')[3]) - 1}"
        with open("packs.txt", "w") as f:
            f.write(newpack)

        def revplayer():
            display_pr.destroy()
            playerimg.place(x=0, y=0, relwidth=1, relheight=1)

            sell_button.place(x=270, y=1000)
            save_button.place(x=270, y=1100)
            valuedisplay.place(x=290, y=45)

        display_pr.after(3000, revplayer)

    packanimation.mainloop()

def openpackanimation(option):
    try:
        packanimation.deiconify()
    except:
        pack_animation(option)

def mypacks_window():
    global mypackswin
    mypackswin = Toplevel()
    mypackswin.title('Hetnikfut | My Packs')
    mypackswin.iconbitmap(r'logo.ico')
    mypackswin.geometry("720x1280+30+30")
    mypackswin.resizable(False,False)

    background_img = PhotoImage(file='mypacks.png')
    background = Label(mypackswin, image=background_img)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(mypackswin, image=backtohome_button_picture,borderwidth=0, command=lambda: mypackswin.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    with open("coins.txt") as f:
        coinsamount = f.read()
    global coinsdisplay
    coinsdisplay = Label(mypackswin, text=coinsamount, fg="white", bg="black", font=("Helvetica", 25))
    coinsdisplay.place(x=300,y=45)

    pack_pic = PhotoImage(file='pack.png')


    with open("packs.txt") as f:
        packsamt = f.read()
        #sprint(packsamt)
    packs85 = packsamt.split('-')[0]
    packs87 = packsamt.split('-')[1]
    packs90 = packsamt.split('-')[2]
    packspr = packsamt.split('-')[3]

    #85s
    if packs85 == '1':
        pack_85_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_85"), highlightthickness=0)
        pack_85_1_button.place(x=217, y=276)

    if packs85 == '2':
        pack_85_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_85"), highlightthickness=0)
        pack_85_1_button.place(x=217, y=276)
        pack_85_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_85"), highlightthickness=0)
        pack_85_2_button.place(x=367, y=276)

    if packs85 == '3':
        pack_85_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_85"), highlightthickness=0)
        pack_85_1_button.place(x=215, y=276)
        pack_85_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_85"), highlightthickness=0)
        pack_85_2_button.place(x=367, y=276)
        pack_85_3_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_85"), highlightthickness=0)
        pack_85_3_button.place(x=520, y=276)

    #87s
    if packs87 == '1':
        pack_87_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_87"), highlightthickness=0)
        pack_87_1_button.place(x=217, y=476)

    if packs87 == '2':
        pack_87_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_87"), highlightthickness=0)
        pack_87_1_button.place(x=217, y=476)
        pack_87_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_87"), highlightthickness=0)
        pack_87_2_button.place(x=367, y=476)

    if packs87 == '3':
        pack_87_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_87"), highlightthickness=0)
        pack_87_1_button.place(x=215, y=476)
        pack_87_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_87"), highlightthickness=0)
        pack_87_2_button.place(x=367, y=476)
        pack_87_3_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_87"), highlightthickness=0)
        pack_87_3_button.place(x=520, y=476)

    #90s
    if packs90 == '1':
        pack_90_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_90"), highlightthickness=0)
        pack_90_1_button.place(x=217, y=685)

    if packs90 == '2':
        pack_90_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_90"), highlightthickness=0)
        pack_90_1_button.place(x=217, y=685)
        pack_90_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_90"), highlightthickness=0)
        pack_90_2_button.place(x=367, y=685)

    if packs90 == '3':
        pack_90_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_90"), highlightthickness=0)
        pack_90_1_button.place(x=215, y=685)
        pack_90_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_90"), highlightthickness=0)
        pack_90_2_button.place(x=367, y=685)
        pack_90_3_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_90"), highlightthickness=0)
        pack_90_3_button.place(x=520, y=685)

    #promos
    if packspr == '1':
        pack_pr_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_pr"), highlightthickness=0)
        pack_pr_1_button.place(x=217, y=965)

    if packspr == '2':
        pack_pr_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_pr"), highlightthickness=0)
        pack_pr_1_button.place(x=217, y=965)
        pack_pr_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_pr"), highlightthickness=0)
        pack_pr_2_button.place(x=367, y=965)

    if packspr == '3':
        pack_pr_1_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_pr"), highlightthickness=0)
        pack_pr_1_button.place(x=215, y=965)
        pack_pr_2_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_pr"), highlightthickness=0)
        pack_pr_2_button.place(x=367, y=965)
        pack_pr_3_button = Button(mypackswin, image=pack_pic, borderwidth=0,
                                   command=lambda: pack_animation("packs_pr"), highlightthickness=0)
        pack_pr_3_button.place(x=520, y=965)

    mypackswin.mainloop()

"""def sbc_window():
    sbcwindow = Toplevel()
    sbcwindow.title('Hetnikfut | Packs')
    sbcwindow.iconbitmap(r'logo.ico')
    sbcwindow.geometry("720x1280+30+30")
    sbcwindow.resizable(False,False)

    global sbc1_background_picture
    global sbc2_background_picture
    global sbc3_background_picture
    sbc1_background_picture = PhotoImage(file="sbc1.png")
    sbc2_background_picture = PhotoImage(file="sbc2.png")
    sbc3_background_picture = PhotoImage(file="sbc3.png")

    global sbc1_background
    sbc1_background = Label(sbcwindow, image=sbc1_background_picture)
    sbc1_background.place(x=0, y=0, relwidth=1, relheight=1)

    global goto_sbc3_button
    goto_sbc3_button_picture = PhotoImage(file='down2_btn.png')
    goto_sbc3_button = Button(sbcwindow, image=goto_sbc3_button_picture,borderwidth=0, command=sbc3_function, highlightthickness=0)

    global goto_sbc1_up_button
    goto_sbc1_up_button_picture = PhotoImage(file='up12_btn.png')
    goto_sbc1_up_button = Button(sbcwindow, image=goto_sbc1_up_button_picture,borderwidth=0, command=sbc2up_function, highlightthickness=0)

    global goto_sbc2_up_button
    goto_sbc2_up_button_picture = PhotoImage(file='up12_btn.png')
    goto_sbc2_up_button = Button(sbcwindow, image=goto_sbc2_up_button_picture,borderwidth=0, command=sbc3up_function, highlightthickness=0)

    goto_sbc2_button_picture = PhotoImage(file='down1_btn.png')
    global goto_sbc2_button
    goto_sbc2_button = Button(sbcwindow, image=goto_sbc2_button_picture,borderwidth=0, command=sbc2_function, highlightthickness=0)
    goto_sbc2_button.place(x=260, y=990)

    sbcwindow.mainloop()"""

def sbc1_window():
    try:
        sbcwindow2.destroy()
        sbcwindow3.destroy()
    except:
        pass
    global sbcwindow1
    sbcwindow1 = Toplevel()
    sbcwindow1.title('Hetnikfut | OBJ')
    sbcwindow1.iconbitmap(r'logo.ico')
    sbcwindow1.geometry("720x1280+30+30")
    sbcwindow1.resizable(False,False)

    sbc1_background_picture = PhotoImage(file="sbc1.png")
    sbc1_background = Label(sbcwindow1, image=sbc1_background_picture)
    sbc1_background.place(x=0, y=0, relwidth=1, relheight=1)

    goto_sbc2_button_picture = PhotoImage(file='down1_btn.png')
    goto_sbc2_button = Button(sbcwindow1, image=goto_sbc2_button_picture,borderwidth=0,command=sbc2_window, highlightthickness=0)
    goto_sbc2_button.place(x=260, y=990)

    fbmishuk_button_picture = PhotoImage(file='fbmishuk_btn.png')
    fbmishuk_button = Button(sbcwindow1, image=fbmishuk_button_picture,borderwidth=0, command=lambda: sbccomplete('mishuk'), highlightthickness=0)
    fbmishuk_button.place(x=35, y=250)

    fbyahez_button_picture = PhotoImage(file='fbyahez_btn.png')
    fbyahez_button = Button(sbcwindow1, image=fbyahez_button_picture,borderwidth=0, command=lambda: sbccomplete('yahez'), highlightthickness=0)
    fbyahez_button.place(x=35, y=500)

    fbyanch_button_picture = PhotoImage(file='fbyanch_btn.png')
    fbyanch_button = Button(sbcwindow1, image=fbyanch_button_picture,borderwidth=0, command=lambda: sbccomplete('yanch'), highlightthickness=0)
    fbyanch_button.place(x=35, y=730)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(sbcwindow1, image=backtohome_button_picture,borderwidth=0, command=lambda: sbcwindow1.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    sbcwindow1.mainloop()

def sbc2_window():
    try:
        sbcwindow1.destroy()
        sbcwindow3.destroy()
    except:
        pass
    global sbcwindow2
    sbcwindow2 = Toplevel()
    sbcwindow2.title('Hetnikfut | OBJ')
    sbcwindow2.iconbitmap(r'logo.ico')
    sbcwindow2.geometry("720x1280+30+30")
    sbcwindow2.resizable(False,False)

    sbc2_background_picture = PhotoImage(file="sbc2.png")
    sbc2_background = Label(sbcwindow2, image=sbc2_background_picture)
    sbc2_background.place(x=0, y=0, relwidth=1, relheight=1)

    goto_sbc1up_button_picture = PhotoImage(file='up12_btn.png')
    goto_sbc1up_button = Button(sbcwindow2, image=goto_sbc1up_button_picture, borderwidth=0, command=sbc1_window, highlightthickness=0)
    goto_sbc1up_button.place(x=260, y=260)

    hmyahez_button_picture = PhotoImage(file='hmyahez_btn.png')
    hmyahez_button = Button(sbcwindow2, image=hmyahez_button_picture,borderwidth=0, command=lambda: sbccomplete('hmyahez'), highlightthickness=0)
    hmyahez_button.place(x=35, y=380)

    upg90_button_picture = PhotoImage(file='90upg_btn.png')
    upg90_button = Button(sbcwindow2, image=upg90_button_picture,borderwidth=0, command=lambda: sbccomplete('90upg'), highlightthickness=0)
    upg90_button.place(x=35, y=620)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(sbcwindow2, image=backtohome_button_picture,borderwidth=0, command=lambda: sbcwindow2.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    sbcwindow1.mainloop()



def sbccomplete(option):
    mishukwindow = Toplevel()
    mishukwindow.title('Hetnikfut | OBJ')
    mishukwindow.iconbitmap(r'logo.ico')
    mishukwindow.geometry("720x1280+30+30")
    mishukwindow.resizable(False,False)

    game_background_picture = PhotoImage(file="back.png")
    game_background = Label(mishukwindow, image=game_background_picture)
    game_background.place(x=0, y=0, relwidth=1, relheight=1)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(mishukwindow, image=backtohome_button_picture,borderwidth=0, command=lambda: mishukwindow.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    claimrewards_button_picture = PhotoImage(file='claimrewards_btn.png')

    if option == 'mishuk':
        goals = checkstats('goals')
        text_show = Label(mishukwindow, text=f"Yonatan Mishuk FB", fg="white", bg="black", font=("Helvetica", 35))
        text_show.place(x=155, y=100)
        stats_show = Label(mishukwindow, text=f"Goals Scored: {goals}/100", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=230, y=600)

        mishuk_picture = PhotoImage(file="mishuk_pick.png")
        mishuk_picture_bck = Label(mishukwindow, image=mishuk_picture, bd= 0)
        mishuk_picture_bck.place(x=60, y=150)

        claimrewards_button = Button(mishukwindow, image=claimrewards_button_picture, borderwidth=0, command=lambda: claimsbc('mishuk', goals), highlightthickness=0)
        claimrewards_button.place(x=270, y=700)

    if option == 'yahez':
        goals = checkstats('wins')
        text_show = Label(mishukwindow, text=f"Ethan Yahez FB", fg="white", bg="black", font=("Helvetica", 35))
        text_show.place(x=200, y=100)
        stats_show = Label(mishukwindow, text=f"Games Won: {goals}/250", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=210, y=600)

        yahez_picture = PhotoImage(file="yahez_pick.png")
        yahez_picture_bck = Label(mishukwindow, image=yahez_picture, bd= 0)
        yahez_picture_bck.place(x=63, y=200)

        claimrewards_button = Button(mishukwindow, image=claimrewards_button_picture, borderwidth=0, command=lambda: claimsbc('yahez', goals), highlightthickness=0)
        claimrewards_button.place(x=270, y=700)

    if option == 'yanch':
        goals = checkstats('goals')
        text_show = Label(mishukwindow, text=f"Yanchevsky FB", fg="white", bg="black", font=("Helvetica", 35))
        text_show.place(x=200, y=100)
        stats_show = Label(mishukwindow, text=f"Goals Scored: {goals}/250", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=210, y=600)

        yanch_picture = PhotoImage(file="yanch_pick.png")
        yanch_picture_bck = Label(mishukwindow, image=yanch_picture, bd= 0)
        yanch_picture_bck.place(x=63, y=200)

        claimrewards_button = Button(mishukwindow, image=claimrewards_button_picture, borderwidth=0, command=lambda: claimsbc('yanch', goals), highlightthickness=0)
        claimrewards_button.place(x=270, y=700)

    if option == 'hmyahez':
        goals = checkstats('wins')
        text_show = Label(mishukwindow, text=f"Ethan Yahez HM", fg="white", bg="black", font=("Helvetica", 35))
        text_show.place(x=190, y=100)
        stats_show = Label(mishukwindow, text=f"Games Won: {goals}/75", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=230, y=600)

        hmyahez_picture = PhotoImage(file="hmyahez_pick.png")
        hmyahez_picture_bck = Label(mishukwindow, image=hmyahez_picture, bd= 0)
        hmyahez_picture_bck.place(x=63, y=200)

        claimrewards_button = Button(mishukwindow, image=claimrewards_button_picture, borderwidth=0, command=lambda: claimsbc('hmyahez ', goals), highlightthickness=0)
        claimrewards_button.place(x=270, y=700)

    if option == '90upg':
        goals = checkstats('wins')
        text_show = Label(mishukwindow, text=f"90+ Pack Upgrade", fg="white", bg="black", font=("Helvetica", 35))
        text_show.place(x=160, y=100)
        stats_show = Label(mishukwindow, text=f"Games Won: {goals}/25", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=240, y=600)

        upg90_picture = PhotoImage(file="90upg.png")
        upg90_picture_bck = Label(mishukwindow, image=upg90_picture, bd= 0)
        upg90_picture_bck.place(x=63, y=200)

        claimrewards_button = Button(mishukwindow, image=claimrewards_button_picture, borderwidth=0, command=lambda: playgamerewards('won', homegoals - awaygoals), highlightthickness=0)
        claimrewards_button.place(x=270, y=700)

    mishukwindow.mainloop()

def claimsbc(option, stat):
    if option == 'mishuk':
        if stat < 100:
            return
        else:
            with open("rep.txt") as f:
                text = f.read()
                text1 = text.split("-")[0]
                text2 = text.split("-")[1]
                text3 = text.split("-")[2]
                text4 = text.split("-")[3]
                f.close()

                if text1 == '1':
                    return
                else:
                    with open("rep.txt", "w") as f:
                        text = f"1-{text2}-{text3}-{text4}"
                        f.write(text)
                        f.close()
                        sbcplayerpick('mishuk')

    if option == 'yahez':
        if stat < 250:
            return
        else:
            with open("rep.txt") as f:
                text = f.read()
                text1 = text.split("-")[0]
                text2 = text.split("-")[1]
                text3 = text.split("-")[2]
                text4 = text.split("-")[3]
                f.close()

                if text2 == '1':
                    return
                else:
                    with open("rep.txt", "w") as f:
                        text = f"{text1}-1-{text3}-{text4}"
                        f.write(text)
                        f.close()
                        sbcplayerpick('yahez')

    if option == 'yanch':
        if stat < 250:
            return
        else:
            with open("rep.txt") as f:
                text = f.read()
                text1 = text.split("-")[0]
                text2 = text.split("-")[1]
                text3 = text.split("-")[2]
                text4 = text.split("-")[3]
                f.close()

                if text3 == '1':
                    return
                else:
                    with open("rep.txt", "w") as f:
                        text = f"{text1}-{text2}-1-{text4}"
                        f.write(text)
                        f.close()
                        sbcplayerpick('yanch')

    if option == 'hmyahez':
        if stat < 75:
            return
        else:
            with open("rep.txt") as f:
                text = f.read()
                text1 = text.split("-")[0]
                text2 = text.split("-")[1]
                text3 = text.split("-")[2]
                text4 = text.split("-")[3]
                f.close()

                if text4 == '1':
                    return
                else:
                    with open("rep.txt", "w") as f:
                        text = f"{text1}-{text2}-{text3}-1"
                        f.write(text)
                        f.close()
                        save_player('yahez_hm.png')

    if option == '90upg':
        if stat % 10:
            addpack('90')
        else:
            return

def sbcplayerpick(option):
    global ppwindow
    ppwindow = Toplevel()
    ppwindow.title('Hetnikfut | Player Pick')
    ppwindow.iconbitmap(r'logo.ico')
    ppwindow.geometry("720x1280+30+30")
    ppwindow.resizable(False,False)

    game_background_picture = PhotoImage(file="back.png")
    game_background = Label(ppwindow, image=game_background_picture)
    game_background.place(x=0, y=0, relwidth=1, relheight=1)

    if option == 'mishuk':
        stats_show = Label(ppwindow, text=f"Choose your player", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=220, y=200)

        mishukcb_picture = PhotoImage(file='mishuk_cb_black.png')
        mishukcb = Button(ppwindow, image=mishukcb_picture, borderwidth=0, command=lambda: sbcaddplayer("mishuk_cb_black.png"), highlightthickness=0)
        mishukcb.place(x=150, y=300)

        mishukst_picture = PhotoImage(file='mishuk_st_black.png')
        mishukst = Button(ppwindow, image=mishukst_picture, borderwidth=0, command=lambda: sbcaddplayer("mishuk_st_black.png"), highlightthickness=0)
        mishukst.place(x=400, y=300)

    if option == 'yahez':
        stats_show = Label(ppwindow, text=f"Choose your player", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=220, y=200)

        yahezcdm_picture = PhotoImage(file='yahezcdm_black.png')
        yahezcdm = Button(ppwindow, image=yahezcdm_picture, borderwidth=0, command=lambda: sbcaddplayer("yahezcdm_black.png"), highlightthickness=0)
        yahezcdm.place(x=150, y=300)

        yahezcf_picture = PhotoImage(file='yahez_cf_black.png')
        yahezcf = Button(ppwindow, image=yahezcf_picture, borderwidth=0, command=lambda: sbcaddplayer("yahez_cf_black.png"), highlightthickness=0)
        yahezcf.place(x=400, y=300)

    if option == 'yanch':
        stats_show = Label(ppwindow, text=f"Choose your player", fg="white", bg="black", font=("Helvetica", 25))
        stats_show.place(x=220, y=200)

        yanchcdm_picture = PhotoImage(file='yanchevskycdm_black.png')
        yanchcdm = Button(ppwindow, image=yanchcdm_picture, borderwidth=0, command=lambda: sbcaddplayer("yanchevskycdm_black.png"), highlightthickness=0)
        yanchcdm.place(x=150, y=300)

        yanchcb_picture = PhotoImage(file='yanchevsky_cb_black.png')
        yanchcb = Button(ppwindow, image=yanchcb_picture, borderwidth=0, command=lambda: sbcaddplayer("yanchevsky_cb_black.png"), highlightthickness=0)
        yanchcb.place(x=400, y=300)

    ppwindow.mainloop()

def sbcaddplayer(player):
    add_player(player)
    ppwinndow.destroy()

def playersbcpick(option):
    global playersbcpickwindow
    playersbcpickwindow = Toplevel()
    playersbcpickwindow.title('Hetnikfut | Player Pick')
    playersbcpickwindow.iconbitmap(r'logo.ico')
    playersbcpickwindow.geometry("720x1280+30+30")
    playersbcpickwindow.resizable(False,False)

    playersbcpick_background_picture = PhotoImage(file="back.png")
    playersbcpick_background = Label(playersbcpickwindow, image=playersbcpick_background_picture)
    playersbcpick_background.place(x=0, y=0, relwidth=1, relheight=1)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(playersbcpickwindow, image=backtohome_button_picture,borderwidth=0, command=lambda: playersbcpickwindow.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    if option == 'gk':
        mandelbtn_pic = PhotoImage(file='mandel_black.png')
        mandelbtn = Button(playersbcpickwindow, image=mandelbtn_pic, highlightthickness=0, command=lambda: setteamplayer("gk", 'mandel_black.png', '86'))
        cohenbtn_pic = PhotoImage(file='cohen_black.png')
        cohenbtn = Button(playersbcpickwindow, image=cohenbtn_pic, highlightthickness=0, command=lambda: setteamplayer("gk", 'cohen_black.png', '89'))
        cohenycbtn_pic = PhotoImage(file='cohenyc_black.png')
        cohenycbtn = Button(playersbcpickwindow, image=cohenycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("gk", 'cohenyc_black.png', '90'))
        with open("cards.txt") as f:
            if 'mandel.png' in f.read():
                mandelbtn.place(x=140, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'cohen.png' in f.read():
                cohenbtn.place(x=300, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'cohen_yc.png' in f.read():
                cohenycbtn.place(x=460, y=100)
                f.close()

    if option == 'cb1':
        yanchevskyycbtn_pic = PhotoImage(file='yanchevsky_yc_black.png')
        yanchevskyycbtn = Button(playersbcpickwindow, image=yanchevskyycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'yanchevsky_yc_black.png', '89'))
        yakovrbbtn_pic = PhotoImage(file='yakov_rb_black.png')
        yakovrbbtn = Button(playersbcpickwindow, image=yakovrbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'yakov_rb_black.png', '87'))
        avihaibtn_pic = PhotoImage(file='avihai_black.png')
        avihaibtn = Button(playersbcpickwindow, image=avihaibtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'avihai_black.png', '86'))
        yanchevskybtn_pic = PhotoImage(file='yanchevsky_black.png')
        yanchevskybtn = Button(playersbcpickwindow, image=yanchevskybtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'yanchevsky_black.png', '87'))
        yakovbtn_pic = PhotoImage(file='yakov_black.png')
        yakovbtn = Button(playersbcpickwindow, image=yakovbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'yakov_black.png', '86'))
        mishukbtn_pic = PhotoImage(file='mishuk_black.png')
        mishukbtn = Button(playersbcpickwindow, image=mishukbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'mishuk_black.png', '84'))
        yanchevskycbbtn_pic = PhotoImage(file='yanchevsky_cb_black.png')
        yanchevskycbbtn = Button(playersbcpickwindow, image=yanchevskycbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'yanchevsky_cb_black.png', '88'))
        mishukcbbtn_pic = PhotoImage(file='mishuk_cb_black.png')
        mishukcbbtn = Button(playersbcpickwindow, image=mishukcbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb1", 'mishuk_cb_black.png', '85'))

        with open("cards.txt") as f:
            if 'yanchevsky_yc.png' in f.read():
                yanchevskyycbtn.place(x=70, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'yakov_rb.png' in f.read():
                yakovrbbtn.place(x=220, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'avihai.png' in f.read():
                avihaibtn.place(x=370, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'yanchevsky.png' in f.read():
                yanchevskybtn.place(x=520, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'yakov.png' in f.read():
                yakovbtn.place(x=70, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'mishuk.png' in f.read():
                mishukbtn.place(x=220, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'yanchevsky_cb_fb.png' in f.read():
                yanchevskycbbtn.place(x=370, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'mishuk_cb_fb.png' in f.read():
                mishukcbbtn.place(x=520, y=280)
                f.close()


    if option == 'cb2':
        yanchevskyycbtn_pic = PhotoImage(file='yanchevsky_yc_black.png')
        yanchevskyycbtn = Button(playersbcpickwindow, image=yanchevskyycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'yanchevsky_yc_black.png', '89'))
        yakovrbbtn_pic = PhotoImage(file='yakov_rb_black.png')
        yakovrbbtn = Button(playersbcpickwindow, image=yakovrbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'yakov_rb_black.png', '87'))
        avihaibtn_pic = PhotoImage(file='avihai_black.png')
        avihaibtn = Button(playersbcpickwindow, image=avihaibtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'avihai_black.png', '86'))
        yanchevskybtn_pic = PhotoImage(file='yanchevsky_black.png')
        yanchevskybtn = Button(playersbcpickwindow, image=yanchevskybtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'yanchevsky_black.png', '87'))
        yakovbtn_pic = PhotoImage(file='yakov_black.png')
        yakovbtn = Button(playersbcpickwindow, image=yakovbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'yakov_black.png', '86'))
        mishukbtn_pic = PhotoImage(file='mishuk_black.png')
        mishukbtn = Button(playersbcpickwindow, image=mishukbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'mishuk_black.png', '84'))
        yanchevskycbbtn_pic = PhotoImage(file='yanchevsky_cb_black.png')
        yanchevskycbbtn = Button(playersbcpickwindow, image=yanchevskycbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'yanchevsky_cb_black.png', '88'))
        mishukcbbtn_pic = PhotoImage(file='mishuk_cb_black.png')
        mishukcbbtn = Button(playersbcpickwindow, image=mishukcbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cb2", 'mishuk_cb_black.png', '85'))

        with open("cards.txt") as f:
            if 'yanchevsky_yc.png' in f.read():
                yanchevskyycbtn.place(x=70, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'yakov_rb.png' in f.read():
                yakovrbbtn.place(x=220, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'avihai.png' in f.read():
                avihaibtn.place(x=370, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'yanchevsky.png' in f.read():
                yanchevskybtn.place(x=520, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'yakov.png' in f.read():
                yakovbtn.place(x=70, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'mishuk.png' in f.read():
                mishukbtn.place(x=220, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'yanchevsky_cb_fb.png' in f.read():
                yanchevskycbbtn.place(x=370, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'mishuk_cb_fb.png' in f.read():
                mishukcbbtn.place(x=520, y=280)
                f.close()

    if option == 'cm':
        yahezycbtn_pic = PhotoImage(file='yahezyc_black.png')
        yahezycbtn = Button(playersbcpickwindow, image=yahezycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'yahezyc_black.png', '96'))
        isarycbtn_pic = PhotoImage(file='isaryc_black.png')
        isarycbtn = Button(playersbcpickwindow, image=isarycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'isaryc_black.png', '86'))
        bampirbbtn_pic = PhotoImage(file='bampirb_black.png')
        bampirbbtn = Button(playersbcpickwindow, image=bampirbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'bampirb_black.png', '89'))
        moradnibtn_pic = PhotoImage(file='moradni_black.png')
        moradnibtn = Button(playersbcpickwindow, image=moradnibtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'moradni_black.png', '90'))
        yotambtn_pic = PhotoImage(file='yotam_black.png')
        yotambtn = Button(playersbcpickwindow, image=yotambtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'yotam_black.png', '96'))
        yakovibtn_pic = PhotoImage(file='yakovi_black.png')
        yakovibtn = Button(playersbcpickwindow, image=yakovibtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'yakovi_black.png', '96'))
        yahezhmbtn_pic = PhotoImage(file='yahezhm_black.png')
        yahezhmbtn = Button(playersbcpickwindow, image=yahezhmbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'yahezhm_black.png', '88'))
        yahezbtn_pic = PhotoImage(file='yahez_black.png')
        yahezbtn = Button(playersbcpickwindow, image=yahezbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'yahez_black.png', '94'))
        shovalbtn_pic = PhotoImage(file='shoval_black.png')
        shovalbtn = Button(playersbcpickwindow, image=shovalbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'shoval_black.png', '87'))
        shonbtn_pic = PhotoImage(file='shon_black.png')
        shonbtn = Button(playersbcpickwindow, image=shonbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'shon_black.png', '88'))
        moradbtn_pic = PhotoImage(file='morad_black.png')
        moradbtn = Button(playersbcpickwindow, image=moradbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'morad_black.png', '89'))
        isarbtn_pic = PhotoImage(file='isar_black.png')
        isarbtn = Button(playersbcpickwindow, image=isarbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'isar_black.png', '84'))
        bampibtn_pic = PhotoImage(file='bampi_black.png')
        bampibtn = Button(playersbcpickwindow, image=bampibtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'bampi_black.png', '88'))
        grinebtn_pic = PhotoImage(file='grine_black.png')
        grinebtn = Button(playersbcpickwindow, image=grinebtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'grine_black.png', '89'))
        bensibtn_pic = PhotoImage(file='bensi_black.png')
        bensibtn = Button(playersbcpickwindow, image=bensibtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'bensi_black.png', '88'))
        yanchevskycdmbtn_pic = PhotoImage(file='yanchevskycdm_black.png')
        yanchevskycdmbtn = Button(playersbcpickwindow, image=yanchevskycdmbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'yanchevskycdm_black.png', '88'))
        yahezcdmbtn_pic = PhotoImage(file='yahezcdm_black.png')
        yahezcdmbtn = Button(playersbcpickwindow, image=yahezcdmbtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'yahezcdm_black.png', '95'))
        shovalfbabtn_pic = PhotoImage(file='shovalfba_black.png')
        shovalfbabtn = Button(playersbcpickwindow, image=shovalfbabtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'shovalfba_black.png', '88'))
        grinefbabtn_pic = PhotoImage(file='grinefba_black.png')
        grinefbabtn = Button(playersbcpickwindow, image=grinefbabtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'grinefba_black.png', '90'))
        bensifbabtn_pic = PhotoImage(file='bensifba_black.png')
        bensifbabtn = Button(playersbcpickwindow, image=bensifbabtn_pic, highlightthickness=0, command=lambda: setteamplayer("cm", 'bensifba_black.png', '90'))

        with open("cards.txt") as f:
            if 'yahez_yc.png' in f.read():
                yahezycbtn.place(x=70, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'isar_yc.png' in f.read():
                isarycbtn.place(x=220, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'bampi_rb.png' in f.read():
                bampirbbtn.place(x=370, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'morad_ni.png' in f.read():
                moradnibtn.place(x=520, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'yotam.png' in f.read():
                yotambtn.place(x=70, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'yakov_i.png' in f.read():
                yakovibtn.place(x=220, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'yahez_hm.png' in f.read():
                yahezhmbtn.place(x=370, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'yahez.png' in f.read():
                yahezbtn.place(x=520, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'shoval.png' in f.read():
                shovalbtn.place(x=70, y=460)
                f.close()
        with open("cards.txt") as f:
            if 'shon.png' in f.read():
                shonbtn.place(x=220, y=460)
                f.close()
        with open("cards.txt") as f:
            if 'morad.png' in f.read():
                moradbtn.place(x=370, y=460)
                f.close()
        with open("cards.txt") as f:
            if 'isar.png' in f.read():
                isarbtn.place(x=520, y=460)
                f.close()
        with open("cards.txt") as f:
            if 'bampi.png' in f.read():
                bampibtn.place(x=70, y=640)
                f.close()
        with open("cards.txt") as f:
            if 'grine.png' in f.read():
                grinebtn.place(x=220, y=640)
                f.close()
        with open("cards.txt") as f:
            if 'bensi.png' in f.read():
                bensibtn.place(x=370, y=640)
                f.close()
        with open("cards.txt") as f:
            if 'yanchevskycdm_fb.png' in f.read():
                yanchevskycdmbtn.place(x=520, y=640)
                f.close()
        with open("cards.txt") as f:
            if 'yahezcdm_fb.png' in f.read():
                yahezcdmbtn.place(x=70, y=820)
                f.close()
        with open("cards.txt") as f:
            if 'shoval_fba.png' in f.read():
                shovalfbabtn.place(x=220, y=820)
                f.close()
        with open("cards.txt") as f:
            if 'grine_fba.png' in f.read():
                grinefbabtn.place(x=370, y=820)
                f.close()
        with open("cards.txt") as f:
            if 'bensi_fba.png' in f.read():
                bensifbabtn.place(x=520, y=820)
                f.close()

    if option == 'st1':
        shonycbtn_pic = PhotoImage(file='shon_yc_black.png')
        shonycbtn = Button(playersbcpickwindow, image=shonycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'shon_yc_black.png', '91'))
        bensiycbtn_pic = PhotoImage(file='bensi_yc_black.png')
        bensiycbtn = Button(playersbcpickwindow, image=bensiycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'bensi_yc_black.png', '91'))
        ulitskyrbbtn_pic = PhotoImage(file='ulitsky_rb_black.png')
        ulitskyrbbtn = Button(playersbcpickwindow, image=ulitskyrbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'ulitsky_rb_black.png', '85'))
        bensinibtn_pic = PhotoImage(file='bensi_ni_black.png')
        bensinibtn = Button(playersbcpickwindow, image=bensinibtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'bensi_ni_black.png', '89'))
        rotembtn_pic = PhotoImage(file='rotem_black.png')
        rotembtn = Button(playersbcpickwindow, image=rotembtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'rotem_black.png', '85'))
        ulitskybtn_pic = PhotoImage(file='ulitsky_black.png')
        ulitskybtn = Button(playersbcpickwindow, image=ulitskybtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'ulitsky_black.png', '84'))
        shtaifbtn_pic = PhotoImage(file='shtaif_black.png')
        shtaifbtn = Button(playersbcpickwindow, image=shtaifbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'shtaif_black.png', '83'))
        mishukstbtn_pic = PhotoImage(file='mishuk_st_black.png')
        mishukstbtn = Button(playersbcpickwindow, image=mishukstbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'mishuk_st_black.png', '85s'))
        yahezcfbtn_pic = PhotoImage(file='yahez_cf_black.png')
        yahezcfbtn = Button(playersbcpickwindow, image=yahezcfbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'yahez_cf_black.png', '95'))
        shonfbabtn_pic = PhotoImage(file='shon_fba_black.png')
        shonfbabtn = Button(playersbcpickwindow, image=shonfbabtn_pic, highlightthickness=0, command=lambda: setteamplayer("st1", 'shon_fba_black.png', '89'))

        with open("cards.txt") as f:
            if 'shon_yc.png' in f.read():
                shonycbtn.place(x=70, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'bensi_yc.png' in f.read():
                bensiycbtn.place(x=220, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'ulistky_rb.png' in f.read():
                ulitskyrbbtn.place(x=370, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'bensi_ni.png' in f.read():
                bensinibtn.place(x=520, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'rotem.png' in f.read():
                rotembtn.place(x=70, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'ulitsky.png' in f.read():
                ulitskybtn.place(x=220, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'shtaif.png' in f.read():
                shtaifbtn.place(x=370, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'mishuk_st.png' in f.read():
                mishukstbtn.place(x=520, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'yahez_cf.png' in f.read():
                yahezcfbtn.place(x=70, y=460)
                f.close()
        with open("cards.txt") as f:
            if 'shon_fba.png' in f.read():
                shonfbabtn.place(x=220, y=460)
                f.close()

    if option == 'st2':
        shonycbtn_pic = PhotoImage(file='shon_yc_black.png')
        shonycbtn = Button(playersbcpickwindow, image=shonycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'shon_yc_black.png', '91'))
        bensiycbtn_pic = PhotoImage(file='bensi_yc_black.png')
        bensiycbtn = Button(playersbcpickwindow, image=bensiycbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'bensi_yc_black.png', '91'))
        ulitskyrbbtn_pic = PhotoImage(file='ulitsky_rb_black.png')
        ulitskyrbbtn = Button(playersbcpickwindow, image=ulitskyrbbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'ulitsky_rb_black.png', '85'))
        bensinibtn_pic = PhotoImage(file='bensi_ni_black.png')
        bensinibtn = Button(playersbcpickwindow, image=bensinibtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'bensi_ni_black.png', '89'))
        rotembtn_pic = PhotoImage(file='rotem_black.png')
        rotembtn = Button(playersbcpickwindow, image=rotembtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'rotem_black.png', '85'))
        ulitskybtn_pic = PhotoImage(file='ulitsky_black.png')
        ulitskybtn = Button(playersbcpickwindow, image=ulitskybtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'ulitsky_black.png', '84'))
        shtaifbtn_pic = PhotoImage(file='shtaif_black.png')
        shtaifbtn = Button(playersbcpickwindow, image=shtaifbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'shtaif_black.png', '83'))
        mishukstbtn_pic = PhotoImage(file='mishuk_st_black.png')
        mishukstbtn = Button(playersbcpickwindow, image=mishukstbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'mishuk_st_black.png', '85s'))
        yahezcfbtn_pic = PhotoImage(file='yahez_cf_black.png')
        yahezcfbtn = Button(playersbcpickwindow, image=yahezcfbtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'yahez_cf_black.png', '95'))
        shonfbabtn_pic = PhotoImage(file='shon_fba_black.png')
        shonfbabtn = Button(playersbcpickwindow, image=shonfbabtn_pic, highlightthickness=0, command=lambda: setteamplayer("st2", 'shon_fba_black.png', '89'))

        with open("cards.txt") as f:
            if 'shon_yc.png' in f.read():
                shonycbtn.place(x=70, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'bensi_yc.png' in f.read():
                bensiycbtn.place(x=220, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'ulitsky_rb.png' in f.read():
                ulitskyrbbtn.place(x=370, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'bensi_ni.png' in f.read():
                bensinibtn.place(x=520, y=100)
                f.close()
        with open("cards.txt") as f:
            if 'rotem.png' in f.read():
                rotembtn.place(x=70, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'ulitsky.png' in f.read():
                ulitskybtn.place(x=220, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'shtaif.png' in f.read():
                shtaifbtn.place(x=370, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'mishuk_st.png' in f.read():
                mishukstbtn.place(x=520, y=280)
                f.close()
        with open("cards.txt") as f:
            if 'yahez_cf.png' in f.read():
                yahezcfbtn.place(x=70, y=460)
                f.close()
        with open("cards.txt") as f:
            if 'shon_fba.png' in f.read():
                shonfbabtn.place(x=220, y=460)
                f.close()

    playersbcpickwindow.mainloop()

def squadordraft(option):
    global squadordraftwindow
    squadordraftwindow = Toplevel()
    squadordraftwindow.title('Hetnikfut | TEAM')
    squadordraftwindow.iconbitmap(r'logo.ico')
    squadordraftwindow.geometry("720x1280+30+30")
    squadordraftwindow.resizable(False,False)

    field_background_picture = PhotoImage(file="teamdraft.png")
    field_background = Label(squadordraftwindow, image=field_background_picture)
    field_background.place(x=0, y=0, relwidth=1, relheight=1)

    #playerhole_button_picture = PhotoImage(file='black_btn.png')

    squad_button_picture = PhotoImage(file='squad_btn.png')
    squad_button = Button(squadordraftwindow, image=squad_button_picture,borderwidth=0, command=squad_window, highlightthickness=0)
    squad_button.place(x=31, y=220)

    draft_button_picture = PhotoImage(file='draft_btn.png')
    draft_button = Button(squadordraftwindow, image=draft_button_picture,borderwidth=0, command=draft_window, highlightthickness=0)
    draft_button.place(x=31, y=535)

    ##playerhole_gk_button = Button(squadordraftwindow, image= playerhole_button_picture,borderwidth=0, command=lambda: playersbcpick('gk'), highlightthickness=0)
    #playerhole_gk_button.place(x=296, y=834)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(squadordraftwindow, image=backtohome_button_picture,borderwidth=0, command=lambda: squadordraftwindow.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)


    squadordraftwindow.mainloop()

def squad_window():
    squadordraftwindow.destroy()
    squadwindow = Toplevel()
    squadwindow.title('Hetnikfut | SQUAD')
    squadwindow.iconbitmap(r'logo.ico')
    squadwindow.geometry("720x1280+30+30")
    squadwindow.resizable(False,False)

    field_background_picture = PhotoImage(file="field.png")
    field_background = Label(squadwindow, image=field_background_picture)
    field_background.place(x=0, y=0, relwidth=1, relheight=1)

    global midrating_show
    midrating_show = Label(squadwindow, text=f"Rating: 0", fg="white", bg="black", font=("Helvetica", 25))
    midrating_show.place(x=100, y=100)
    squadrating()

    global playerholegk_button_picture
    if os.path.getsize("sqd_gk.txt") > 0:
        with open("sqd_gk.txt") as f:
            playerholegk_button_picture = PhotoImage(file=f.read().split("-n-")[0])
    if os.path.getsize("sqd_gk.txt") == 0:
        playerholegk_button_picture = PhotoImage(file='black_btn.png')
    playerhole_gk_button = Button(squadwindow, image=playerholegk_button_picture,borderwidth=0, command=lambda: playersbcpick('gk'), highlightthickness=0)
    playerhole_gk_button.place(x=296, y=834)

    global playerholecb1_button_picture
    if os.path.getsize("sqd_cb1.txt") > 0:
        with open("sqd_cb1.txt") as f:
            playerholecb1_button_picture = PhotoImage(file=f.read().split("-n-")[0])
    if os.path.getsize("sqd_cb1.txt") == 0:
        playerholecb1_button_picture = PhotoImage(file='black_btn.png')
    playerhole_cb1_button = Button(squadwindow, image=playerholecb1_button_picture,borderwidth=0, command=lambda: playersbcpick('cb1'), highlightthickness=0)
    playerhole_cb1_button.place(x=135, y=659)

    global playerholecb2_button_picture
    if os.path.getsize("sqd_cb2.txt") > 0:
        with open("sqd_cb2.txt") as f:
            playerholecb2_button_picture = PhotoImage(file=f.read().split("-n-")[0])
    if os.path.getsize("sqd_cb2.txt") == 0:
        playerholecb2_button_picture = PhotoImage(file='black_btn.png')
    playerhole_cb2_button = Button(squadwindow, image=playerholecb2_button_picture,borderwidth=0, command=lambda: playersbcpick('cb2'), highlightthickness=0)
    playerhole_cb2_button.place(x=455, y=660)

    global playerholecm_button_picture
    if os.path.getsize("sqd_cm.txt") > 0:
        with open("sqd_cm.txt") as f:
            playerholecm_button_picture = PhotoImage(file=f.read().split("-n-")[0])
    if os.path.getsize("sqd_cm.txt") == 0:
        playerholecm_button_picture = PhotoImage(file='black_btn.png')
    playerhole_cm_button = Button(squadwindow, image=playerholecm_button_picture,borderwidth=0, command=lambda: playersbcpick('cm'), highlightthickness=0)
    playerhole_cm_button.place(x=299, y=455)

    global playerholest1_button_picture
    if os.path.getsize("sqd_st1.txt") > 0:
        with open("sqd_st1.txt") as f:
            playerholest1_button_picture = PhotoImage(file=f.read().split("-n-")[0])
    if os.path.getsize("sqd_st1.txt") == 0:
        playerholest1_button_picture = PhotoImage(file='black_btn.png')
    playerhole_st1_button = Button(squadwindow, image=playerholest1_button_picture,borderwidth=0, command=lambda: playersbcpick('st1'), highlightthickness=0)
    playerhole_st1_button.place(x=110, y=267)

    global playerholest2_button_picture
    if os.path.getsize("sqd_st2.txt") > 0:
        with open("sqd_st2.txt") as f:
            playerholest2_button_picture = PhotoImage(file=f.read().split("-n-")[0])
    if os.path.getsize("sqd_st2.txt") == 0:
        playerholest2_button_picture = PhotoImage(file='black_btn.png')
    playerhole_st2_button = Button(squadwindow, image=playerholest2_button_picture,borderwidth=0, command=lambda: playersbcpick('st2'), highlightthickness=0)
    playerhole_st2_button.place(x=474, y=267)

    play_button_picture = PhotoImage(file='play_btn.png')
    play_button = Button(squadwindow, image=play_button_picture,borderwidth=0, command=lambda: playgame1_window('lvl1', 'squad'), highlightthickness=0)
    play_button.place(x=270, y=1050)

    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(squadwindow, image=backtohome_button_picture,borderwidth=0, command=lambda: squadwindow.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    squadwindow.mainloop()

def draft_window():
    add_coins(-50000, '2')
    squadordraftwindow.destroy()
    global draftwindow
    draftwindow = Toplevel()
    draftwindow.title('Hetnikfut | DRAFT')
    draftwindow.iconbitmap(r'logo.ico')
    draftwindow.geometry("720x1280+30+30")
    draftwindow.resizable(False,False)

    global draftratings
    draftratings = []

    field_background_picture = PhotoImage(file="field.png")
    field_background = Label(draftwindow, image=field_background_picture)
    field_background.place(x=0, y=0, relwidth=1, relheight=1)

    global midrating_show
    midrating_show = Label(draftwindow, text=f"Rating: 0", fg="white", bg="black", font=("Helvetica", 25))
    midrating_show.place(x=100, y=100)

    global draft_playerholegk_button_picture
    draft_playerholegk_button_picture = PhotoImage(file='black_btn.png')
    global draft_playerhole_gk_button
    draft_playerhole_gk_button = Button(draftwindow, image=draft_playerholegk_button_picture,borderwidth=0, command=lambda: draftplayersbcpick('gk'), highlightthickness=0)
    draft_playerhole_gk_button.place(x=296, y=834)
    global draft_playerholegk_image_picture
    draft_playerholegk_image_picture = PhotoImage(file='black_btn.png')
    global draft_playerholegk_image
    draft_playerholegk_image = Button(draftwindow, image=draft_playerholegk_image_picture,borderwidth=0,highlightthickness=0)

    global draft_playerholecb1_button_picture
    draft_playerholecb1_button_picture = PhotoImage(file='black_btn.png')
    global draft_playerholecb1_button
    draft_playerholecb1_button = Button(draftwindow, image=draft_playerholecb1_button_picture,borderwidth=0, command=lambda: draftplayersbcpick('cb1'), highlightthickness=0)
    draft_playerholecb1_button.place(x=135, y=659)
    global draft_playerholecb1_image_picture
    draft_playerholecb1_image_picture = PhotoImage(file='black_btn.png')
    global draft_playerholecb1_image
    draft_playerholecb1_image = Button(draftwindow, image=draft_playerholecb1_image_picture,borderwidth=0,highlightthickness=0)

    global draft_playerholecb2_button_picture
    draft_playerholecb2_button_picture = PhotoImage(file='black_btn.png')
    global draft_playerholecb2_button
    draft_playerholecb2_button = Button(draftwindow, image=draft_playerholecb2_button_picture,borderwidth=0, command=lambda: draftplayersbcpick('cb2'), highlightthickness=0)
    draft_playerholecb2_button.place(x=455, y=660)
    global draft_playerholecb2_image_picture
    draft_playerholecb2_image_picture = PhotoImage(file='black_btn.png')
    global draft_playerholecb2_image
    draft_playerholecb2_image = Button(draftwindow, image=draft_playerholecb2_image_picture,borderwidth=0,highlightthickness=0)

    global draft_playerholecm_button_picture
    draft_playerholecm_button_picture = PhotoImage(file='black_btn.png')
    global draft_playerholecm_button
    draft_playerholecm_button = Button(draftwindow, image=draft_playerholecm_button_picture,borderwidth=0, command=lambda: draftplayersbcpick('cm'), highlightthickness=0)
    draft_playerholecm_button.place(x=299, y=455)
    global draft_playerholecm_image_picture
    draft_playerholecm_image_picture = PhotoImage(file='black_btn.png')
    global draft_playerholecm_image
    draft_playerholecm_image = Button(draftwindow, image=draft_playerholecm_image_picture,borderwidth=0,highlightthickness=0)

    global draft_playerholest1_button_picture
    draft_playerholest1_button_picture = PhotoImage(file='black_btn.png')
    global draft_playerholest1_button
    draft_playerholest1_button = Button(draftwindow, image=draft_playerholest1_button_picture,borderwidth=0, command=lambda: draftplayersbcpick('st1'), highlightthickness=0)
    draft_playerholest1_button.place(x=110, y=267)
    global draft_playerholest1_image_picture
    draft_playerholest1_image_picture = PhotoImage(file='black_btn.png')
    global draft_playerholest1_image
    draft_playerholest1_image = Button(draftwindow, image=draft_playerholest1_image_picture,borderwidth=0,highlightthickness=0)


    global draft_playerholest2_button_picture
    draft_playerholest2_button_picture = PhotoImage(file='black_btn.png')
    global draft_playerholest2_button
    draft_playerholest2_button = Button(draftwindow, image=draft_playerholest2_button_picture,borderwidth=0, command=lambda: draftplayersbcpick('st2'), highlightthickness=0)
    draft_playerholest2_button.place(x=474, y=267)
    global draft_playerholest2_image_picture
    draft_playerholest2_image_picture = PhotoImage(file='black_btn.png')
    global draft_playerholest2_image
    draft_playerholest2_image = Button(draftwindow, image=draft_playerholest2_image_picture,borderwidth=0,highlightthickness=0)


    play_button_picture = PhotoImage(file='play_btn.png')
    play_button = Button(draftwindow, image=play_button_picture,borderwidth=0, command=lambda: playgame1_window('lvl1', 'draft'), highlightthickness=0)
    play_button.place(x=270, y=1050)


    backtohome_button_picture = PhotoImage(file='backtohome.png')
    backtohome_button = Button(draftwindow, image=backtohome_button_picture,borderwidth=0, command=lambda: draftwindow.destroy(), highlightthickness=0)
    backtohome_button.place(x=170, y=1200)

    draftwindow.mainloop()

def playgame1_window(level, option):
    global playgamewindow
    playgamewindow = Toplevel()
    playgamewindow.title('Hetnikfut | GAME')
    playgamewindow.iconbitmap(r'logo.ico')
    playgamewindow.geometry("720x1280+30+30")
    playgamewindow.resizable(False,False)

    game_background_picture = PhotoImage(file="game.png")
    game_background = Label(playgamewindow, image=game_background_picture)
    game_background.place(x=0, y=0, relwidth=1, relheight=1)

    if level == 'lvl1':
        win = False
        if option == 'draft':
            midrating = int(draftsquadrating() + 1)
        if option == 'squad':
            midrating = int(squadrating() + 1)
        if midrating > 10 and midrating < 80:
            playgamewindow.destroy()
        rivalratigns = [84, 85, 86, 87]
        rivalrating = random.choice(rivalratigns)
        winnumbers = random.randint(0,10)
        if midrating >= rivalrating:
            if winnumbers <= 8:
                win = True
            if winnumbers > 8:
                win = False
        if midrating < rivalrating:
            if winnumbers <= 8:
                win = False
            if winnumbers > 8:
                win = True

        rivalrating_show = Label(playgamewindow, text=f"Rival Rating: {rivalrating}", fg="white", bg="black", font=("Helvetica", 25))
        rivalrating_show.place(x=235, y=340)
        myrating_show = Label(playgamewindow, text=f"Team Rating: {midrating}", fg="white", bg="black", font=("Helvetica", 25))
        myrating_show.place(x=235, y=380)

        homegoals = random.randint(1,7)
        awaygoals = random.randint(1,6)

        if win == True:
            while homegoals < awaygoals:
                homegoals = random.randint(1, 7)
                awaygoals = random.randint(0, 6)
        if win == False:
            while homegoals > awaygoals:
                homegoals = random.randint(0, 6)
                awaygoals = random.randint(1, 7)

        gamenum_show = Label(playgamewindow, text=f"GAME ONE", fg="white", bg="black", font=("Helvetica", 25))
        gamenum_show.place(x=260, y=300)
        minute_show = Label(playgamewindow, text=f"0'", fg="white", bg="black", font=("Helvetica", 25))
        minute_show.place(x=330, y=440)
        goals_show = Label(playgamewindow, text=f"HOME 0 - 0 AWAY", fg="white", bg="black", font=("Helvetica", 25))
        goals_show.place(x=215, y=475)


        mincounter = 0
        homegoalcounter = 0
        awaygoalcounter = 0
        secondtimer = 0

        while mincounter <= 90:
            secondtimer = secondtimer + 200
            minute_show['text'] = str(mincounter) + "'"
            mincounter = mincounter + 1
            if secondtimer == 2200 or secondtimer == 5000 or secondtimer == 7400 or secondtimer == 10000 or secondtimer == 12800 or secondtimer == 15200 or secondtimer == 16200:
                if homegoalcounter < homegoals:
                    homegoalcounter = homegoalcounter + 1
                    goals_show['text'] = f"HOME {homegoalcounter} - {awaygoalcounter} AWAY"
            if secondtimer == 1600 or secondtimer == 4000 or secondtimer == 8600 or secondtimer == 12000 or secondtimer == 13200 or secondtimer == 14300 or secondtimer == 15000:
                if awaygoalcounter < awaygoals:
                    awaygoalcounter = awaygoalcounter + 1
                    goals_show['text'] = f"HOME {homegoalcounter} - {awaygoalcounter} AWAY"

            playgamewindow.after(200, playgamewindow.update())

        wonorlost_show = Label(playgamewindow, text=f"WON/LOST", fg="white", bg="black", font=("Helvetica", 25))
        wonorlost_show.place(x=310, y=550)

        nextgame_button_picture = PhotoImage(file='nextgame_btn.png')
        nextgame_button = Button(playgamewindow, image=nextgame_button_picture, borderwidth=0, command=lambda: playgame2_window('lvl2', 'draft'), highlightthickness=0)

        claimrewards_button_picture = PhotoImage(file='claimrewards_btn.png')
        #claimrewards_button = Button(playgamewindow, image=claimrewards_button_picture, borderwidth=0, command=lambda: playgamerewards('lvl1'), highlightthickness=0)

        if win:
            updstatwins()
            updstatgoal(homegoals)
            wonorlost_show['text'] = 'WON!'
            claimrewards_button = Button(playgamewindow, image=claimrewards_button_picture, borderwidth=0,
                                         command=lambda: playgamerewards('won', homegoals-awaygoals), highlightthickness=0)
        if win == False:
            wonorlost_show['text'] = 'LOST.'
            claimrewards_button = Button(playgamewindow, image=claimrewards_button_picture, borderwidth=0,
                                         command=lambda: playgamerewards('los', homegoals-awaygoals), highlightthickness=0)

        claimrewards_button.place(x=270, y=900)

    playgamewindow.mainloop()


def draftplayersbcpick(option):
    global playersbcpickwindow
    playersbcpickwindow = Toplevel()
    playersbcpickwindow.title('Hetnikfut | Player Pick')
    playersbcpickwindow.iconbitmap(r'logo.ico')
    playersbcpickwindow.geometry("720x1280+30+30")
    playersbcpickwindow.resizable(False,False)

    playersbcpick_background_picture = PhotoImage(file="back.png")
    playersbcpick_background = Label(playersbcpickwindow, image=playersbcpick_background_picture)
    playersbcpick_background.place(x=0, y=0, relwidth=1, relheight=1)

    if option == 'gk':
        mandelbtn_pic = PhotoImage(file='mandel_black.png')
        mandelbtn = Button(playersbcpickwindow, image=mandelbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("gk", 'mandel_black.png', '86'))
        cohenbtn_pic = PhotoImage(file='cohen_black.png')
        cohenbtn = Button(playersbcpickwindow, image=cohenbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("gk", 'cohen_black.png', '89'))
        cohenycbtn_pic = PhotoImage(file='cohenyc_black.png')
        cohenycbtn = Button(playersbcpickwindow, image=cohenycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("gk", 'cohenyc_black.png', '90'))

        mandelbtn.place(x=140, y=500)
        cohenbtn.place(x=300, y=500)
        cohenycbtn.place(x=460, y=500)

    if option == 'cb1':
        draft_playerholecb1_button.config(state="disabled")
        yanchevskyycbtn_pic = PhotoImage(file='yanchevsky_yc_black.png')
        yanchevskyycbtn = Button(playersbcpickwindow, image=yanchevskyycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'yanchevsky_yc_black.png', '89'))
        yakovrbbtn_pic = PhotoImage(file='yakov_rb_black.png')
        yakovrbbtn = Button(playersbcpickwindow, image=yakovrbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'yakov_rb_black.png', '87'))
        avihaibtn_pic = PhotoImage(file='avihai_black.png')
        avihaibtn = Button(playersbcpickwindow, image=avihaibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'avihai_black.png', '86'))
        yanchevskybtn_pic = PhotoImage(file='yanchevsky_black.png')
        yanchevskybtn = Button(playersbcpickwindow, image=yanchevskybtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'yanchevsky_black.png', '87'))
        yakovbtn_pic = PhotoImage(file='yakov_black.png')
        yakovbtn = Button(playersbcpickwindow, image=yakovbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'yakov_black.png', '86'))
        mishukbtn_pic = PhotoImage(file='mishuk_black.png')
        mishukbtn = Button(playersbcpickwindow, image=mishukbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'mishuk_black.png', '84'))
        yanchevskycbbtn_pic = PhotoImage(file='yanchevsky_cb_black.png')
        yanchevskycbbtn = Button(playersbcpickwindow, image=yanchevskycbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'yanchevsky_cb_black.png', '88'))
        mishukcbbtn_pic = PhotoImage(file='mishuk_cb_black.png')
        mishukcbbtn = Button(playersbcpickwindow, image=mishukcbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb1", 'mishuk_cb_black.png', '85'))

        cbs = [yanchevskyycbtn, yakovrbbtn, avihaibtn, yanchevskybtn, yakovbtn, mishukbtn, yanchevskycbbtn, mishukcbbtn]

        plr1 = random.choice(cbs)
        plr2 = random.choice(cbs)
        while plr1 == plr2:
            plr2 = random.choice(cbs)
        plr3 = random.choice(cbs)
        while plr2 == plr3 or plr1 == plr3:
            plr3 = random.choice(cbs)

        plr1.place(x=140, y=500)
        plr2.place(x=300, y=500)
        plr3.place(x=460, y=500)

    if option == 'cb2':
        draft_playerholecb2_button.config(state="disabled")
        yanchevskyycbtn_pic = PhotoImage(file='yanchevsky_yc_black.png')
        yanchevskyycbtn = Button(playersbcpickwindow, image=yanchevskyycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'yanchevsky_yc_black.png', '89'))
        yakovrbbtn_pic = PhotoImage(file='yakov_rb_black.png')
        yakovrbbtn = Button(playersbcpickwindow, image=yakovrbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'yakov_rb_black.png', '87'))
        avihaibtn_pic = PhotoImage(file='avihai_black.png')
        avihaibtn = Button(playersbcpickwindow, image=avihaibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'avihai_black.png', '86'))
        yanchevskybtn_pic = PhotoImage(file='yanchevsky_black.png')
        yanchevskybtn = Button(playersbcpickwindow, image=yanchevskybtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'yanchevsky_black.png', '87'))
        yakovbtn_pic = PhotoImage(file='yakov_black.png')
        yakovbtn = Button(playersbcpickwindow, image=yakovbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'yakov_black.png', '86'))
        mishukbtn_pic = PhotoImage(file='mishuk_black.png')
        mishukbtn = Button(playersbcpickwindow, image=mishukbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'mishuk_black.png', '84'))
        yanchevskycbbtn_pic = PhotoImage(file='yanchevsky_cb_black.png')
        yanchevskycbbtn = Button(playersbcpickwindow, image=yanchevskycbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'yanchevsky_cb_black.png', '88'))
        mishukcbbtn_pic = PhotoImage(file='mishuk_cb_black.png')
        mishukcbbtn = Button(playersbcpickwindow, image=mishukcbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cb2", 'mishuk_cb_black.png', '85'))

        cbs = [yanchevskyycbtn, yakovrbbtn, avihaibtn, yanchevskybtn, yakovbtn, mishukbtn, yanchevskycbbtn, mishukcbbtn]

        plr1 = random.choice(cbs)
        plr2 = random.choice(cbs)
        while plr1 == plr2:
            plr2 = random.choice(cbs)
        plr3 = random.choice(cbs)
        while plr2 == plr3 or plr1 == plr3:
            plr3 = random.choice(cbs)

        plr1.place(x=140, y=500)
        plr2.place(x=300, y=500)
        plr3.place(x=460, y=500)

    if option == 'cm':
        draft_playerholecm_button.config(state="disabled")
        yahezycbtn_pic = PhotoImage(file='yahezyc_black.png')
        yahezycbtn = Button(playersbcpickwindow, image=yahezycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'yahezyc_black.png', '96'))
        isarycbtn_pic = PhotoImage(file='isaryc_black.png')
        isarycbtn = Button(playersbcpickwindow, image=isarycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'isaryc_black.png', '86'))
        bampirbbtn_pic = PhotoImage(file='bampirb_black.png')
        bampirbbtn = Button(playersbcpickwindow, image=bampirbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'bampirb_black.png', '89'))
        moradnibtn_pic = PhotoImage(file='moradni_black.png')
        moradnibtn = Button(playersbcpickwindow, image=moradnibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'moradni_black.png', '90'))
        yotambtn_pic = PhotoImage(file='yotam_black.png')
        yotambtn = Button(playersbcpickwindow, image=yotambtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'yotam_black.png', '96'))
        yakovibtn_pic = PhotoImage(file='yakovi_black.png')
        yakovibtn = Button(playersbcpickwindow, image=yakovibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'yakovi_black.png', '96'))
        yahezhmbtn_pic = PhotoImage(file='yahezhm_black.png')
        yahezhmbtn = Button(playersbcpickwindow, image=yahezhmbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'yahezhm_black.png', '88'))
        yahezbtn_pic = PhotoImage(file='yahez_black.png')
        yahezbtn = Button(playersbcpickwindow, image=yahezbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'yahez_black.png', '94'))
        shovalbtn_pic = PhotoImage(file='shoval_black.png')
        shovalbtn = Button(playersbcpickwindow, image=shovalbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'shoval_black.png', '87'))
        shonbtn_pic = PhotoImage(file='shon_black.png')
        shonbtn = Button(playersbcpickwindow, image=shonbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'shon_black.png', '88'))
        moradbtn_pic = PhotoImage(file='morad_black.png')
        moradbtn = Button(playersbcpickwindow, image=moradbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'morad_black.png', '89'))
        isarbtn_pic = PhotoImage(file='isar_black.png')
        isarbtn = Button(playersbcpickwindow, image=isarbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'isar_black.png', '84'))
        bampibtn_pic = PhotoImage(file='bampi_black.png')
        bampibtn = Button(playersbcpickwindow, image=bampibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'bampi_black.png', '88'))
        grinebtn_pic = PhotoImage(file='grine_black.png')
        grinebtn = Button(playersbcpickwindow, image=grinebtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'grine_black.png', '89'))
        bensibtn_pic = PhotoImage(file='bensi_black.png')
        bensibtn = Button(playersbcpickwindow, image=bensibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'bensi_black.png', '88'))
        yanchevskycdmbtn_pic = PhotoImage(file='yanchevskycdm_black.png')
        yanchevskycdmbtn = Button(playersbcpickwindow, image=yanchevskycdmbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'yanchevskycdm_black.png', '88'))
        yahezcdmbtn_pic = PhotoImage(file='yahezcdm_black.png')
        yahezcdmbtn = Button(playersbcpickwindow, image=yahezcdmbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'yahezcdm_black.png', '95'))
        shovalfbabtn_pic = PhotoImage(file='shovalfba_black.png')
        shovalfbabtn = Button(playersbcpickwindow, image=shovalfbabtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'shovalfba_black.png', '88'))
        grinefbabtn_pic = PhotoImage(file='grinefba_black.png')
        grinefbabtn = Button(playersbcpickwindow, image=grinefbabtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'grinefba_black.png', '90'))
        bensifbabtn_pic = PhotoImage(file='bensifba_black.png')
        bensifbabtn = Button(playersbcpickwindow, image=bensifbabtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("cm", 'bensifba_black.png', '90'))

        cms = [yahezycbtn, isarycbtn, bampirbbtn, moradnibtn, yotambtn, yakovibtn, yahezhmbtn, yahezbtn, shovalbtn, yahezhmbtn, yahezbtn, shovalbtn, shonbtn, moradbtn, isarbtn, bampibtn, grinebtn, bensibtn, yanchevskycdmbtn, yahezcdmbtn, shovalfbabtn, grinefbabtn, bensifbabtn]

        plr1 = random.choice(cms)
        plr2 = random.choice(cms)
        while plr1 == plr2:
            plr2 = random.choice(cms)
        plr3 = random.choice(cms)
        while plr2 == plr3 or plr1 == plr3:
            plr3 = random.choice(cms)

        plr1.place(x=140, y=500)
        plr2.place(x=300, y=500)
        plr3.place(x=460, y=500)

    if option == 'st1':
        draft_playerholest1_button.config(state="disabled")
        shonycbtn_pic = PhotoImage(file='shon_yc_black.png')
        shonycbtn = Button(playersbcpickwindow, image=shonycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'shon_yc_black.png', '91'))
        bensiycbtn_pic = PhotoImage(file='bensi_yc_black.png')
        bensiycbtn = Button(playersbcpickwindow, image=bensiycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'bensi_yc_black.png', '91'))
        ulitskyrbbtn_pic = PhotoImage(file='ulitsky_rb_black.png')
        ulitskyrbbtn = Button(playersbcpickwindow, image=ulitskyrbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'ulitsky_rb_black.png', '85'))
        bensinibtn_pic = PhotoImage(file='bensi_ni_black.png')
        bensinibtn = Button(playersbcpickwindow, image=bensinibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'bensi_ni_black.png', '89'))
        rotembtn_pic = PhotoImage(file='rotem_black.png')
        rotembtn = Button(playersbcpickwindow, image=rotembtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'rotem_black.png', '85'))
        ulitskybtn_pic = PhotoImage(file='ulitsky_black.png')
        ulitskybtn = Button(playersbcpickwindow, image=ulitskybtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'ulitsky_black.png', '84'))
        shtaifbtn_pic = PhotoImage(file='shtaif_black.png')
        shtaifbtn = Button(playersbcpickwindow, image=shtaifbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'shtaif_black.png', '83'))
        mishukstbtn_pic = PhotoImage(file='mishuk_st_black.png')
        mishukstbtn = Button(playersbcpickwindow, image=mishukstbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'mishuk_st_black.png', '85s'))
        yahezcfbtn_pic = PhotoImage(file='yahez_cf_black.png')
        yahezcfbtn = Button(playersbcpickwindow, image=yahezcfbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'yahez_cf_black.png', '95'))
        shonfbabtn_pic = PhotoImage(file='shon_fba_black.png')
        shonfbabtn = Button(playersbcpickwindow, image=shonfbabtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st1", 'shon_fba_black.png', '89'))

        sts = [shonycbtn, bensiycbtn, ulitskyrbbtn, bensinibtn, rotembtn, ulitskybtn, shtaifbtn, mishukstbtn, yahezcfbtn, shonfbabtn]

        plr1 = random.choice(sts)
        plr2 = random.choice(sts)
        while plr1 == plr2:
            plr2 = random.choice(sts)
        plr3 = random.choice(sts)
        while plr2 == plr3 or plr1 == plr3:
            plr3 = random.choice(sts)

        plr1.place(x=140, y=500)
        plr2.place(x=300, y=500)
        plr3.place(x=460, y=500)

    if option == 'st2':
        draft_playerholest2_button.config(state="disabled")
        shonycbtn_pic = PhotoImage(file='shon_yc_black.png')
        shonycbtn = Button(playersbcpickwindow, image=shonycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'shon_yc_black.png', '91'))
        bensiycbtn_pic = PhotoImage(file='bensi_yc_black.png')
        bensiycbtn = Button(playersbcpickwindow, image=bensiycbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'bensi_yc_black.png', '91'))
        ulitskyrbbtn_pic = PhotoImage(file='ulitsky_rb_black.png')
        ulitskyrbbtn = Button(playersbcpickwindow, image=ulitskyrbbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'ulitsky_rb_black.png', '85'))
        bensinibtn_pic = PhotoImage(file='bensi_ni_black.png')
        bensinibtn = Button(playersbcpickwindow, image=bensinibtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'bensi_ni_black.png', '89'))
        rotembtn_pic = PhotoImage(file='rotem_black.png')
        rotembtn = Button(playersbcpickwindow, image=rotembtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'rotem_black.png', '85'))
        ulitskybtn_pic = PhotoImage(file='ulitsky_black.png')
        ulitskybtn = Button(playersbcpickwindow, image=ulitskybtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'ulitsky_black.png', '84'))
        shtaifbtn_pic = PhotoImage(file='shtaif_black.png')
        shtaifbtn = Button(playersbcpickwindow, image=shtaifbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'shtaif_black.png', '83'))
        mishukstbtn_pic = PhotoImage(file='mishuk_st_black.png')
        mishukstbtn = Button(playersbcpickwindow, image=mishukstbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'mishuk_st_black.png', '85s'))
        yahezcfbtn_pic = PhotoImage(file='yahez_cf_black.png')
        yahezcfbtn = Button(playersbcpickwindow, image=yahezcfbtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'yahez_cf_black.png', '95'))
        shonfbabtn_pic = PhotoImage(file='shon_fba_black.png')
        shonfbabtn = Button(playersbcpickwindow, image=shonfbabtn_pic, highlightthickness=0, command=lambda: draftsetteamplayer("st2", 'shon_fba_black.png', '89'))

        sts = [shonycbtn, bensiycbtn, ulitskyrbbtn, bensinibtn, rotembtn, ulitskybtn, shtaifbtn, mishukstbtn, yahezcfbtn, shonfbabtn]

        plr1 = random.choice(sts)
        plr2 = random.choice(sts)
        while plr1 == plr2:
            plr2 = random.choice(sts)
        plr3 = random.choice(sts)
        while plr2 == plr3 or plr1 == plr3:
            plr3 = random.choice(sts)

        plr1.place(x=140, y=500)
        plr2.place(x=300, y=500)
        plr3.place(x=460, y=500)

    playersbcpickwindow.mainloop()

#===FUNCTIONS===
def updatecoins(coins):
    coindisplay_pack['text'] = str(coins)

def checkstats(option):
    if option == 'goals':
        with open("stats.txt") as f:
            text = f.read()
            text = text.split("-")
            goals = int(text[0])
            f.close()
            return goals
    if option == 'wins':
        with open("stats.txt") as f:
            text = f.read()
            text = text.split("-")
            wins = int(text[1])
            f.close()
            return wins

def updstatgoal(option):
    with open("stats.txt") as f:
        text = f.read()
        text = text.split("-")
        goals = int(text[0])
        f.close()
    with open("stats.txt", "w") as f:
        text = f"{option}-{text[1]}"
        f.write(text)
        f.close()

def updstatwins():
    with open("stats.txt") as f:
        text = f.read()
        text = text.split("-")
        wins = int(text[1])
        wins = wins + 1
        f.close()
    with open("stats.txt", "w") as f:
        text = f"{text[0]}-{wins}"
        f.write(text)
        f.close()

def get_custom_code(text):
    if text.startswith("addalon"):
        with open("coins.txt") as f:
            coinsamount = f.read()
            text = text.strip("addalon ")
            coinsamount = int(coinsamount) + int(text)
            f.close()

        with open("coins.txt", "w") as f:
            f.write(str(coinsamount))
            f.close()

        with open("coins.txt") as f:
            f.close()
        coinsdisplay['text'] = str(coinsamount)
        try:
            updatecoins(coinsamount)
        except:
            pass
        code_button.delete('0', END)
        code_button.insert('0', f"{text} Coins added successfully")

    if text == 'resetgame':
        with open("sqd_cm.txt", "w") as f:
            f.write("")
            f.close()
        with open("cards.txt", "w") as f:
            f.write("")
            f.close()
        with open("coins.txt", "w") as f:
            f.write("100000")
            f.close()
        with open("sqd_st2.txt", "w") as f:
            f.write("")
            f.close()
        with open("sqd_gk.txt", "w") as f:
            f.write("")
            f.close()
        with open("sqd_cb2.txt", "w") as f:
            f.write("")
            f.close()
        with open("sqd_cb1.txt", "w") as f:
            f.write("")
            f.close()
        with open("sqd_st1.txt", "w") as f:
            f.write("")
            f.close()
        code_button.delete('0', END)
        code_button.insert('0', f"Game has been reseted successfully")
        coinsdisplay['text'] = "100000"

    else:
        code_button.delete('0', END)
        code_button.insert('0', f"Wrong Command")

def add_coins(amount, option):
    try:
        mypackswin.destroy()
    except:
        pass
    with open("coins.txt") as f:
        coinsamount = f.read()
        coinsamount = int(coinsamount) + int(amount)
        f.close()

    with open("coins.txt", "w") as f:
        f.write(str(coinsamount))
        f.close()

    with open("coins.txt") as f:
        f.close()
    try:
        coinsdisplay['text'] = str(coinsamount)
        updatecoins(coinsamount)
    except:
        pass
    if option == '1':
        packanimation.destroy()

def save_player(player):
    try:
        mypackswin.destroy()
    except:
        pass
    with open("cards.txt", "a") as f:
        f.write(f"\r{player}")
        packanimation.destroy()

def setteamplayer(option, playerpath, rating):
    if option == "gk":
        with open("sqd_gk.txt", "w") as f:
            f.write(f"{playerpath}-n-{rating}")
            f.close()
            playerholegk_button_picture['file'] = playerpath
    if option == "cm":
        with open("sqd_cm.txt", "w") as f:
            f.write(f"{playerpath}-n-{rating}")
            f.close()
            playerholecm_button_picture['file'] = playerpath
    if option == "cb1":
        with open("sqd_cb2.txt") as f:
            playerpath_name = playerpath.split('_')[0]
            if playerpath_name not in f.read():
                with open("sqd_cb1.txt", "w") as f:
                    f.write(f"{playerpath}-n-{rating}")
                    f.close()
                    playerholecb1_button_picture['file'] = playerpath
    if option == "cb2":
        with open("sqd_cb1.txt") as f:
            playerpath_name = playerpath.split('_')[0]
            if playerpath_name not in f.read():
                with open("sqd_cb2.txt", "w") as f:
                    f.write(f"{playerpath}-n-{rating}")
                    f.close()
                    playerholecb2_button_picture['file'] = playerpath
    if option == "st1":
        with open("sqd_st2.txt") as f:
            playerpath_name = playerpath.split('_')[0]
            if playerpath_name not in f.read():
                with open("sqd_st1.txt", "w") as f:
                    f.write(f"{playerpath}-n-{rating}")
                    f.close()
                    playerholest1_button_picture['file'] = playerpath
    if option == "st2":
        with open("sqd_st1.txt") as f:
            playerpath_name = playerpath.split('_')[0]
            if playerpath_name not in f.read():
                with open("sqd_st2.txt", "w") as f:
                    f.write(f"{playerpath}-n-{rating}")
                    f.close()
                    playerholest2_button_picture['file'] = playerpath

    squadrating()
    playersbcpickwindow.destroy()

def draftsetteamplayer(option, playerpath, rating):
    if option == "gk":
        draft_playerholegk_image_picture['file'] = playerpath
        draft_playerholegk_image.place(x=296, y=834)
        draftratings.append(int(rating))

    if option == "cb1":
        draft_playerholecb1_image_picture['file'] = playerpath
        draft_playerholecb1_image.place(x=135, y=659)
        draftratings.append(int(rating))

    if option == "cb2":
        draft_playerholecb2_image_picture['file'] = playerpath
        draft_playerholecb2_image.place(x=455, y=660)
        draftratings.append(int(rating))

    if option == "cm":
        draft_playerholecm_image_picture['file'] = playerpath
        draft_playerholecm_image.place(x=299, y=455)
        draftratings.append(int(rating))

    if option == "st1":
        draft_playerholest1_image_picture['file'] = playerpath
        draft_playerholest1_image.place(x=110, y=267)
        draftratings.append(int(rating))

    if option == "st2":
        draft_playerholest2_image_picture['file'] = playerpath
        draft_playerholest2_image.place(x=474, y=267)
        draftratings.append(int(rating))

    draftsquadrating()
    playersbcpickwindow.destroy()

def squadrating():
    with open("sqd_gk.txt") as f:
        if os.path.getsize("sqd_gk.txt") > 0:
            gk_rt = f.read().split("-n-")[1]
        if os.path.getsize("sqd_gk.txt") == 0:
            gk_rt = 0

    with open("sqd_cm.txt") as f:
        if os.path.getsize("sqd_cm.txt") > 0:
            cm_rt = f.read().split("-n-")[1]
        if os.path.getsize("sqd_cm.txt") == 0:
            cm_rt = 0

    with open("sqd_cb1.txt") as f:
        if os.path.getsize("sqd_cb1.txt") > 0:
            cb1_rt = f.read().split("-n-")[1]
        if os.path.getsize("sqd_cb1.txt") == 0:
            cb1_rt = 0

    with open("sqd_cb2.txt") as f:
        if os.path.getsize("sqd_cb2.txt") > 0:
            cb2_rt = f.read().split("-n-")[1]
        if os.path.getsize("sqd_cb2.txt") == 0:
            cb2_rt = 0

    with open("sqd_st1.txt") as f:
        if os.path.getsize("sqd_st1.txt") > 0:
            st1_rt = f.read().split("-n-")[1]
        if os.path.getsize("sqd_st1.txt") == 0:
            st1_rt = 0

    with open("sqd_st2.txt") as f:
        if os.path.getsize("sqd_st2.txt") > 0:
            st2_rt = f.read().split("-n-")[1]
        if os.path.getsize("sqd_st2.txt") == 0:
            st2_rt = 0

    rating = int(gk_rt) + int(cm_rt) + int(cb1_rt)+ int(cb2_rt)+ int(st1_rt)+ int(st2_rt)
    midrating = int(rating)/6
    try:
        midrating_show['text'] = f"Rating: {round(midrating) + 1}"
        return round(midrating)
    except:
        return round(midrating)

def draftsquadrating():
    rating = sum(draftratings)
    global midrating
    midrating = int(rating)/6
    midrating_show['text'] = f"Rating: {round(midrating) + 1}"
    return midrating


def sbcsquadrating():
    rating = sum(draftratings)
    global midrating
    midrating = int(rating) / 6
    midrating_show['text'] = f"Rating: {round(midrating) + 1}"
    return midrating

def playgamerewards(level, score):
    if level == 'won':
        if score <= 2:
            addpack('85')
            add_coins('10000', '2')
        if score > 2 and score <= 4:
            addpack('87')
            add_coins('15000', '2')
        if score > 4 and score <= 7:
            choice = random.randint(1,2)
            if choice == 1:
                addpack('90')
            if choice == 2:
                addpack('promos')
            add_coins('15000', '2')
        playgamewindow.destroy()

    if level == 'los':
        add_coins('500', '2')
        playgamewindow.destroy()

def ispackfull(pack):
    with open("packs.txt") as f:
        packsamt = f.read()
    if pack == '85':
        if packsamt.split('-')[0] == '3':
            return True
        else:
            return False
    if pack == '87':
        if packsamt.split('-')[1] == '3':
            return True
        else:
            return False
    if pack == '90':
        if packsamt.split('-')[2] == '3':
            return True
        else:
            return False
    if pack == 'promo':
        if packsamt.split('-')[3] == '3':
            return True
        else:
            return False


def addpack(pack):
    if pack == '85':
        if ispackfull('85') is True:
            add_coins('10000', '2')
        else:
            with open("packs.txt") as f:
                packsamt = f.read()
                newpack = f"{int(packsamt.split('-')[0]) + 1}-{packsamt.split('-')[1]}-{packsamt.split('-')[2]}-{packsamt.split('-')[3]}"
            with open("packs.txt", "w") as f:
                f.write(newpack)

    if pack == '87':
        if ispackfull('87') is True:
            add_coins('40000', '2')
        else:
            with open("packs.txt") as f:
                packsamt = f.read()
                newpack = f"{packsamt.split('-')[0]}-{int(packsamt.split('-')[1]) + 1}-{packsamt.split('-')[2]}-{packsamt.split('-')[3]}"
            with open("packs.txt", "w") as f:
                f.write(newpack)

    if pack == '90':
        if ispackfull('90') is True:
            add_coins('80000', '2')
        else:
            with open("packs.txt") as f:
                packsamt = f.read()
                newpack = f"{packsamt.split('-')[0]}-{packsamt.split('-')[1]}-{int(packsamt.split('-')[2]) + 1}-{packsamt.split('-')[3]}"
            with open("packs.txt", "w") as f:
                f.write(newpack)

    if pack == 'promos':
        if ispackfull('promo') is True:
            add_coins('100000', '2')
        else:
            with open("packs.txt") as f:
                packsamt = f.read()
                newpack = f"{packsamt.split('-')[0]}-{packsamt.split('-')[1]}-{packsamt.split('-')[2]}-{int(packsamt.split('-')[3]) + 1}"
            with open("packs.txt", "w") as f:
                f.write(newpack)

home_window()
