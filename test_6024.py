from adam_io import Adam6024D
from adam_io import DigitalOutput
from adam_io import AnalogOutput
from adam_io.digital_io import DigitalInput

ip='192.168.1.110'
username = 'root'
password = '00000000'

adam = Adam6024D(ip, username, password)
# print(adam)
do = DigitalOutput()
print(do)

# set every available output to 1
do[0]=0
do[1]=1
try:
    adam.d_output(do)
except Exception as err:
    print(err)

di = adam.d_input()
print(di)

# digital inputs
print("DI0: ", di[0]) # DI0
print("DI1: ", di[1]) # DI1

ao = AnalogOutput()
# ao[0]=int('0x00FF', 16) # 1.245 mA @ 0-20mA onfiguration
# ao[1]=int('0x0182', 16) # 1.885 mA @ 0-20mA onfiguration
print(ao)

ao[0]='00FF' # 1.245 mA @ 0-20mA onfiguration
ao[1]='0182' # 1.885 mA @ 0-20mA onfiguration

try:
    adam.a_output(ao)
except Exception as err:
    print(err)

ai = adam.a_input()
print(ai)

# digital inputs
print("AI0: ", ai[0]) # AI0
print("AI1: ", ai[1]) # AI1
