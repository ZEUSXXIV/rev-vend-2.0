{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "MissingSchema",
     "evalue": "Invalid URL '/users.json': No schema supplied. Perhaps you meant http:///users.json?",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mMissingSchema\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-3425715be3a4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     21\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;34m'phone'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mphone\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'number of bottles'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mquantity\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'points'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[0mpoints\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 22\u001b[1;33m \u001b[0mdb\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mchild\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'users'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpush\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     23\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     24\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"done\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pyrebase\\pyrebase.py\u001b[0m in \u001b[0;36mpush\u001b[1;34m(self, data, token, json_kwargs)\u001b[0m\n\u001b[0;32m    307\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    308\u001b[0m         \u001b[0mheaders\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbuild_headers\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtoken\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 309\u001b[1;33m         \u001b[0mrequest_object\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequests\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpost\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrequest_ref\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdumps\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mjson_kwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mencode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"utf-8\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    310\u001b[0m         \u001b[0mraise_detailed_error\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrequest_object\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    311\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mrequest_object\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjson\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36mpost\u001b[1;34m(self, url, data, json, **kwargs)\u001b[0m\n\u001b[0;32m    576\u001b[0m         \"\"\"\n\u001b[0;32m    577\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 578\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'POST'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mjson\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mjson\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    579\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    580\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[0;32m    514\u001b[0m             \u001b[0mhooks\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mhooks\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    515\u001b[0m         )\n\u001b[1;32m--> 516\u001b[1;33m         \u001b[0mprep\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprepare_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    517\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    518\u001b[0m         \u001b[0mproxies\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mproxies\u001b[0m \u001b[1;32mor\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\requests\\sessions.py\u001b[0m in \u001b[0;36mprepare_request\u001b[1;34m(self, request)\u001b[0m\n\u001b[0;32m    447\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    448\u001b[0m         \u001b[0mp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPreparedRequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 449\u001b[1;33m         p.prepare(\n\u001b[0m\u001b[0;32m    450\u001b[0m             \u001b[0mmethod\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    451\u001b[0m             \u001b[0murl\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\requests\\models.py\u001b[0m in \u001b[0;36mprepare\u001b[1;34m(self, method, url, headers, files, data, params, auth, cookies, hooks, json)\u001b[0m\n\u001b[0;32m    312\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    313\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprepare_method\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 314\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprepare_url\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    315\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprepare_headers\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    316\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprepare_cookies\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcookies\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\requests\\models.py\u001b[0m in \u001b[0;36mprepare_url\u001b[1;34m(self, url, params)\u001b[0m\n\u001b[0;32m    386\u001b[0m             \u001b[0merror\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0merror\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mto_native_string\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'utf8'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    387\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 388\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mMissingSchema\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0merror\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    389\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    390\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mhost\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mMissingSchema\u001b[0m: Invalid URL '/users.json': No schema supplied. Perhaps you meant http:///users.json?"
     ]
    }
   ],
   "source": [
    "import pyrebase\n",
    "\n",
    "points = 2\n",
    "quantity = 1\n",
    "phone = \"7798988500\"\n",
    "firebaseConfig = {\n",
    "    'apiKey': \"AIzaSyCtj8nO9ld-NeDJ3GXqEjVfwnMjnQltwZU\",\n",
    "    'authDomain': \"try1-6edc1.firebaseapp.com\",\n",
    "    'projectId': \"try1-6edc1\",\n",
    "    'storageBucket': \"try1-6edc1.appspot.com\",\n",
    "    'messagingSenderId': \"164103821321\",\n",
    "    'appId': \"1:164103821321:web:f37ee14a1ec0746a8040d8\",\n",
    "    'measurementId': \"G-L0G5M8NB3Z\",\n",
    "    'databaseURL' : \"\"\n",
    "  }\n",
    "#print(\"hello\")\n",
    "\n",
    "firebase = pyrebase.initialize_app(firebaseConfig)\n",
    "db = firebase.database()\n",
    "\n",
    "data={'phone':phone,'number of bottles':quantity,'points':points}\n",
    "db.child('users').push(data)\n",
    "\n",
    "print(\"done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
