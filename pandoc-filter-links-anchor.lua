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
