## W5 – Truth Tables

**Due**: 29 Oct by 11:59  
**Points**: 55  
**Submitting**: file upload (`.doc`, `.docx`, `.pdf`)  
**Available**: after 8 Oct at 7:00  

Submit answers to the following questions in a single document.

---

### Section 1: Truth Tables from Logic Diagrams

1. Choose **two Boolean expressions** with at least **three variables**.  
2. Draw the **logic gate diagrams** and construct the corresponding **truth tables**.  
3. Use the truth tables to **simplify the expressions**.  
4. Label all **inputs** and **outputs** clearly.  
5. You may use the following tools:
   - [Function to logic circuit converter](https://madformath.com/calculators/digital-systems/boolean-functions/function-to-logic-circuit-converter)  
   - [Function to truth table converter](https://madformath.com/calculators/digital-systems/boolean-functions/function-to-truth-table-converter)

#### Question 1  [12]

Given the following logic circuit, construct its truth table and derive the corresponding Boolean expression.

- \(A \land B \lor (\lnot A \land C)\)  
- Draw a logic diagram based on this Boolean expression.  
- Identify and describe any **redundant terms** in the expression.  

#### Question 2  [8]

Convert the following Boolean expressions into truth tables and simplify them using logical equivalences:

1. \((A \lor B) \land (A \lor \lnot B)\)  
2. \((A \land B) \lor (A \land \lnot B)\)  

For each case, verify using a truth table that the simplified expression produces the **same output** as the original.

---

### Section 2: Karnaugh Maps and Algebraic Simplification

1. Choose **two expressions** and create their **truth tables**.  
2. Draw **Karnaugh maps (K-maps)** and simplify using grouping.  
3. Apply **Boolean algebra rules** to verify the simplifications.  

#### Question 3  [9]

A vending machine releases a product only if the user inserts the correct amount and selects an available item. The inputs are:

- \(A = 1\) if the correct amount is inserted.  
- \(B = 1\) if an item is selected.  
- \(C = 1\) if the item is available.  

The output \(X\) should be 1 only if the vending machine should dispense the item.

1. Construct a **truth table** for the system.  
2. Write a **Boolean expression** for the output \(X\).  
3. **Simplify** the expression using Boolean algebra and **verify** using a truth table.  

#### Question 4  [12]

The following truth table represents a digital circuit:

| A | B | C | Output |
|---|---|---|--------|
| 0 | 0 | 0 |   0    |
| 0 | 0 | 1 |   1    |
| 0 | 1 | 0 |   1    |
| 0 | 1 | 1 |   1    |
| 1 | 0 | 0 |   0    |
| 1 | 0 | 1 |   1    |
| 1 | 1 | 0 |   1    |
| 1 | 1 | 1 |   1    |

1. Draw a **Karnaugh map (K-map)** for the given truth table.  
2. Identify and **group adjacent 1s** to simplify the Boolean expression.  
3. Write the **simplified Boolean expression** using AND, OR, NOT operations.  

#### Question 5  [8]

A digital security system activates an alarm if:

- A door is opened \((A = 1)\), **or**  
- A window is broken \((B = 1)\) **and** motion is detected \((C = 1)\).  

1. Write the **Boolean expression** for the alarm activation system.  
2. Construct a **truth table** for this system.  
3. **Simplify** the expression using Karnaugh maps and Boolean algebra.  
4. Draw the **simplified logic circuit**.  

#### Question 6  [6]

Explain why **Karnaugh maps** are often preferred over Boolean algebra for simplifying logic expressions in **complex circuits**.  

Include a **real-world example** where Karnaugh map simplification has led to improved performance in a system (for example, in **CPU design**, **networking**, or **automation**).

