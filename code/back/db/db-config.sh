#! /bin/bash

psql --command 'DROP DATABASE "ing-software";'

createdb 'ing-software'

psql --dbname 'ing-software' --file './create.sql'
psql --dbname 'ing-software' --file './init.sql'