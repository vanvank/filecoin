#!/bin/bash
watch -n 10 'go-filecoin show block $(go-filecoin chain head | head -n 1)'
