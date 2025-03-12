chameleon create_replica_schema  --debug --config config.yaml

chameleon add_source --debug  --config config.yaml --source mysql

chameleon init_replica  --config config.yaml --source mysql
