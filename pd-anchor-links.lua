-- Adds anchor links to headings with IDs.
-- See: https://github.com/jgm/pandoc-website/blob/master/tools/anchor-links.lua
function Header(h)
	if h.identifier ~= '' then
		-- an empty link to this header
		local anchor_link = pandoc.Link(
			h.content,                                           -- content
			'#' .. h.identifier,                                 -- href
			pandoc.utils.stringify(h.content),                   -- title
			{ class = 'class-anchor', ['aria-hidden'] = 'true' } -- attributes
		)
		h.content = { anchor_link }
		return h
	end
end
