docker-compose up -d
echo "Waiting for server to start..."
sleep 1
python3 get-url.py