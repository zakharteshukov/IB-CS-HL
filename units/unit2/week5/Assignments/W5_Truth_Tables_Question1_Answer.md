# Section 1: Truth Tables from Logic Diagrams

## Question 1 [12 points]

Given the Boolean expression: \(A \land B \lor (\lnot A \land C)\)

### a) Truth Table

| A | B | C | A ∧ B | ¬A ∧ C | X = (A ∧ B) ∨ (¬A ∧ C) |
|---|---|---|-------|--------|------------------------|
| 0 | 0 | 0 |   0   |   0    |           0            |
| 0 | 0 | 1 |   0   |   1    |           1            |
| 0 | 1 | 0 |   0   |   0    |           0            |
| 0 | 1 | 1 |   0   |   1    |           1            |
| 1 | 0 | 0 |   0   |   0    |           0            |
| 1 | 0 | 1 |   0   |   0    |           0            |
| 1 | 1 | 0 |   1   |   0    |           1            |
| 1 | 1 | 1 |   1   |   0    |           1            |

**Explanation of the truth table:**
- Column `A ∧ B`: This is 1 only when both A and B are 1 (rows 7 and 8).
- Column `¬A ∧ C`: This is 1 only when A is 0 AND C is 1 (rows 2 and 4). Note: When A=0, ¬A=1, so ¬A ∧ C = 1 only when C=1.
- Column `X`: This is the final output, which is 1 when either `A ∧ B` is 1 OR `¬A ∧ C` is 1.

### b) Boolean Expression

**Deriving the Boolean expression from the truth table:**

Looking at the truth table, we can see that X = 1 in the following cases:
- Row 2: A=0, B=0, C=1 → This is the case where (¬A ∧ C) = 1
- Row 4: A=0, B=1, C=1 → This is the case where (¬A ∧ C) = 1
- Row 7: A=1, B=1, C=0 → This is the case where (A ∧ B) = 1
- Row 8: A=1, B=1, C=1 → This is the case where (A ∧ B) = 1

**The Boolean expression derived from the logic circuit is:**

\[X = (A \land B) \lor (\lnot A \land C)\]

**Alternative notations:**
- Using multiplication and addition: \(X = AB + \overline{A}C\)
- Using parentheses for clarity: \(X = (A \cdot B) + (\overline{A} \cdot C)\)

**In words:** The output X is 1 when (A AND B) is true, OR when (NOT A AND C) is true.

**Verification:**
- When A=1 and B=1: The first term (A ∧ B) = 1, so X = 1 regardless of C
- When A=0 and C=1: The second term (¬A ∧ C) = 1, so X = 1 regardless of B
- All other combinations result in X = 0

This matches the truth table results perfectly.

### c) Logic Diagram

**What is a logic diagram?**
A logic diagram shows how the Boolean expression is implemented using logic gates. Each gate performs a specific operation (AND, OR, NOT).

**Breaking down the expression:** \(X = (A \land B) \lor (\lnot A \land C)\)

**Step-by-step construction:**

1. **Inputs**: Three input variables A, B, and C enter from the left
2. **First AND gate**: Takes inputs A and B, produces output (A ∧ B)
3. **NOT gate**: Takes input A, produces output ¬A
4. **Second AND gate**: Takes inputs ¬A and C, produces output (¬A ∧ C)
5. **OR gate**: Takes inputs (A ∧ B) and (¬A ∧ C), produces final output X

**Textual representation:**
```
    A ──────────┐
                │
                ├──[AND]──────────┐
    B ─────────┘                 │
                                  │
    A ────[NOT]──┐                │
                 │                │
                 ├──[AND]─────────┤
    C ───────────┘                │
                                  │
                                  ├──[OR]── X
                                  │
                                  │
```

**Visual representation using standard gate symbols:**

```
         A ────┐
              │
              ├───[AND]───┐
         B ───┘           │
                          │
         A ────[NOT]───┐   │
                       │   │
                       ├───[AND]───┐
         C ────────────┘           │
                                 │
                                 ├───[OR]─── X
                                 │
```

**Gate symbols reference:**
- **NOT gate**: Triangle with a circle (inverter)
- **AND gate**: D-shaped symbol with inputs on left, output on right
- **OR gate**: Curved D-shaped symbol with inputs on left, output on right

**How to create a professional diagram:**

1. **Option 1 - Online tool (Recommended):**
   - Visit: https://madformath.com/calculators/digital-systems/boolean-functions/function-to-logic-circuit-converter
   - Enter the expression: `(A AND B) OR (NOT A AND C)`
   - The tool will generate a visual diagram that you can copy or screenshot

2. **Option 2 - Draw manually:**
   - Use drawing software (like draw.io, Lucidchart, or even PowerPoint)
   - Draw the gates using standard symbols
   - Connect inputs to outputs with lines
   - Label all inputs (A, B, C) and the output (X)

**Description of the circuit:**
The logic circuit implements the expression \(X = (A \land B) \lor (\lnot A \land C)\) using:
- 1 NOT gate (to invert A)
- 2 AND gates (one for A∧B, one for ¬A∧C)
- 1 OR gate (to combine the two AND outputs)

### d) Redundant Terms

**What are redundant terms?**
A redundant term is a part of a Boolean expression that can be removed without changing the output. If removing a term doesn't affect the truth table, that term is redundant.

**Analysis of the expression:** \(X = (A \land B) \lor (\lnot A \land C)\)

**Testing if `(A ∧ B)` is redundant:**
If we remove `(A ∧ B)`, we'd have: \(X = (\lnot A \land C)\)

Let's check the truth table for this simplified expression:

| A | B | C | ¬A ∧ C | Original X | Match? |
|---|---|---|--------|-----------|---------|
| 0 | 0 | 0 |   0    |     0     |   ✓    |
| 0 | 0 | 1 |   1    |     1     |   ✓    |
| 0 | 1 | 0 |   0    |     0     |   ✓    |
| 0 | 1 | 1 |   1    |     1     |   ✓    |
| 1 | 0 | 0 |   0    |     0     |   ✓    |
| 1 | 0 | 1 |   0    |     0     |   ✓    |
| 1 | 1 | 0 |   0    |     1     |   ✗    |
| 1 | 1 | 1 |   0    |     1     |   ✗    |

**Result:** Removing `(A ∧ B)` changes the output in rows 7 and 8. Therefore, `(A ∧ B)` is **NOT redundant**.

**Testing if `(¬A ∧ C)` is redundant:**
If we remove `(¬A ∧ C)`, we'd have: \(X = (A \land B)\)

Let's check the truth table for this simplified expression:

| A | B | C | A ∧ B | Original X | Match? |
|---|---|---|-------|-----------|---------|
| 0 | 0 | 0 |   0   |     0     |   ✓    |
| 0 | 0 | 1 |   0   |     1     |   ✗    |
| 0 | 1 | 0 |   0   |     0     |   ✓    |
| 0 | 1 | 1 |   0   |     1     |   ✗    |
| 1 | 0 | 0 |   0   |     0     |   ✓    |
| 1 | 0 | 1 |   0   |     0     |   ✓    |
| 1 | 1 | 0 |   1   |     1     |   ✓    |
| 1 | 1 | 1 |   1   |     1     |   ✓    |

**Result:** Removing `(¬A ∧ C)` changes the output in rows 2 and 4. Therefore, `(¬A ∧ C)` is **NOT redundant**.

**Conclusion:**
Neither term is redundant. Both `(A ∧ B)` and `(¬A ∧ C)` are necessary because:
- `(A ∧ B)` is needed to make X=1 when A=1 and B=1 (rows 7 and 8)
- `(¬A ∧ C)` is needed to make X=1 when A=0 and C=1 (rows 2 and 4)

These two terms cover **mutually exclusive** conditions (one requires A=1, the other requires A=0), so both are essential to produce the correct output for all input combinations.
