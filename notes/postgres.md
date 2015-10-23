https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04

Create a super user om database

sudo -i -u postgres

createdb -E UTF-8 <db name>

```
sudo -i -u postgres
psql <db name>

CREATE USER <user> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE "<database name>" to <user>;
ALTER USER <user> CREATEDB;
```

export DATABASE_URL="postgres://postgres:postgres@localhost/orfeu"

DATABASE_URL="postgres://postgres:postgres@localhost/orfeu" 
