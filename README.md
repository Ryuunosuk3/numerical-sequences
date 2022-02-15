# README

This script displays a numerical sequence based on parameters defined by the user.

No modules are required, this is only a simple function just in case someone would need it.
Here are the parameters and what they mean:

  - `n` (int): The number `u0` - or what the first value of the series - will be equal to.
  - `u_var` (str): The `un` operation, like for example `3n+2`. (CAUTION: Please note that in order for the code to work, all math symbols must be included (ex. `3n+2`->`3*n+2`)
  - `nb_rpt` (int): `The nb_rpt` amount of series that will be displayed (ex. `10` -> `u0 + u1 + u2 + ... + u10`)

 ### Here is an example:
  
  series(10, 'n + 3', '3')
    >>> u0 = 10 (n + 3)
        u1 = 13
        u2 = 16
        u3 = 19
