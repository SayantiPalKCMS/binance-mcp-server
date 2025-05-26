#!/bin/bash

commit_msg_file="$1"
commit_msg=$(cat "$commit_msg_file")
pattern='^(feat|fix|docs|test|refactor|chore|style|perf)\([a-zA-Z0-9_-]+\): .{1,72}$'

if ! echo "$commit_msg" | grep -Eq "$pattern"; then
    echo "ERROR: Invalid commit message format."
    echo ""
    echo "Use format: <type>(<scope>): <subject>"
    echo "Example: fix(api): correct status code handling"
    exit 1
fi
