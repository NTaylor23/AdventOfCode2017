import multiprocessing
import time 

def program(
    values, 
    instructions, 
    pipe, 
    deadlock_counter, 
    deadlock_lock,
    queue, 
    id
):    
    # Give each process its own data - no shared resources
    values = values.copy()
    
    # Set the value of `p` to the Process ID
    values['p'] = id
    
    operation_map = {
        # set, add, multiply or modulo
        'set': lambda x, y: values.__setitem__(x, y),
        'add': lambda x, y: values.__setitem__(x, values[x] + y),
        'mul': lambda x, y: values.__setitem__(x, values[x] * y),
        'mod': lambda x, y: values.__setitem__(x, values[x] % y),
    }

    def get_value(val):
        if not val.strip('-').isnumeric():
            return values[val]
        return int(val)

    idx, count = 0, 0    
    while idx < len(instructions):
        
        current_line = instructions[idx]
        
        # Set the instruction, and the first (`x`) value
        inst, x = current_line[0], current_line[1][0]
    
        # Set y if it exists in the instruction
        if len(current_line[1]) > 1:
            y = current_line[1][1] 
        
        # Parse instructions
        if inst == 'rcv':
            # Accept value from other process
            if pipe.poll(0.01):
                val = pipe.recv()
                values[x] = val
            else:
                # Watch for deadlock
                with deadlock_lock:
                    deadlock_counter.value += 1
                    if deadlock_counter.value >= 2:
                        # Terminate if both processes are blocked
                        break
                    time.sleep(0.01)
        elif inst == 'snd':
            # Send value to other process and increment count
            pipe.send(get_value(x))
            count += 1
        elif inst == 'jgz' and get_value(x) > 0:
            # Jump `y` indices
            idx += get_value(y)
            continue
        elif inst in operation_map: 
            # set, add, multiply or modulo
            y = get_value(y)
            operation_map[inst](x, y)
        idx += 1
    queue.put(count)

def main():
    values, instructions = {}, {}

    with open('inputs/day18.txt', 'r') as file:
        for idx, line in enumerate(file.readlines()):
            command, *vars = line.split()
            values[vars[0]] = 0
            instructions[idx] = [command, vars]
    
    with multiprocessing.Manager() as manager:
        parent, child = multiprocessing.Pipe()
        queue = multiprocessing.Queue()
        deadlock_counter = manager.Value("i", 0)
        deadlock_lock = manager.Lock()

        p1 = multiprocessing.Process(target=program, args=(
            values, 
            instructions, 
            parent, 
            deadlock_counter, 
            deadlock_lock,
            queue, 
            0
        ))
        
        p2 = multiprocessing.Process(target=program, args=(
            values, 
            instructions, 
            child, 
            deadlock_counter, 
            deadlock_lock,
            queue, 
            1
        ))
        
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        
        result = queue.get()
        print(f'Day 18 Part 2: Program 1 sent a value {result} times.\n')

if __name__ == '__main__':
    main()