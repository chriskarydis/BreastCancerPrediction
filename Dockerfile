# Βασική Python εικόνα
FROM python:3.10-slim

# Ορίζουμε working directory
WORKDIR /app

# Αντιγραφή αρχείων στο container
COPY . .

# Εγκατάσταση απαιτήσεων
RUN pip install --no-cache-dir -r requirements.txt

# Άνοιγμα port
EXPOSE 5000

# Εκκίνηση Flask app
CMD ["python", "app.py"]
