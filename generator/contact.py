from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ""*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Contact(firstname ="", middlename ="", lastname ="", nickname ="", title ="", company ="",
                    address ="", home ="", mobile ="", work ="",fax ="", email = "", email2 = "",
                    email3 = "", homepage ="",address_2 = "",phone_2 = "", notes = "")] + [
    Contact(firstname =random_string("firstname",10), middlename =random_string("middlename",15),
           lastname =random_string("lastname",15),nickname =random_string("nickname",15), title =random_string("title",15),
           company=random_string("company",15), address =random_string("address",15), home =random_string("home",15),
           mobile =random_string("mobile",15), work =random_string("work",15), fax =random_string("fax",15),
           email = random_string("email",15),email2 = random_string("email2",15), email3 = random_string("email3",15),
           homepage =random_string("homepage",15), bday = random_string("17",15), bmonth = random_string("Desember",15),
           byear = random_string("32",15), aday =random_string("18",15),
           amonth = random_string("August",15), ayear =random_string("33",15), address_2 = random_string("adress_2",15),
           phone_2 = random_string("phone_2",15), notes = random_string("notes",15))
    for i in range (n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))
