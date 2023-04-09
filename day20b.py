from collections import Counter

class Point:
    def __init__(self, coordinates) -> None:
        self.x, self.y, self.z = coordinates

class Particle:
    def __init__(self, id: int, position: Point, velocity: Point, acceleration: Point) -> None:
        self.id = id
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
    
    def manhattan_distance_sum(self) -> int:
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

    def update(self) -> None:
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z
        
    def get_position(self) -> tuple:
        return (self.position.x, self.position.y, self.position.z)

with open('inputs/day20.txt', 'r') as file:
    particles = []
    for particle in file.readlines():
        vectors = particle.strip().split(', ') 
        p = Point(tuple(int(n) for n in vectors[0][3:-1].split(',')))
        v = Point(tuple(int(n) for n in vectors[1][3:-1].split(',')))
        a = Point(tuple(int(n) for n in vectors[2][3:-1].split(',')))
        particles.append(Particle(len(particles), p, v, a))

def simulate(particles: list) -> int:
    
    particle_exists = [True] * len(particles)
    iteration_count = len(particles) // 2

    for _ in range(iteration_count): 
        locations = {}
        for idx, particle in enumerate(particles):
            if particle_exists[idx]:
                particle.update()
                pos = particle.get_position()
                if pos in locations.keys():
                    particle_exists[idx] = False
                    particle_exists[locations[pos]] = False
                else:
                    locations[pos] = idx
    
    return sum(n for n in particle_exists)
                
result = simulate(particles)   
print(f'Day 20 Part 2: There are {result} particles remaining after resolving all collisions.\n')