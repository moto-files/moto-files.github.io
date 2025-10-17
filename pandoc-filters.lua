-- Adds anchor links to headings with IDs.
-- See: https://github.com/jgm/pandoc-website/blob/master/tools/anchor-links.lua
-- This will help disable visited links on headings and a proper anchors to it.
function Header(header)
	if header.identifier ~= '' then
		-- Set header as link.
		local anchor_link = pandoc.Link(
			header.content,                                           -- content
			'#' .. header.identifier,                                 -- href
			pandoc.utils.stringify(header.content),                   -- title
			{ class = 'anchor-link' }                                 -- attributes
		)
		header.content = { anchor_link }
		return pandoc.Div(
			{ header }, -- Keep the header block as-is.
			{ class = "pandoc-header" }
		)
	end
end

-- For wrapping inline code with a custom <span> tag.
-- This will help add border/background to inline code without ugly CSS hacks.
function Code(code)
	-- Let Pandoc render the code as usual, then wrap it in a <span> tag.
	return pandoc.Span(
		{ code }, -- Keep the code as-is.
		{ class = "pandoc-code-inline" }
	)
end

-- For wrapping code blocks with a custom <div> tag.
-- This will help add border/background to block code without ugly CSS hacks.
function CodeBlock(code)
	-- Let Pandoc render the block as usual, then wrap it in a <div> tag.
	return pandoc.Div(
		{ code }, -- Keep the code block as-is.
		{ class = "pandoc-code-block" }
	)
end
