

procedure makelasagne:
    objects = ingredients, utensils
    actions = dice, slice, stir, layer, pour
    conditions = hot, cooked
    begin
    for ingredients in makelasagne:
        put(ingredients in utensil)
    if cooked and hot = TRUE put( white sauce on lasagne )     
    if hot + cooked = True 
    _FINISHED