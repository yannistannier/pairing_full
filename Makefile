COMPOSE = docker-compose -p dgfip_pairing


.PHONY: build
build:
	$(COMPOSE) build build-package
	$(COMPOSE) run build-package


.PHONY: format
format:
	$(COMPOSE) build format-imports
	$(COMPOSE) run format-imports
	$(COMPOSE) build format
	$(COMPOSE) run format


.PHONY: style
style:
	$(COMPOSE) build check-format-imports
	$(COMPOSE) run check-format-imports
	$(COMPOSE) build check-format
	$(COMPOSE) run check-format
	$(COMPOSE) build check-style
	$(COMPOSE) run check-style


.PHONY: complexity
complexity:
	$(COMPOSE) build check-complexity
	$(COMPOSE) run check-complexity


.PHONY: security-sast
security-sast:
	$(COMPOSE) build check-security-sast
	$(COMPOSE) run check-security-sast


.PHONY: test-unit
test-unit:
	$(COMPOSE) build test-unit
	$(COMPOSE) run test-unit


.PHONY: test
test: test-unit


.PHONY: clean
clean:
	$(COMPOSE) down --volumes
