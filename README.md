# README  
## Dataset Description  

### Columns  
Type -
X - x coordinate of particle position (cm)  
Y - y coordinate of particle position (cm)  
Z - z coordinate of particle position (cm)  
U - Particle x axis direction cosine   
V - Particle y axis direction cosine  
W - Particle z axis direction cosine  
Energy - 
Weight - 
Cell - 
Material - 
Time - Time at the particle position (shakes)  

Page 586  

### Type Column
SRC #1000 source (new particle spawn)  
BNK #2000 Bank - the birth of a secondary particle track.  
SUR #3000 surface crossed  
COL #4000 collision  
TER #5000 termination  

Page 584 & 890  

## Input File Desciption 

The MCNP input consists of one optional and three required blocks. A single blank line is used as a delimiter between blocks and as an optional input-file terminator. A $ (dollar sign) terminates data entry on a line. Anything on the line that follows the $ is interpreted as a comment and ignored by the code. Comment lines must have a c somewhere in columns 1–5 followed by at least one space and can be a total of 128 columns long.  

Page 225-226  

### Cell Cards
The cell number is the first entry and must begin in the first five columns. The next entry is the cell material number, which is arbitrarily assigned by the user. The corresponding material is described on a material ( M ) card with the same material number. If the cell is a void, a zero is entered for the material number. The cell and material numbers cannot exceed eight digits each. Following the material number is the cell material density. A positive entry is interpreted as atom density in units of 1024 atoms/cm3. A negative entry is interpreted as mass density in units of g/cm3. There is no density entry for a void cell. After the material density, a complete specification of the geometry of the cell follows. This specification includes a list of the signed surfaces bounding the cell where the sign denotes the sense of the regions defined by the surfaces. The regions are combined with the Boolean intersection and union operators. A space indicates an intersection and a colon indicates a union.   

Page 226. Page 257-258: Table 5.2  

### Surface Cards
The surface number is the first entry. The surface number must begin in columns 1–5 and not exceed eight digits. The surface number is followed by an alphabetic mnemonic entry that indicates the surface type. The surface type is followed by the numerical coefficients of the equation of the surface, in the required order.  

Page 227. Page 260: Table 5.3.1  

### Data Cards
The card name must begin within the first five columns. No data card can be used more than once with the same number or particle type designations.  