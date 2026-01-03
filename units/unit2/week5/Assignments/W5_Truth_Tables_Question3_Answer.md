# Section 2: Karnaugh Maps and Algebraic Simplification

## Question 3 [9 points]

A vending machine releases a product only if the user inserts the correct amount and selects an available item. The inputs are:
- A = 1 if the correct amount is inserted
- B = 1 if an item is selected
- C = 1 if the item is available

The output X should be 1 only if the vending machine should dispense the item.

### Part A: Truth Table

**Understanding the logic:**
The vending machine should dispense (X = 1) only when ALL three conditions are met:
- Correct amount is inserted (A = 1) AND
- Item is selected (B = 1) AND
- Item is available (C = 1)

**Truth Table:**

| A | B | C | X (Dispense) |
|---|---|---|--------------|
| 0 | 0 | 0 |      0       |
| 0 | 0 | 1 |      0       |
| 0 | 1 | 0 |      0       |
| 0 | 1 | 1 |      0       |
| 1 | 0 | 0 |      0       |
| 1 | 0 | 1 |      0       |
| 1 | 1 | 0 |      0       |
| 1 | 1 | 1 |      1       |

**Explanation:**
- X = 1 only in row 8, where A=1, B=1, and C=1 (all conditions are satisfied)
- In all other cases, at least one condition is missing, so X = 0

### Part B: Boolean Expression

**Deriving the Boolean expression from the problem statement:**

The output X should be 1 when:
- A = 1 AND B = 1 AND C = 1

**Boolean Expression:**

\[X = A \land B \land C\]

**Alternative notations:**
- Algebraic form: \(X = ABC\)
- Using multiplication: \(X = A \cdot B \cdot C\)

**In words:** The vending machine dispenses the item only when the correct amount is inserted AND an item is selected AND the item is available.

### Part C: Simplification using Boolean Algebra

**Original expression:** \(X = A \land B \land C\)

**Simplification steps:**

1. The expression \(A \land B \land C\) is already in its simplest form.
2. This is a product of all three variables with no redundant terms.
3. All three conditions are necessary and cannot be removed.

**Simplified expression:**

\[X = A \land B \land C\]

**Explanation:**
- This expression cannot be simplified further because:
  - All three variables (A, B, C) are required
  - There are no redundant terms
  - The expression is already in minimal form (a single AND operation of all inputs)
- Any attempt to remove a variable would change the logic:
  - Removing A: Would allow dispensing without correct amount (incorrect)
  - Removing B: Would allow dispensing without item selection (incorrect)
  - Removing C: Would allow dispensing unavailable items (incorrect)

**Conclusion:** The expression is already in its simplest form and cannot be simplified.

### Part D: Verification using Truth Table

**Verification Table:**

| A | B | C | A ∧ B ∧ C | X (from Part A) | Match? |
|---|---|---|------------|------------------|--------|
| 0 | 0 | 0 |     0     |        0         |   ✓    |
| 0 | 0 | 1 |     0     |        0         |   ✓    |
| 0 | 1 | 0 |     0     |        0         |   ✓    |
| 0 | 1 | 1 |     0     |        0         |   ✓    |
| 1 | 0 | 0 |     0     |        0         |   ✓    |
| 1 | 0 | 1 |     0     |        0         |   ✓    |
| 1 | 1 | 0 |     0     |        0         |   ✓    |
| 1 | 1 | 1 |     1     |        1         |   ✓    |

**Verification Result:**
✅ **The simplified expression produces the same output as the original in all 8 rows.**

The Boolean expression \(X = A \land B \land C\) correctly represents the vending machine logic:
- X = 1 only when all three inputs are 1 (row 8)
- X = 0 in all other cases (rows 1-7)

**Summary:**
- The truth table shows X = 1 in exactly one case (A=1, B=1, C=1)
- The Boolean expression \(X = A \land B \land C\) matches this behavior perfectly
- The expression is already in simplest form and cannot be simplified further
- Verification confirms that the expression produces the correct output for all input combinations
