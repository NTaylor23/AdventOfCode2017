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

with open('inputs/day20.txt', 'r') as file:
    particles = []
    for particle in file.readlines():
        vectors = particle.strip().split(', ') 
        p = Point(tuple(int(n) for n in vectors[0][3:-1].split(',')))
        v = Point(tuple(int(n) for n in vectors[1][3:-1].split(',')))
        a = Point(tuple(int(n) for n in vectors[2][3:-1].split(',')))
        particles.append(Particle(len(particles), p, v, a))

def simulate(particles: list) -> int:
    
    distances: dict = {n : 0 for n in range(len(particles))}
    iteration_count = len(particles) # chosen at random - 1000 particles, 1000 iterations of each particle
    
    for _ in range(iteration_count): 
        closest_point_distance = float('inf')
        for particle in particles:
            particle.update()
            if particle.manhattan_distance_sum() < closest_point_distance:
                closest_point_id = particle.id
                closest_point_distance = particle.manhattan_distance_sum()
        distances[closest_point_id] += 1
    return max(distances, key=lambda k: distances.get(k))

result = simulate(particles)   
print(f'Day 20 Part 1: The particle that remains closest to the origin has an ID of {result}.\n')
