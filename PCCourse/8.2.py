unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs: #While list is not empty, when empty it will evaluate to False
    current_design = unprinted_designs.pop() #Take the last item of the list, remove it and save it in current_desgn var
    print("Printing model: " + current_design)
    completed_models.append(current_design) #add current design to completed models list

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
