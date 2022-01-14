
from tkinter import *
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )

def show():
    city = clicked1.get() 
    state=clicked2.get()
    with open('task2data.txt', 'a') as f:
        f.write(city)
        f.write(" "+state)
        f.write('\n')
    print(city,state)
  
# Dropdown menu options
states = [ "Andhra Pradesh",
                "Arunachal Pradesh",
                "Assam",
                "Bihar",
                "Chhattisgarh",
                "Goa",
                "Gujarat",
                "Haryana",
                "Himachal Pradesh",
                "Jammu and Kashmir",
                "Jharkhand",
                "Karnataka",
                "Kerala",
                "Madhya Pradesh",
                "Maharashtra",
                "Manipur",
                "Meghalaya",
                "Mizoram",
                "Nagaland",
                "Odisha",
                "Punjab",
                "Rajasthan",
                "Sikkim",
                "Tamil Nadu",
                "Telangana",
                "Tripura",
                "Uttarakhand",
                "Uttar Pradesh",
                "West Bengal",
                "Andaman and Nicobar Islands",
                "Chandigarh",
                "Dadra and Nagar Haveli",
                "Daman and Diu",
                "Delhi",
                "Lakshadweep",
                "Puducherry",
]
citys=['Alirajpur',
			'Anuppur',
			'Ashok Nagar',
			'Balaghat',
			'Barwani',
			'Betul',
			'Bhind',
			'Bhopal',
			'Burhanpur',
			'Chhatarpur',
			'Chhindwara',
			'Damoh',
			'Datia',
			'Dewas',
			'Dhar',
			'Dindori',
			'Guna',
			'Gwalior',
			'Harda',
			'Hoshangabad',
			'Indore',
			'Jabalpur',
			'Jhabua',
			'Katni',
			'Khandwa (East Nimar)',
			'Khargone (West Nimar)',
			'Mandla',
			'Mandsaur',
			'Morena',
			'Narsinghpur',
			'Neemuch',
			'Panna',
			'Rewa',
			'Rajgarh',
			'Ratlam',
			'Raisen',
			'Sagar',
			'Satna',
			'Sehore',
			'Seoni',
			'Shahdol',
			'Shajapur',
			'Sheopur',
			'Shivpuri',
			'Sidhi',
			'Singrauli',
			'Tikamgarh',
			'Ujjain',
			'Umaria',
			'Vidisha',]
  
# datatype of menu text
clicked1 = StringVar()
clicked2 = StringVar()
  
# initial menu text
clicked1.set( "MP" )
clicked2.set("Indore")
  
# Create Dropdown menu
drop1 = OptionMenu( root , clicked1 , *states )
drop2 = OptionMenu( root , clicked2 , *citys )
drop1.pack()
drop2.pack()
  
# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  
# Execute tkinter
root.mainloop()
