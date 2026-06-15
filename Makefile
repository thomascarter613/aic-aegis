.PHONY: doctor check dev test fmt lint clean

doctor:
	bash scripts/doctor.sh

check:
	bash scripts/check.sh

dev:
	bash scripts/dev.sh

test:
	bash scripts/test.sh

fmt:
	bash scripts/format.sh

lint:
	bash scripts/lint.sh

clean:
	rm -rf .aic/runtime .aic/tmp logs tmp
