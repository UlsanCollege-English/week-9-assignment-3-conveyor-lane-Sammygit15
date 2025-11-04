[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/No7yWBeY)
# HW03 — Conveyor Lane: Nearly-Sorted Packages

**Story intro (new theme):**  
A **conveyor lane** outputs packages **almost in order**. Each package is at most **k positions away** from its correct place. Sort them efficiently.

**Technical description**  
- **Input:** list `arr` of integers; integer `k >= 0`.  
- **Output:** new list: `arr` sorted ascending.  
- **Guarantee:** Each element is at most `k` positions from its final sorted index.  
- **Expected complexity:** **Time** `O(n log k)` with a min-heap of size `k+1`; **Space** `O(k)`.

---

## 8 Steps scaffold
**Steps 1–3 (brief prompts)**  

1. **Read & Understand:** We need to sort a k-near-sorted list.  
2. **Re-phrase:** Keep a small window heap; output the smallest each step.  
3. **Identify:** inputs `arr, k`; output sorted list; vars: `heap`, `out`.

**You handle Steps 4–8**


4. Break down algorithm steps.  
5. Write pseudocode.  
6. Code with `heapq`.  
7. Debug small lists.  
8. Explain why it is `O(n log k)`.

---

## Hints
- Push first `k+1` items; then push one, pop one for the rest.  
- If `k >= len(arr)`, heapify whole array.  
- For empty `arr`, return `[]`.

---

## How to run tests
python -m pytest -q


---

## FAQ
- **Q:** Does this always equal `sorted(arr)`? **A:** Yes, if implemented right.  
- **Q:** What if `k <= 0`? **A:** Return a copy of `arr` sorted (or the same if already sorted).  
- **Q:** Complexity? **A:** `O(n log k)` time, `O(k)` space.  
- **Q:** stdin? **A:** No. Provide a function the tests call.  
- **Q:** Duplicates? **A:** Yes, keep stable order not required.  
- **Q:** Reading failures? **A:** Compare the output to `sorted(arr)`.  
- **Q:** Grading? **A:** We run tests on your function.
