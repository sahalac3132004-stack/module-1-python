def details(**kwargs):
    print(f"my name is {kwargs['name']}, i am {kwargs['age']}, my department is {kwargs['department']}")


details(name='sahal', age='22', department='cs')