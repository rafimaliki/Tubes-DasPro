# File: main.py
import commands
import function.f13_load as data

import os

os.system("cls")

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

# Mengisi users, candi, dan bahan_bangunan menggunakan file
users = data.load(r"file\user.csv", users) # Matrix data user
candi = data.load(r"file\candi.csv", candi) # Matrix data user
bahan_bangunan = data.load(r"file\bahan_bangunan.csv", bahan_bangunan) # Matrix data user

active_user = [0,0] # Untuk menentukan apakah ada user yang sedang login atau tidak

iterasi = 0 

# Menerima masukan
running = True
while running:

    if iterasi == 0:
        masukan = input(">>> ")

    else:
        masukan = input("\n>>> ")

    iterasi += 1
    running_dict = {'value': running}
    commands.run(masukan,users,candi,bahan_bangunan,active_user,running_dict)
    running = running_dict['value']