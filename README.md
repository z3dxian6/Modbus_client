# Modbus Simulator 

## Description :octocat:

`modbus_simulator.py` est un script Python conçu pour simuler un serveur Modbus TCP. Ce simulateur est utile pour tester des applications industrielles ou des systèmes SCADA sans nécessiter de matériel réel. Le script utilise la bibliothèque [pymodbus](https://github.com/bashwork/pymodbus/) pour fournir un environnement entièrement fonctionnel.

## Fonctionnalités :triangular_flag_on_post:

- **Support Modbus TCP** : Le serveur écoute sur l'adresse IP spécifiée et le port standard Modbus TCP (502).
- **Sondes simulées** :
  - Input registers (IR)
  - Holding registers (HR) avec des données de température et d'humidité simulées.
  - Coils (CO) et Discrete Inputs (DI).
- **Personnalisation facile** : Les données simulées peuvent être ajustées dans le script pour répondre à des cas d'utilisation spécifiques.
- **Compatible avec les outils de test Modbus** comme Modbus Poll ou des bibliothèques clientes.

## Structure des Registres

| Type de Registre       | Adresse(s)  | Description                  |
|------------------------|-------------|------------------------------|
| **Holding Registers**  | 10          | Température simulée : 34°C   |
| **Holding Registers**  | 11          | Humidité simulée : 45%       |
| **Input Registers**    | 0-99        | Valeurs par défaut : 17      |
| **Coils**              | 0-99        | Valeurs par défaut : 17      |
| **Discrete Inputs**    | 0-99        | Valeurs par défaut : 17      |

## Prérequis

- Python 3.7 ou plus récent.
- Bibliothèque `pymodbus` installée.

### Installation de `pymodbus`

Utilisez la commande suivante pour installer la bibliothèque :

```bash
pip install pymodbus
```

## Configuration

Les paramètres suivants peuvent être ajustés dans le script :

- **Adresse IP** : Modifiez `SERVER_IP` pour définir l'adresse IP du serveur (par défaut : `0.0.0.0` pour écouter sur toutes les interfaces).
- **Port** : Modifiez `PORT` pour spécifier le port (par défaut : `502`).
- **ID Modbus** : Modifiez l'ID de l'esclave Modbus dans `slaves={200: store}` (par défaut : `200`).

## Utilisation

1. Clonez ce dépôt ou téléchargez le script.
2. Exécutez le script avec Python :

```bash
python modbus_simulator.py
```

3. Le serveur affichera :

```text
Démarrage du serveur modbus sur 0.0.0.0:502 avec ID Modbus 200
```

4. Connectez un client Modbus à l'adresse IP du serveur et commencez les tests.

## Exemple de Client Modbus
Voici un exemple de script Python simple pour lire les registres du serveur simulé :

```python
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1', port=502)
client.connect()

# Lire le registre de température (adresse 10)
response = client.read_holding_registers(10, 1, unit=200)
print(f"Température : {response.registers[0]}°C")

# Lire le registre d'humidité (adresse 11)
response = client.read_holding_registers(11, 1, unit=200)
print(f"Humidité : {response.registers[0]}%")

client.close()
```

## Dépannage

- **Port 502 déjà utilisé** : Assurez-vous qu'aucun autre service n'écoute sur ce port. Changez `PORT` dans le script si nécessaire.
- **Permission refusée** : L'exécution sur le port 502 nécessite des privilèges administratifs. Lancez le script avec `sudo` ou utilisez un port supérieur à 1024.

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez ajouter des fonctionnalités ou corriger des problèmes, n'hésitez pas à ouvrir une issue ou à proposer une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

---

### Auteur :shipit:
Créé par **zзd**.

Pour toute question ou suggestion, contactez-moi à [zoran.tauvry@ens.uvsq.fr](zoran.tauvry@ens.uvsq.fr).

