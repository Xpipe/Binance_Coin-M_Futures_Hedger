<pre>

 _     _                                        _                _              _              _           _   
| |__ (_)_ __   __ _ _ __   ___ ___    ___ ___ (_)_ __   /\/\   | |__   ___  __| | __ _  ___  | |__   ___ | |_ 
| '_ \| | '_ \ / _` | '_ \ / __/ _ \  / __/ _ \| | '_ \ /    \  | '_ \ / _ \/ _` |/ _` |/ _ \ | '_ \ / _ \| __|
| |_) | | | | | (_| | | | | (_|  __/ | (_| (_) | | | | / /\/\ \ | | | |  __/ (_| | (_| |  __/ | |_) | (_) | |_ 
|_.__/|_|_| |_|\__,_|_| |_|\___\___|  \___\___/|_|_| |_\/    \/ |_| |_|\___|\__,_|\__, |\___| |_.__/ \___/ \__|
                                                                                  |___/                        

</pre>

Original project developed by [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/mahaviracrypto.svg?style=social&label=MahaviraCrypto)](https://twitter.com/mahaviracrypto) - https://twitter.com/MahaviraCrypto

All ideas and logic are that of Mahavira Crypto.                                               

This is a code port from the original of PHP to Python. 

The original can be found here:
https://github.com/MahaviraCrypto/Binance_Coin-M_Futures_Hedger

### How do I use this and run it?
In order to get this code to work correctly, you have to do the following:

* Setup a VPS or have a server available
* Install Python
* Install python-binance - in the terminal: `pip install python-binance`

1. have an understanding of how to use a server and have Python 7.0+ installed.
2. create an API key on Binance with trade permissions for Futures
3. update the config.py file with your API keys and set the various variables to your own preferences - order sizes for buy / sell side orders and the BTC delta amount distance when you want the bot to stop executing
4. setup a cronjob / scheduled task that executes the `__init__.py` at your specified interval or run `python __init__.py` to test and review the output
5. enjoy the magic / simplicitiy of the program running to consistently keep your hedge optimized correctly

### Disclaimer
Please use this code at your own risk.  If you modify certain variables to be beyond certain ranges, you may end up with bad results.  Always test first and optimize after.

<pre>
               .__                .__                                                 __          
  _____ _____  |  |__ _____ ___  _|__|___________          ___________ ___.__._______/  |_  ____  
 /     \\__  \ |  |  \\__  \\  \/ /  \_  __ \__  \       _/ ___\_  __ <   |  |\____ \   __\/  _ \ 
|  Y Y  \/ __ \|   Y  \/ __ \\   /|  ||  | \// __ \_     \  \___|  | \/\___  ||  |_> >  | (  <_> )
|__|_|  (____  /___|  (____  /\_/ |__||__|  (____  /      \___  >__|   / ____||   __/|__|  \____/ 
      \/     \/     \/     \/                    \/           \/       \/     |__|                

</pre>