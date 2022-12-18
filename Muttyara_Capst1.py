data_karyawan = {
    '1201':{
        'Nama':'Muthia Aluna Azzahra',
        'Umur':25,
        'Gender':'Perempuan',
        'Pekerjaan':'Data Science'
        },
    '1202':{
        'Nama':'Arkanza Eqbal Gauzan',
        'Umur':30,
        'Gender':'Laki-laki',
        'Pekerjaan':'Web Development'
        },
    '1203':{
        'Nama':'Zea Alesha Shaqueena',
        'Umur': 24,
        'Gender':'Perempuan',
        'Pekerjaan':'UI/UX Designer'
        },
    '1204':{
        'Nama':'Kemal Nabil Haidan',
        'Umur': 31,
        'Gender':'Laki-laki',
        'Pekerjaan':'Digital Marketing'
    }
}

def read_data() :
    print('********** LAPORAN DATA KARYAWAN PT. MEGA MENANTY **********\n')
    print('============================================================================')
    print('NIK\t| NAMA\t\t\t| UMUR\t| GENDER\t| PEKERJAAN')
    print('============================================================================')
    for i in data_karyawan :
        print(f'{i}\t| {data_karyawan[i]["Nama"]}\t| {data_karyawan[i]["Umur"]}\t| {data_karyawan[i]["Gender"]}\t| {data_karyawan[i]["Pekerjaan"]}')

def specific_data() :
    Input = input('Masukkan NIK : ')
    count = 0
    for input_user in data_karyawan.keys() :
        if Input == input_user :
            count += 1

            print('Yes! Data karyawan ditemukan.')

            print(f'Nama:{data_karyawan[Input]["Nama"]}')
            print(f'Umur:{data_karyawan[Input]["Umur"]}')
            print(f'Gender:{data_karyawan[Input]["Gender"]}')
            print(f'Pekerjaan:{data_karyawan[Input]["Pekerjaan"]}')
        else :
            count += 0
    if count == 0:
        print('Maaf. Data karyawan tidak ditemukan.')

def delete_data() :
    read_data()
    kodehapus = input('Masukkan data karyawan yang ingin dihapus: ')
    if kodehapus in data_karyawan :
        confrm = input('Apakah anda yakin ingin menghapus data karyawan? (Y/N): ')
        if confrm.lower() == 'y':
            del data_karyawan[kodehapus]
            read_data()
        else:
            print('\nMasukkan kode berupa NIK!\n')
            delete_data()
    else :
        print('Maaf Data Tidak Ada:(')
        read_data()

def create_data() :
    id_input = input('Masukan NIK baru : ')
    Nama_karyawan = input('Masukkan Nama Karyawan: ')
    Umur_karyawan = int(input('Masukkan Umur Karyawan: '))
    Gender_karyawan = input('Masukkan Gender Karyawan: ')
    Pekerjaan_karyawan = input('Masukkan Pekerjaan Karyawan: ')
    data_karyawan.update({id_input:{
        'Nama':Nama_karyawan,
        'Umur':Umur_karyawan,
        'Gender':Gender_karyawan,
        'Pekerjaan':Pekerjaan_karyawan
    }})
    print('Yes! Update data karyawan telah berhasil.')

def update_data() :
    inputNIK_user = (input('Masukkan NIK: '))
    for input_user in data_karyawan.keys() :
        if inputNIK_user == input_user :
            print('Data karyawan ditemukan!\t')
            print(f'''
            Nama:{data_karyawan[input_user]['Nama']} 
            Umur:{data_karyawan[input_user]['Umur']}
            Gender:{data_karyawan[input_user]['Gender']}
            Pekerjaan:{data_karyawan[input_user]['Pekerjaan']}
            ''')

            print('Silahkan pilih data yang ingin diubah: ')
            print('''
            1. Nama Karyawan
            2. Umur Karyawan
            3. Pekerjaan Karyawan
            ''')
            inputID_user = input('Masukkan data yang ingin diubah (1-3): ')

            if inputID_user == '1':
                input_namabaru = input('Masukkan Nama Baru: ')
                data_karyawan[input_user]['Nama'] = input_namabaru
                print('Data telah update!')
            elif inputID_user == '2':
                input_umurbaru = int(input('Masukkan Umur Baru: '))
                data_karyawan[input_user]['Umur'] = input_umurbaru
                print('Data telah update!')
            elif inputID_user == '3':
                input_pekerjaanbaru = input('Masukkan Pekerjaan Baru: ')
                data_karyawan[input_user]['Pekerjaan'] = input_pekerjaanbaru
                print('Data telah update!')
                break
        else:
            print('Maaf data tidak ada.')

def menu_utama() :
    while True:
        print('''
        ====== Selamat Datang di PT. Mega Menanty ======

        Menu Utama :
            1. Laporan data karyawan
            2. Menambahkan data karyawan
            3. Mengubah data karyawan
            4. Menghapus data karyawan
            5. Selesai
        ''')
        input_menu_utama = input(f'''Silahkan pilih menu yang ingin di jalankan. \nMasukkan pilihan menu anda (1-5): ''')

        while True:
            if input_menu_utama == '1':
                menu_utama_sub = input('''
                Pilih menu dibawah:
                1. Menampilkan data karyawan
                2. Mencari data karyawan
                3. Kembali ke menu utama

                Masukkan angka 1-3: ''')
                if menu_utama_sub == '1':
                    read_data()
                elif menu_utama_sub == '2':
                    specific_data()
                elif menu_utama_sub == '3' :
                    break
                else:
                    menu_utama()
                    break
            elif input_menu_utama =='2':
                create_data()
                break
            elif input_menu_utama == '3':
                update_data()
                break
            elif input_menu_utama == '4':
                delete_data()
                break
            elif input_menu_utama == '5':
                print()
                print('''Terima kasih atas kunjungan anda.''')
                return None
            else:
                print()
                print('''Angka yang anda masukkan salah. \nSilahkan masukkan pilihan menu (1-5) : ''')

def submenu1() :
    print(f'''
    Sub Menu :
        1. Menampilkan laporan data karyawan
        2. Mencari data karyawan
        3. Kembali ke menu utama
    ''')

def submenu2() :
    print(f'''
    Sub Menu :
        1. Menampilkan laporan data karyawan
        2. Menghapus data karyawan
        3. Kembali ke menu utama
    ''')

def submenu3() :
    print(f'''
    Sub Menu :
        1. Menampilkan laporan data karyawan
        2. Menambahkan data karyawan
        3. Kembali ke menu utama
    ''')

def submenu4() :
    print(f'''
    Sub Menu :
        1. Menampilkan laporan data karyawan
        2. Mengubah data karyawan
        3. Kembali ke menu utama
    ''')

def submenu5() :
    print(f'''
    Sub Menu :
        1. Menampilkan laporan data karyawan
        2. Kembali ke menu utama
    ''')

def pilih_sub():
    pilih_sub = input (f'''Masukkan pilihan menu anda: ''')
    return pilih_sub

menu_utama()
