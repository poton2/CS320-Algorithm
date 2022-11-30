# CS320-Algorithm

# PA1 Line of sight 

Givenn an array, X[i,j] of the elevations of points in a (hilly)
terrain, and n information about where the sun currently is,
determine, for each point, whether it is sunlit or in
the shade.

The azimuth is due west, Φ = 270°. So only points to the west
(i.e., on the i
th row) can cast a shadow on [i, j]

### Inputs

n Y[i, j] is an n x n array of (floating point) numbers (in meters)

n The angle of elevation of the sun Θ ≤ 90°

n The angle of azimuth of the sun, Φ

n The horizontal distance (in meters) between adjacent points, d,
(the resolution or scale of our data)

### Output:

n S[i, j] an n x n array of Booleans:

n If [i, j] is in the shade, S[i, j] is 1

n Otherwise it is 0

