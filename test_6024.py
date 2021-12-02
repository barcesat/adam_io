from adam_io import Adam6024D
from adam_io import DigitalOutput
from adam_io import AnalogOutput

ip='192.168.1.110'
username = 'root'
password = '00000000'

adam = Adam6024D(ip, username, password)
# print(adam)
do = DigitalOutput()

# set every available output to 1
do[0]=0
do[1]=1
try:
    adam.d_output(do)
except Exception as err:
    print(err)

ao = AnalogOutput()
ao[0]='00FF'
ao[1]='0182'

try:
    adam.a_output(ao)
except Exception as err:
    print(err)

