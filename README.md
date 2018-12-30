# Facebook Chat (Terminal mode)
[![npm](https://img.shields.io/npm/l/date-2.svg?style=flat-square)]() [![npm](https://img.shields.io/badge/Langage-Python-blue.svg)](https://en.wikipedia.org/wiki/Python_(programming_language))

[website](https://touir1.github.io/Facebook-Chat-Terminal-mode/)

Facebook Chat is a python script to chat with facebook account using the terminal.

## Usage ##


to use Facebook Chat Terminal mode you need to:
```
Usage: python fbchat_terminal_mode.py [options]

Options:
  -h, --help            show this help message and exit
  -p PASSWORD, --password=PASSWORD
                        the password for the facebook account
  -u USER, --username=USER
                        the username for the facebook account
```

<!---
to use Spam Classifier as a web service you need to:

**-Start the web server**
```
Usage: web_service.py [options]

Options:
  -h, --help            show this help message and exit
  -c FILE, --classifier=FILE
                        import classifier from file
  -v FILE, --vectorizer=FILE
                        import vectorizer from file
  -p PORT, --port=PORT  port of the server
  -a ADRESS, --adress=ADRESS
                        adress of the server
```

**-call the web service**

```
http://[adress]:[port]/[subject]/[message]

adress: adress of the server
port: port of the server
subject: subject of the mail encoded in url format
message: message of the mail encoded in url format
```
-->
## Authors ##

* Mohamed Ali Touir
  * Github: [https://github.com/touir1](https://github.com/touir1)
  * Email: [touir.mat@gmail.com](mailto:touir.mat@gmail.com)

## License ##

Facebook chat Terminal Mode is published under the [MIT license](http://www.opensource.org/licenses/mit-license).

## Special thanks ##

Fbchat used to get the user info [fbchat: Facebook Chat (Messenger) for Python](https://github.com/carpedm20/fbchat).

Micah Elliott (website: [http://MicahElliott.com](http://MicahElliott.com)) and Kevin Lange (email: [k@dakko.us](mailto:k@dakko.us)) for the image-to-ansi.py module.
<!---
csmining.org for providing the dataset used for training my model [csmining: Spam email datasets](http://csmining.org/index.php/spam-email-datasets-.html).
-->
