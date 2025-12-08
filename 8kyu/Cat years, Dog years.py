def human_years_cat_years_dog_years(human_years):
    catYear = 0
    dogYear = 0
    if human_years == 1:
        catYear = 15
        dogYear = 15
    elif human_years == 2:
        catYear = 15 + 9
        dogYear = 15 + 9
    else:
        catYear = 15 + 9 + (human_years - 2) *4
        dogYear = 15 + 9 + (human_years - 2) *5
    return [human_years,catYear,dogYear]
