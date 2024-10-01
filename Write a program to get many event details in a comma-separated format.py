'''Filter Events

Write a program to get many event details in a comma-separated format. But get only specific events based on some classifications in ‘|’ separated format. Get the event details in comma separated format and get event name/event type/organizer and display the events with the specified details in ‘|’ separated format.
 

Input Format:
The first line of input corresponds to the number of events 'n'.
The next 'n' line of input corresponds to the event details in the CSV format of (Event Name, Event Type, Orgnaizer Name).
The next line of input corresponds to the type of filtering 'm'. Types→ using event name, using event type, using organizer name.
The next line corresponds to the name of filtering.
Refer to sample input for formatting specifications.

Output Format:
The output consists of filtered event details separated by  "|". If no event is there for specified search, then display as "No results found".
Refer to sample output for formatting specifications.
 

Problem Constraints:
n > 0 , else display as "Invalid Input".
m > 0 and m < 4 , else display as "Invalid Input".
 

Sample Input/Output-1:

Enter number of events
4
Enter event details in CSV(Event Name,Event Type,Orgnaizer Name)
Lulu,Fun party,William
Maazdha,Birthday,Edilbert
Shadhi Mela,Wedding,Yadu singla
Lulu,Wedding,Edilbert
Filter:
1)Using Event name
2)Using Event type
3)Using Organizer name
Choice:
3
Enter value:
Edilbert
Maazdha|Birthday|Edilbert
Lulu|Wedding|Edilbert
 

Sample Input/Output-2:

Enter number of events
4
Enter event details in CSV(Event Name,Event Type,Orgnaizer Name)
Lulu,Fun party,William
Maazdha,Birthday,Edilbert
Shadhi Mela,Wedding,Yadu singla
Lulu,Wedding,Edilbert
Filter:
1)Using Event name
2)Using Event type
3)Using Organizer name
Choice:
5'''
def filter_events():
    try:
        # Read number of events
        n = int(input("Enter number of events\n"))
        if n <= 0:
            print("Invalid Input")
            return
        
        # Read event details
        events = []
        print("Enter event details in CSV(Event Name,Event Type,Orgnaizer Name)")
        for _ in range(n):
            event = input().strip()
            events.append(event.split(','))
        
        # Read filtering choice
        print("Filter:")
        print("1) Using Event name")
        print("2) Using Event type")
        print("3) Using Organizer name")
        choice = int(input("Choice:\n"))
        if choice < 1 or choice > 3:
            print("Invalid Input")
            return
        
        # Read filtering value
        value = input("Enter value:\n").strip()
        
        # Define filter index based on choice
        filter_index = choice - 1
        
        # Use lambda function for filtering
        filtered_events = list(filter(lambda event: event[filter_index].strip() == value, events))
        
        # Print the filtered events
        if filtered_events:
            for event in filtered_events:
                print("|".join(event))
        else:
            print("No results found")
    except Exception as e:
        print("Invalid Input")

# Run the function
filter_events()