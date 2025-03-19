def fret_spacing_calculator(number_of_frets, scale_length):
    #loop start
    fret_number = 1
    distance_from_nut = 0.0

    data = []

    while fret_number <= number_of_frets:

        #rule_eighteen = 17.817
        twelve_two = 1 / 1.059463

        #calc measurements
        fret_to_fret_distance = (scale_length - distance_from_nut) / twelve_two
        nut_to_fret_distance = distance_from_nut + fret_to_fret_distance

        #build data set
        row = {"fret_number":fret_number
            , "fret_to_fret_distance":round(fret_to_fret_distance,3)
            , "nut_to_fret_distance":round(nut_to_fret_distance,3)
            }
        data.append(row)

        #increment loop
        distance_from_nut += fret_to_fret_distance
        fret_number += 1

    return data

#begin

#inputs
input_number_of_frets = int(input("Number of frets: "))
input_scale_length = float(input("Scale Length: "))

print(fret_spacing_calculator(input_number_of_frets, input_scale_length))