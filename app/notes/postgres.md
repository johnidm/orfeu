https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04

Create a super user om database

```
sudo -i -u postgres
psql <db name>

CREATE USER <user> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE "<database name>" to <user>;
```
