import random

class Space():

    def __init__(self, height, width, num_hospitals):
        """Create a new state space with given dimensions."""
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set()
        self.hospitals = set()

    def add_house(self, row, col):
        """Add a house at a particular location in state space."""
        self.houses.add((row, col))

    def available_space(self):
        """Returns all cells not currently used by a house ò hospital."""

        # Consider all posible cells
        candidate = set(
            (row, col)
            for row in range(self.height)
            for col in range(self.width)
        )

        # Remove all houses and hospitals
        for house in self.houses:
            candidate.remove(house)
        for hospital in self.hospitals:
            candidate.remove(hospital)

        return candidate

    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        """Performs hill-climbing to find a solution."""
        count = 0

        # Start by initializing hospitals randomly
        self.hospitals = set()
        for i in range(self.num_hospitals):
            self.hospitals.add(random.choice(list(self.available_space())))
        if log:
            print("Initial Solution: Cost", self.get_cost(self.hospitals))
        
        if image_prefix:
            self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")
    

        # Comtinue until we reach muaximum number iterations
        while maximum is None or count < maximum:
            count += 1
            best_neighbors = []
            best_neighbor_cost = None

            # Consider all hospitals to move
            for hospital in self.hospitals:

                # Consider all neighbors for that hospital
                for replacement in self.get_neighbors(*hospital):
                    neighbor = self.hospitals.copy()
                    neighbor.remove(hospital)
                    neighbor.add(replacement)

                    # Check ì neighbor is best so far
                    cost = self.get_cost(neighbor)
                    if best_neighbor_cost is None or cost < best_neighbor_cost:
                        best_neighbor_cost = cost
                        best_neighbors = [neighbor]
                    elif best_neighbor_cost == cost:
                        best_neighbors.append(neighbor)

            # None of the neighbors are better than the current state
            if best_neighbor_cost >= self.get_cost(self.hospitals):
                return self.hospitals
            
            # Move to a highest-valued neighbor
            else:
                if log:
                    print(f"Found better neighbor: cost {best_neighbor_cost}")
                # Stochastic
                self.hospitals = random.choice(best_neighbors)
            
            # Generate image
            if image_prefix:
                self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")
            

    def random_restart(self, maximum, image_prefix=None, log=False):
        """Repeat hill-climbing multiple times."""
        best_hospitals = None
        best_cost = None

        # Repeat hill-climbng a fixxed number of times
        for i in range(maximum):
            hospitals = self.hill_climb()
            cost = self.get_cost(hospitals)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_hospitals = hospitals
                if log:
                    print(f"{i}: Found new best state: cost {cost}")
            else:
                if log:
                    print(f"{i}: Found state: cost {cost}")
            
            if image_prefix:
                self.output_image(f"{image_prefix}{str(i).zfill(3)}.png")
            
            
        return best_hospitals
        
    def get_cost(self, hospitals):
        """Calculate sum of distances from houses to nearest hospital."""
        cost = 0
        for house in self.houses:
            cost += min(
                abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
                for hospital in hospitals
            )
        return cost
    
    def get_neighbors(self, row, col):
        """Return neighbors not already containing a housse of hospital."""
        candidate = [
            (row+1, col),   # Down
            (row-1, col),   # Up
            (row, col+1),   # Right
            (row, col-1)    # Left
        ]
        neighbors = []
        for r, c in candidate:
            if (r, c) in self.houses or (r, c) in self.hospitals:
                continue
            if 0 <= r <= self.height and 0 <= c <= self.width:
                neighbors.append((r, c))
        return neighbors

    
    def output_image(self, filename):
        """Generate image with all houses and hospitals."""
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "black"
        )
        house = Image.open("assets/images/New_House.png").resize((cell_size, cell_size))
        hospital = Image.open("assets/images/New_Hospital.png").resize((cell_size, cell_size))
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):

                # Deaw cell
                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="white")

                if (i, j) in self.houses:
                    img.paste(house, rect[0], mask=house)
                if (i, j) in self.hospitals:
                    img.paste(hospital, rect[0], mask=hospital)
                
        # Add cost
        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "black"
        )
        draw.text(
            (padding, self.height * cell_size + padding),
            f"Cost: {self.get_cost(self.hospitals)}",
            fill="white",
            font=font
        )
        img.save(filename)
    
random.seed(40)
# Create a new space and add houses randomly
s = Space(height=10, width=20, num_hospitals=3)
for i in range(15):
    s.add_house(random.randrange(s.height), random.randrange(s.width))

# Use local search to determine hospital placement
Hospitals = s.random_restart(image_prefix="hospitals", log=True, maximum=20)

# rm *.png
