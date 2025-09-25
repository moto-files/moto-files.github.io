# Markdown Cheat Sheet

Page generation is powered by **[Pandoc](https://pandoc.org/)**, and **[GitHub Flavored Markdown](https://github.github.com/gfm/)** is used for markup.

This document describes a basic writing and formatting GFM syntax.

---

## Headings

To create a heading, add one to four `#` symbols before your heading text. 
The number of `#` you use will determine the hierarchy level and typeface size of the heading.

**Code:**

```md
# A first-level heading
## A second-level heading
### A third-level heading
#### A fourth-level heading
asd
asd
asd
asd
```

**Result:**

# A first-level heading
## A second-level heading
### A third-level heading
#### A fourth-level heading

---

`#0969DA`

1. First list item
   - First nested list item
     - Second nested list item


- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

<details>
  <summary>Spoiler warning</summary>
  
  Spoiler text. Note that it's important to have a space after the summary tag. You should be able to write any markdown you want inside the `<details>` tag... just make sure you close `<details>` afterward.
  
  ```javascript
  console.log("I'm a code block!");
  ```
  
</details>
