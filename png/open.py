import os, sys

print ("\033[1;32mInput Usr and Pass")
print ("\033[1;31mNo Sex and No Sara :v")
print ("\033[0;36mLw Ndk Tahu, Asking")
username = 'Mr-Paint'
password = 'Merana'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("user : ")
        if uname == username:
                pwd = raw_input("pass : ")

                if pwd == password:
                        print "\n\033[1;34mSelamat Datang Di Wellcome ;D",
                        sys.exit()

                else:
                        print "\n\033[1;36mSalah Pass Oy.Coba Tebak Lagi ;)\033[00m"
                        print "Tebak Ulang\n"
                        restart()

        else:
                print "\n\033[1;36mSorry, Skarang Anda Yg Merana :v\033[00m"
                print "Mikir Lagi\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
