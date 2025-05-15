# 7. To-Do List Organizer
tasks=[]
priority=[]
state=[]

def add_task(): 
    task=input("enter the thats to added")
    p=int(input("what is the priority of the task in a escale of 1 to 10"))
    s=(input)("what is the status of the task. can be:(started, pending, complete): ")
    tasks.append(task)
    priority.append(p)
    state.append(s)

def complete_task():
    look=input("enter the task to search for it")
    for i in range(len(tasks)):
        if look==tasks[i]:
             state[i]="complete"
             break
    
def filter_tasks(): 
    state_started=[]
    state_pending=[]
    state_complete=[]
    for i in range(len(tasks)):
        if state[i]=="started":
            state_started.append(tasks[i])
        elif state[i]=="pending":
            state_pending.append(tasks[i])
        elif state[i]=="complete":
            state_complete.append(tasks[i])
    print(f"the tasks in status started are {state_started}")
    print(f"the tasks in status pending are {state_pending}")
    print(f"the tasks in status complete are {state_complete}")
