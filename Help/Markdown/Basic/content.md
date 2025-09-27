# Markdown Cheat Sheet

The pages on this site are written in [GitHub Flavored Markdown](//github.github.com/gfm/) (GFM) and converted to HTML using [Pandoc](//pandoc.org/) utility. This page provides a guide to the basic GFM syntax. Further details are available in GitHub's official [Basic Writing and Formatting Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) document. Hard-breaks are enabled for this configuration, each line break in Markdown will be rendered in the HTML page.



---

## 1. Bold, Italic, Strikethrough, Underline, Superscript, Subscript

You can indicate emphasis with bold, italic, strikethrough, subscript, or superscript text in documents.

**Code:**

```md
**This is bold text**
_This text is italicized_
~~This was mistaken text~~
**This text is _extremely_ important**
***All this text is important***
This is a <sup>superscript</sup> text
This is a <sub>subscript</sub> text
This is an <ins>underlined</ins> text
```

**Result:**

**This is bold text**
_This text is italicized_
~~This was mistaken text~~
**This text is _extremely_ important**
***All this text is important***
This is a <sup>superscript</sup> text
This is a <sub>subscript</sub> text
This is an <ins>underlined</ins> text

---

## 2. Inline code and Code blocks

You can call out code or a command within a sentence with single backticks. The text within the backticks will not be formatted. To format code or text into its own distinct block, use triple backticks. In addition, you can set the code language for proper highlighting next to triple backticks.

**Code:**

```md
Use `git status` to list all new or modified files that haven't yet been committed.

​```
git status
git add
git commit
​```

​```python
if __name__ == '__main__':
	sys.exit(main())

​```
```

**Result:**

Use `git status` to list all new or modified files that haven't yet been committed.

```
git status
git add
git commit
```

```python
if __name__ == '__main__':
	sys.exit(main())

```

---

## 3. Quoting

You can quote text with a `>` character, nested quotes are also supported.

**Code:**

```
> Text that is a quote
> Text that is a quote
>
> Text that is a quote
>
>> Text that is a quote
>> Text that is a quote
>> Text that is a quote
>>> Text that is a quote
>>> Text that is a quote
>
> Text that is a quote
```

**Result:**

> Text that is a quote
> Text that is a quote
>
> Text that is a quote
>
>> Text that is a quote
>> Text that is a quote
>> Text that is a quote
>>> Text that is a quote
>>> Text that is a quote
>
> Text that is a quote

---

## 1. Horizontal Line

A simple horizontal line is convenient for separating sections of information.

**Code:**

```md
---
```

**Result:**

---

## 2. Headings

To create a heading, add one to four `#` symbols before your heading text. The number of `#` you use will determine the hierarchy level and typeface size of the heading.

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
