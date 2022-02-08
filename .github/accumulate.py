#!/usr/bin/python
# -*- coding: utf-8 -*-
import git
import yaml

repo = git.Repo('.')
remote_refs = repo.remote().refs

repo_heads = repo.heads

print ('Current branch is: ', repo.active_branch)

print 'All branches are: '
for head in repo_heads:
    print head.name

print 'All remote branches are: '
for refs in remote_refs:
    print refs.name

with open('./.github/intent.yml', 'r') as f:
    print ('internal on master ', yaml.safe_load(f))

# Now is on feature branch

branch_name = 'feature-1'
origin = repo.remotes.origin
new_branch = repo.create_head(branch_name, origin.refs[branch_name])
new_branch.checkout()

print ('Current branch is: ', repo.active_branch)

with open('./intent.yml', 'r') as f:
    print ('internal on feature branch ', yaml.safe_load(f))

# Step1: read intent.yml from feature branch

# Step2: merge change from master ./github/intent.yml to feature branch

# Step3: accumulate new intents behind or delete new intents

# Step4: merge the feature branch to master
