import build_data
from build_data import get_data  # Use the get_data function to load the dataset
import sys


def filter_gt(data:list[build_data.CountyDemographics], field:str,level:str, value:float) ->list[build_data.CountyDemographics]:
    #This function takes data and filters the data with the fields of a level greater than the value
    #This function takes in a list of CountyDemographics, a field in the CountyDemographics, a specific value in the field, then the value is float used to filter.
    #def filter_gt(data:list[build_data.CountyDemographics], field:str,level:str, value:float) ->list[build_data.CountyDemographics]:
    #return filtered_data
    #If list of data, field "education", level "Bachelor's Degree or Higher", value "60", then a return of all the counties within data will have a greater than 60 Bachelor's Degree or Higher.
    filtered_data = [county for county in data if getattr(county, field)[level] > value]
    print(f"Filter: {field} gt {value} ({len(filtered_data)} entries)")
    return filtered_data

def filter_lt(data:list[build_data.CountyDemographics], field:str,level:str , value:float) -> list[build_data.CountyDemographics]:
    #This function takes data and filters the data with fields of a level lower than the value given.
    #This function takes in a list of CountyDemographics, a field in the CountyDemographics, a specific value in the field, then the value is a float used to filter.
    #def filter_lt(data:list[build_data.CountyDemographics], field:str,level:str , value:float) -> list[build_data.CountyDemographics]:
    #return filtered_data
    #If the list of data, field "education", level "High School or Higher", value "60", then a list of all the countys with values of education for Higher or Higher lower than 60.
    filtered_data = [county for county in data if getattr(county, field)[level] < value]
    print(f"Filter: {field} lt {value} ({len(filtered_data)} entries)")
    return filtered_data

def filter_state(data:list[build_data.CountyDemographics], state_abbr:str) -> list[build_data.CountyDemographics]:
    #This function takes data and filters the data seperating all counties residing in the given state.
    #This function takes in a list of CountyDemographics and filters out all of the states.
    #def filter_state(data:list[build_data.CountyDemographics], state_abbr:str) -> list[build_data.CountyDemographics]:
    #return filtered data
    #If the list of data and string "CA", the function will return every county within "CA".
    filtered_data = [county for county in data if county.state == state_abbr]
    print(f"Filter: state == {state_abbr} ({len(filtered_data)} entries)")
    return filtered_data

def population_total(data:list[build_data.CountyDemographics])-> list[build_data.CountyDemographics]:
    #This function takes data and prints the total population of all the counties within the data.
    #This function takes in a list of CountyDemographics.
    #def population_total(data:list[build_data.CountyDemographics])-> list[build_data.CountyDemographics]:
    #If a list CountyDemographics is input, the same list will be returned along with a print statement of the total population within the list.
    total = 0.0
    for county in data:
        total += county.population['2014 Population']
    print(f"2014 population: {total}" )
    return data

def population(data:list[build_data.CountyDemographics], field:str, level:float) -> list[build_data.CountyDemographics]:
    #This function takes a list of CountyDemographics and returns the same list while printing a float of the popualtion of a specifc field and level will be printed.
    #This function takes in a list of CountyDemographics, a string as field, and float as level.
    #def population_total(data:list[build_data.CountyDemographics])-> list[build_data.CountyDemographics]:
    #return list of CountyDemographics
    #If a list of CountyDemographics is input, the same list will be returned and a float of the filtered population will be printed.
    fil_pop = 0.0
    for county in data:
        fil_pop += getattr(county, field)[level] * county.population['2014 Population']
    print(f"2014 {field}.{level}: {fil_pop}")
    return data

def percent(data:list[build_data.CountyDemographics], field:str, level:str) -> list[build_data.CountyDemographics]:
    #This function takes a list of CountyDemographics and returns the same list while printing a float of the popoluation percentage of a specific field and level.
    #This function takes in a list of CountyDemographics, string as field, and a string as level.
    #def percent(data:list[build_data.CountyDemographics], field:str, level:str) -> list[build_data.CountyDemographics]:
    #return a list of CountyDemographics
    #If a list of CountyDemographics, "education" as field, and "High School or Higher" as level
    fil_pop = 0.0
    for county in data:
        fil_pop += getattr(county, field)[level] * county.population['2014 Population']

    total = 0
    for county in data:
        total += county.population['2014 Population']
    if total == 0:
        percent = 0.0
    else:
        percent = fil_pop / total
    print(f"2014 {field}.{level}: {percent}")
    return data



def display(data:list[build_data.CountyDemographics]):
    #This function displays the counties in an easy and readable way.
    #This function takes a list of County Demographics as data and prints string.
    #def display(data:list[build_data.CountyDemographics]):
    #If a list of CountyDemographics is put in, then a readable version of every county in the list will be printed.
    if not data:
        print("No entries to display.")
        return None
    for county in data:
        print(f"County: {county.county}, State: {county.state}")
        print(f"  Education: {county.education}")
        print(f"  Ethnicities: {county.ethnicities}")
        print(f"  Income: {county.income}")
        print(f"  Population: {county.population}")
        print("-" * 40)

def main():
    #Check if an operations file is provided
    if len(sys.argv) < 2:
        print("Error: No operations file provided.")
        sys.exit(1)

    operations_file = sys.argv[1]
    #operations_file = "inputs/bachelors_gt_60.ops"
    #operations_file = "inputs/ca.ops"
    #operations_file = "inputs/filter_state.ops"
    #operations_file = "inputs/high_school_lt_60.ops"
    #operations_file = "inputs/percent_fields.ops"
    #operations_file = "inputs/pop.ops"
    #operations_file = "inputs/pop_field.ops"
    #operations_file = "inputs/some_errors.ops"
    #operations_file = "inputs/task2_a.ops"
    #operations_file = "inputs/task2_b.ops"
    #operations_file = "inputs/task2_c.ops"
    #operations_file = "inputs/task2_d.ops"

    # Load the dataset
    data = get_data()
    # Try the operation file
    try:
        with open(operations_file, "r")as file:
            print(len(data), "records loaded")
            for line in file:
                line = line.strip()
                if not line:  # Skip blank lines
                    continue
                parts = line.split(":")
                operation = parts[0]

                # Handle operations
                if operation == "filter-gt":
                    specifc = parts[1].split(".")
                    field = specifc[0]
                    value = float(parts[2])
                    level = specifc[1]
                    data = filter_gt(data, field.lower(), level, value)
                elif operation == "filter-lt":
                    specifc = parts[1].split(".")
                    field = specifc[0]
                    value = float(parts[2])
                    level = specifc[1]
                    data = filter_lt(data, field.lower(), level, value)
                elif operation == "filter-state":
                    state_abbr = parts[1]
                    data = filter_state(data, state_abbr)
                elif operation == "population-total":
                    data = population_total(data)
                #elif operation == "population":
                elif operation == "population":
                    specifc = parts[1].split(".")
                    field = specifc[0]
                    level = specifc[1]
                    data = population(data, field.lower(), level)
                elif operation == "percent":
                    specifc = parts[1].split(".")
                    field = specifc[0]
                    level = specifc[1]
                    data = percent(data, field.lower(), level)
                elif operation == "display":
                    display(data)
                else:
                    print(f"Error: Unsupported operation '{operation}'")
    except FileNotFoundError:
        print(f"Error: Cannot open file '{operations_file}'")
    except Exception as e:
        print(f"Error processing operations file: {e}")

if __name__ == "__main__":
    main()