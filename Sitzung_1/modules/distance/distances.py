import math

class Distance:
    def helloWorld(self):
        print('Hello, World!')

    def euclidianDistance(self,p,q):
        """Calculates eucledian distance between two n-dimensional vectors. 
        The vectors are represented as list of integers or floats.
        Example: 
            distance.euclidianDistance([1, 2],[3,4])
            Distance is 2.8284271247461903."""
        squares = [ (p[i] - q[i])**2 for i in range(len(p)) ]
        summed_squares = sum(squares)
        distance = math.sqrt(summed_squares)
        print(f'Distance is {distance}.')
        return distance


if (__name__ == '__main__'):
    print('Executing as standalone script')
