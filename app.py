from io import BytesIO
import pandas as pd

import numpy as np
t1_trip =  pd.read_csv("D:/xyz/data/t_trip_details.csv")

trip=[t1_trip]
print(t1_trip.head(20))
t1_trip.shape

duplicatedcar = t1_trip.car_id.duplicated()

print(duplicatedcar.head(30)) 

ucar =(t1_trip[t1_trip.car_id.duplicated() == False ])
print(ucar.head(10))

print(ucar.duplicated())

t1_trip['dest_nz_edt'] = pd.to_datetime(t1_trip.dest_nz_edt)

print(t1_trip.head(3))
t1_trip.dtypes

g= t1_trip.groupby('car_id')
for car_id, car_id_df in g:
    car_id_df['Day_of_Year']= t1_trip.dest_nz_edt.dt.dayofyear
    
    print (car_id)
    print (car_id_df)
    
car_id3698 = t1_trip[(t1_trip.car_id == 3698)]
car_id3698['Day_of_Year']= t1_trip.dest_nz_edt.dt.dayofyear
car_id3698.sort_values(by=['dest_nz_edt'],inplace=True,ascending=False)
print(car_id3698.head(10))
car_id3698.shape

car_id4128=t1_trip[(t1_trip.car_id == 4128)]
car_id4128['Day_of_Year']= t1_trip.dest_nz_edt.dt.dayofyear
car_id4128.sort_values(by=['dest_nz_edt'],inplace=True,ascending=False)
print(car_id4128.head(10))
car_id4128.shape

car_id3743=t1_trip[(t1_trip.car_id == 3743)]
car_id3743['Day_of_Year']= t1_trip.dest_nz_edt.dt.dayofyear
car_id3743.sort_values(by=['dest_nz_edt'],inplace=True,ascending=False)
print(car_id3743.head(10))
car_id3743.shape

car_id3864=t1_trip[(t1_trip.car_id == 3864)]
car_id3864['Day_of_Year']= t1_trip.dest_nz_edt.dt.dayofyear
car_id3864.sort_values(by=['dest_nz_edt'],inplace=True,ascending=False)

print(car_id3864.head(10))
car_id3864.shape

t1_trip.dest_nz_edt.dt.dayofyear
t1_trip.shape
print(car_id_df)


from matplotlib import pyplot as plt

    

car_id3743.dtypes

plt.plot(car_id3743.Day_of_Year,'o',label = 'carid_3743')
plt.plot(car_id4128.Day_of_Year,'o',color="red",label = 'carid_4128')
plt.plot(car_id3864.Day_of_Year,'o',color="purple", label = 'carid_3864')
plt.plot(car_id3698.Day_of_Year,'o',color="green", label='carid_3698')
plt.xlabel('index of car_id occurence')
plt.ylabel('day ')
plt.legend()
plt.title('Car_ids utilized according to days')
plt.show()

	


#@app.route('/visualisation1/')
def visualisation1():
	
	
	plt.plot(car_id3743.Day_of_Year,'o',label = 'carid_3743')
	y = [7,14]
	x = [5,10,15,20,25,30,35,40]

	plt.yticks([0,7,14])
	plt.plot(car_id4128.Day_of_Year,'o',color="red",label = 'carid_4128')
	plt.plot(car_id3864.Day_of_Year,'o',color="purple", label = 'carid_3864')
	plt.plot(car_id3698.Day_of_Year,'o',color="green", label='carid_3698')
	plt.xlabel('index of car_id occurence')
	plt.ylabel('week ')
	plt.legend()
	plt.title('Car_ids utilized according to week (2 weeks - 7 day y-axis)')
	plt.show()
    
	bytes_image = io.BytesIO()
	plt.savefig(bytes_image, format='png')
	bytes_image.seek(0)
	return bytes_image
plt.plot(car_id3743.Day_of_Year,'o',label = 'carid_3743')
y = [7,14]
x = [5,10,15,20,25,30,35,40]

plt.yticks([0,7,14])
plt.plot(car_id4128.Day_of_Year,'o',color="red",label = 'carid_4128')
plt.plot(car_id3864.Day_of_Year,'o',color="purple", label = 'carid_3864')
plt.plot(car_id3698.Day_of_Year,'o',color="green", label='carid_3698')
plt.xlabel('index of car_id occurence')
plt.ylabel('week ')
plt.legend()
plt.title('Car_ids utilized according to week (2 weeks - 7 day y-axis)')
plt.show()
	
from flask import Flask, send_file, render_template

app = Flask(__name__)

  

@app.route('/', methods=['GET'])
def chart():
  #  bytes_obj = visualisation1()
	return render_template('index.html', visualisation1=visualisation1)
	#return <h1> Hello </h1>
if __name__ == '__main__':
    app.run(debug=False)
#<img src="http://localhost:5000/visualisation1/" />



	
#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def index():
#	return ' <img src="/visualisation1/" />' 