FROM python:3.8

WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copier notre projet dans le conteneur 
COPY . .

            
# Exposer le port 8000
EXPOSE 8000

# Commande pour lancer l'application 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
