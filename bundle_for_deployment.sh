#!/usr/bin/env bash

virtualenv -p python3 .env
activate () {
  . ../.env/bin/activate
}
pip install -r requirements.txt
export PROJECTDIR=$(pwd)
cd $VIRTUAL_ENV/lib/python3.5/site-packages
zip -r9 $PROJECTDIR/deployment_bundle.zip *
cd $PROJECTDIR/src
zip -r9 $PROJECTDIR/deployment_bundle.zip *
cd $PROJECTDIR


