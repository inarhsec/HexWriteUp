# README

## Starting Point

* Start the machine by downloading the OpenVPN file that is provided by HTB.

```bash
#sudo openvpn <filen.ovpn>
```

{% stepper %}
{% step %}
### Which TCP port is open on the machine?

Answer: `6379`

* TTL OS identification
{% endstep %}

{% step %}
### Which service is running on the port that is open on the machine?

Answer: `redis`
{% endstep %}

{% step %}
### What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database

Answer: `in-memory database`
{% endstep %}

{% step %}
### Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into the terminal without any arguments.

Answer: `redis-cli`
{% endstep %}

{% step %}
### Which flag is used with the Redis command-line utility to specify the hostname?

Answer: `-h`
{% endstep %}

{% step %}
### Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server?

Answer: `info`
{% endstep %}

{% step %}
### What is the version of the Redis server being used on the target machine?

Answer: `5.0.7`
{% endstep %}

{% step %}
### Which command is used to select the desired database in Redis?

Answer: `select`
{% endstep %}

{% step %}
### How many keys are present inside the database with index 0?

Answer: `4`
{% endstep %}

{% step %}
### Which command is used to obtain all the keys in a database?

Answer: `KEYS *`
{% endstep %}

{% step %}
### Submit flag

Answer: `03e1d2b376c37ab3f5319922053953eb`
{% endstep %}
{% endstepper %}
