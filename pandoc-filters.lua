-- Adds anchor links to headings with IDs.
-- See: https://github.com/jgm/pandoc-website/blob/master/tools/anchor-links.lua
function Header(header)
	if header.identifier ~= '' then
		-- Set header as link.
		local anchor_link = pandoc.Link(
			header.content,                                           -- content
			'#' .. header.identifier,                                 -- href
			pandoc.utils.stringify(header.content),                   -- title
			{ class = 'anchor-link', ['aria-hidden'] = 'true' }       -- attributes
		)
		header.content = { anchor_link }
		return header
	end
end

-- For wrapping inline code with a custom <span> tag.
function Code(code)
	-- Let Pandoc render the code as usual, then wrap it in a <span> tag.
	return pandoc.Span(
		{ code }, -- Keep the code as-is.
		{class = "pandoc-code-inline"}
	)
end

-- For wrapping code blocks with a custom <div> tag.
function CodeBlock(code)
	-- Let Pandoc render the block as usual, then wrap it in a <div> tag.
	return pandoc.Div(
		{ code }, -- Keep the code block as-is.
		{class = "pandoc-code"}
	)
end
