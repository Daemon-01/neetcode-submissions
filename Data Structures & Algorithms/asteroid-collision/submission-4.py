class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and self.collide(stack[-1],asteroid):
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack


    def collide(self,top,asteroid):
        return (top > 0 and asteroid < 0 )