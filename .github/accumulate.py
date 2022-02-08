import git

repo = git.Repo('.')
remote_refs = repo.remote().refs

print('All remote branches as following: ')
for refs in remote_refs:
    print(refs.name)

# Now is on feature branch

# Step1: read intent.yml from feature branch

# Step2: merge change from master ./github/intent.yml to feature branch

# Step3: accumulate new intents behind or delete new intents

# Step4: merge the feature branch to master
