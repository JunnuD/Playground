let aVariable = 23;
aVariable

aVariable = "An airplane"
aVariable

// You can change your variable type during execution without a problem. 
// No need for int / str etc. 

var oldVariable = 1;
// DO NOT DO THIS OLD WAY

{ let x = 2; }
// x => NOT visible outside of the curly brackets
{ var y = 3; }
// Y => IS visible outside of the curly brackets because of var

const aConstant = 4;
aConstant

aConstant = "A car";
aConstant
//Will cause an error. Since you can't change the value of a constant after it has been declared.

let z;
z // Value of undefined

typeof aVariable
//String

typeof aConstant
//number
