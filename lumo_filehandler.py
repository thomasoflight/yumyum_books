import os, sys
import datetime

sys.dont_write_bytecode = True


# ---FILES:BOOKLIST--- #
booklist_folder = "..." # E.G. /Users/bobby/Documents/booklist

bookstr_to_filename = {
    'category name':"/Users/bobby/Documents/booklist/fiction.txt",
    'category name 2':"/Users/bobby/Documents/booklist/non-fiction.txt",
    'category name 3':"/Users/bobby/Documents/booklist/poetry.txt",
    'category name 4':"/Users/bobby/Documents/booklist/computers.txt",
    }


# ---FUNCTIONS--- #
class Wrtrs(object):
    
    def pool_wrtr(self, pool_name, pool_output, file, ascii_art):
        
        with open(file, "a+") as fin:

                if ascii_art:                
                    fin.write("\n\n")
                    fin.write(pool_name)

                else:
                    pool_name_frmttd = ("\n\n-%s-") % pool_name.upper()
                    fin.write(pool_name_frmttd)


                for goal in pool_output:
                    fin.write("\n")
                    fin.write(goal)


    def basic_wrtr(self, content, file):

        with open(file, "a+") as fin:
            fin.write(content)
            fin.write("\n")

    def basic_wrtr_list(self, content, file):

        with open(file, "a+") as fin:
            for item in list:
                fin.write(content)
                fin.write("\n")


    def over_wrtr(self, content, file):

        with open(file, "w+") as fin:
            fin.write(content)
            fin.write("\n")

    def over_wrtr_list(self, list, file):

        with open(file, "w+") as fin:
            for item in list:
                fin.write(item)
                fin.write("\n")

    def basic_wrtr_list(self, list, file):

        with open(file, "a+") as fin:
            for item in list:
                fin.write(item)
                fin.write("\n")

    def mk_jrnl(self):
        self.basic_wrtr(today_frmttd.upper(), tdy_jrnl_file)
        self.basic_wrtr("", tdy_jrnl_file)
