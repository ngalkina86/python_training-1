from sys import maxsize

class Contact:

    def __init__(self,bday=None,bmonth=None,aday=None, amonth=None,firstname=None,middlename=None, lastname=None,
                 nickname=None, title=None, company=None,address=None, home=None, mobile=None, work=None,fax=None,
                 email=None,emai12=None, emai13=None, homepage=None,byear=None, ayear=None, address_2=None, phone_2=None,
                 notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = emai12
        self.email3 = emai13
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address_2= address_2
        self.phone_2= phone_2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize