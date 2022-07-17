# code templates
gen_temp:
	# generate code from models
	# ex: make gen_temp app=clinic.userapp
	python manage.py generator app $(app)
gen_temp_all:
	for app in clinic.userapp; do \
		python manage.py generator app $$app ; \
	done

# docker compose in development
build_dev:
	./compose/local/build.sh
dev:
	docker-compose -f local.yml up
dev_down:
	docker-compose -f local.yml down
test:
	docker-compose -f local.yml run web pytest

cbe:
	docker-compose -f $(file) exec web /bin/bash
cdb:
	docker-compose -f $(file) exec db /bin/bash
lbe: # make lbe file=local.yml
	docker-compose -f $(file) logs -f web
ldb:
	docker-compose -f $(file) logs -f db

# docker ocompose in production
# docpush:
# 	docker build -t registry.gitlab.com/bit68/clinic .
# 	docker push registry.gitlab.com/bit68/clinic
build_prod:
	./compose/production/build.sh
start_prod:
	./compose/production/build.sh
	docker-compose -f production.yml up -d
restart_prod:
	./compose/production/build.sh
	docker-compose -f production.yml up --no-deps -d web
