# Database Management
Applies to ***local*** installations.

## Logging in
### As root
`psql -U postgres`
Password will be whatever you set when you downloaded psql
### As user
`psql -h localhost -U csce315_905_05user csce315_905_05db` 
Must set up database first!

## Setup database
1. `createdb -T template0 -U postgres csce315_905_05db`
2. `createuser csce315_905_05user -P`
   1. Set the password in the `.env` file to whatever this is

## Upload database dump
1. In psql: `drop database csce315_905_05db;`
2. `psql -U postgres -d csce315_905_05db < p3db.pgsql`
   1. Or if on powershell  \
   `Get-Content p3db.pgsql | psql -U postgres -d csce315_905_05db`


## Download (local) database dump
`pg_dump -h localhost -U postgres csce315_905_05db > p3db.pgsql`
