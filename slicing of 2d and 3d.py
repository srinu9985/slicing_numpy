# finding sub arrays from the 2D arrays using slicing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[6, 7, 8, 9, 10]])
print(arr.ndim)
print(arr[1, :4])
print(arr[0,:2])
print(arr[1, 3:5])

# finding sub arrays from the 3D arrays using slicing
arr=np.array([[[1,2,3,4],[5,6,7,8],[9,0,1,2]],[[2,4,56,99],[78,67,56,78],[3,4,5,6]]])
print(arr)
print(arr[1,2:5])
