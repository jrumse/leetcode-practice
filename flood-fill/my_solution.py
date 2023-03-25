class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            # if current node is the new color, then return node
            if image[sr][sc] == color:
                return image
            
            # set new color and save old color (don't wanna iterate backwards)
            oldColor = image[sr][sc]
            image[sr][sc] = color

            # iterate left
            if sr - 1 >= 0 and image[sr - 1][sc] == oldColor:
                image = self.floodFill(image, sr - 1, sc, color)

            # iterate right
            if sr + 1 < len(image) and image[sr + 1][sc] == oldColor:
                image = self.floodFill(image, sr + 1, sc, color)

            # iterate up
            if sc - 1 >= 0 and image[sr][sc - 1] == oldColor:
                image = self.floodFill(image, sr, sc - 1, color)

            # iterate down
            if sc + 1 < len(image[sr]) and image[sr][sc + 1] == oldColor:
                image = self.floodFill(image, sr, sc + 1, color)

            # return node
            return image