from package.rectangle import rect_area , rect_perimeter
from package.circle import circle_area , circle_perimeter
from package.d_graphics.cuboid import cuboid_area,  cuboid_perimeter
from package.d_graphics.sphere import sphere_area, sphere_perimeter

print("rectangle area = ", rect_area(5,3),"perimeter = ",rect_perimeter(5,3))
print("circle area = ", circle_area(7),"perimeter = ",circle_perimeter(7))     

print("cuboid area = ", cuboid_area(2,3,4),"perimeter = ",cuboid_perimeter(2,3,4))
print("sphere area = ", sphere_area(6),"perimeter = ",sphere_perimeter(6))
