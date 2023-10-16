# Minecraft eto maia jizni

### This is our Minecraft world that me and my friends play in.

#### This repo uses a docker image to run the server and an ngrok tunnel so that the rest of us can connect to it when one is running it locally.

### Installation

1. Make sure you have Docker installed
2. Clone the repo
   ```sh
   git clone https://github.com/bandreit/minecraft-eto-maia-jizni.git
   ```
3. Enter your NGROK AuthToken in `ngrok.yml`
   ```yml
   authtoken: <YOUR_OWN_TOKEN>;
   ```

### How to run it

Simply run the bash script to start/stop it:

```bash
	./start-server.sh
```

#### The URL will then be printed to your console for tou to share

This will

```bash
	./stop-server.sh
```

\*you might need to give permiossions to the bash scripts first
