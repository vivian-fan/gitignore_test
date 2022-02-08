import git

repo = git.Repo('.')
remote_refs = repo.remote().refs

repo_heads = repo.heads

print('Current branch is: ', repo.active_branch)

print('All branches are: ')
for head in repo_heads:
    print(head.name)


print('All remote branches are: ')
for refs in remote_refs:
    print(refs.name)

# Now is on feature branch

# Step1: read intent.yml from feature branch

# Step2: merge change from master ./github/intent.yml to feature branch

# Step3: accumulate new intents behind or delete new intents

# Step4: merge the feature branch to master
