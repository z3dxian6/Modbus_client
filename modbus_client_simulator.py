rom pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging

# Configuration du logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Adresse IP et port du serveur
SERVER_IP = "0.0.0.0"
PORT = 502

# Simulation de la sonde - utilisation de l'ID Modbus 200
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [17]*100),  # input discrète
    co=ModbusSequentialDataBlock(0, [17]*100),  # coils
    hr=ModbusSequentialDataBlock(0, [0]*10 +  [34, 45] + [0]*88),  # Holding registers avec température et humidité, address 10 data 34, address 11 data 45
    ir=ModbusSequentialDataBlock(0, [17]*100)  # input registers
)
context = ModbusServerContext(slaves={200: store}, single=False)

# Configuration de l'identité du serveur
identity = ModbusDeviceIdentification()
identity.VendorName = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'

print(f"Démarrage du serveur modbus sur {SERVER_IP}:{PORT} avec ID Modbus 200")
StartTcpServer(context, identity=identity, address=(SERVER_IP, PORT))
