import os

from os import chdir, getcwd, listdir, path

import PyPDF2

from time import strftime


def check_path(prompt):

    ''' (str) -> str

    Verifies if the provided absolute path does exist.

    '''

    abs_path = input(prompt)

    while path.exists(abs_path) != True:

        print ("\nThe specified path does not exist.\n")

        abs_path = input(prompt)

    return abs_path   

   

print ("\n")


folder = check_path("Provide absolute path for the folder: ")


list=[]

directory=folder

for root,dirs,files in os.walk(directory):

    for filename in files:

        if filename.endswith('.pdf'):

            t=os.path.join(directory,filename)

            list.append(t)




for item in list:
    path=item

    head,tail=os.path.split(path)

    var="\\"

   

    tail=tail.replace(".pdf",".txt")

    name=head+var+tail

    

   

   

    

    content = ""

    

    pdf = PyPDF2.PdfFileReader(path, "rb")

    

    for i in range(0, pdf.getNumPages()):

        

        content += pdf.getPage(i).extractText() + "\n"
        

    print (strftime("%H:%M:%S"), " pdf  -> txt ")

    with open(name,'a') as out:
        out.write(content )
