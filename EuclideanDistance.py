import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def main():
    
    points = [
        (3, 5),
        (9, 6),
        (2, 4),
        (0, 1),
        (8, 2)
    ]

    
    distances = []

   
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append((points[i], points[j], distance))


    min_distance = min(distances, key=lambda x: x[2])

   
    print("Noktalar arasındaki Öklid mesafeleri:")
    for point1, point2, distance in distances:
        print(f"{point1} ile {point2} arasındaki mesafe: {distance:.2f}")

    print(f"\nMinimum mesafe: {min_distance[2]:.2f}")
    print(f"Bu mesafe {min_distance[0]} ile {min_distance[1]} noktaları arasındadır.")

if __name__ == "__main__":
    main()
