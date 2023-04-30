# Auto-GPT-Messages


AutoGPT plugin for iMessages and potentially other messaging platforms in the future

Note: please be careful with this as AutoGPT could send text messages that may damage relationships. Furthermore this plugin is perhaps best paired with Redis and the Vicuna plugin
since text messages are about the most personal data.


This plugin can run on any platform since it simply makes requests to a python server which allows the plugin to run on any platform however, there still must be a Mac running the server. Also if you run AutoGPT on your mac, you can just set the base url to localhost.

### Pre Installation Steps
Go to this repo and follow the steps here to setup the iMessage server
[iMessage API](https://github.com/danikhan632/iMessage-API)

Make sure to create an "api_key"/ Password are and that there in a url which it is accessible
If the Mac is on a different network, [tunnelto](https://tunnelto.dev/) and [ngrok](https://ngrok.com/) are good methods to make it public


### Plugin Installation Steps

for Linux, depending on distro
```
sudo apt-get install zip
apk add zip
sudo pacman -S zip
sudo yum install zip
```
Mac / Linux / WSL
```
cd plugins && git clone https://github.com/danikhan632/Auto-GPT-Messages-Plugin.git && zip -r ./Auto-GPT-Messages-Plugin.zip ./Auto-GPT-Messages-Plugin && rm -rf ./Auto-GPT-Messages-Plugin && cd .. && ./run.sh --install-plugin-deps

```
Windows, Powershell
```
cd plugins; git clone https://github.com/danikhan632/Auto-GPT-Messages-Plugin.git; Compress-Archive -Path .\Auto-GPT-Messages-Plugin -DestinationPath .\Auto-GPT-Messages-Plugin.zip; Remove-Item -Recurse -Force .\Auto-GPT-Messages-Plugin; cd ..
```



5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=AutoGPTMessagesPlugin
   IMESSAGE_PASSWORD_KEY=your_password_key
   IMESSAGE_BASE_URL=your_imessage_server_url
   ```

   If the plugin is not allowlisted, you will be warned before it's loaded.


   Example
   ```
   ai_goals:
   - Quickly and accurately display incoming text messages using the messages plugin
   to ensure timely communication.
   - Provide a user-friendly interface for viewing and responding to text messages, with
   customizable settings to meet individual preferences.
   - Integrate with other communication tools and platforms to streamline messaging across
   multiple channels.
   - Continuously monitor for new messages and provide real-time notifications to ensure
   prompt responses.
   - Maintain the privacy and security of all messages and user data.
   ai_name: MSGGPT
   ai_role: an AI assistant that specializes in displaying text messages using the messages
   plugin for seamless communication.
   api_budget: 0.0
```