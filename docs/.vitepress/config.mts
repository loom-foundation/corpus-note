import { withMermaid } from 'vitepress-plugin-mermaid'

// Two recorded accommodations (bake-off report):
// 1. markdown-it-attrs disabled, so brace text in prose stays literal.
// 2. Mermaid via vitepress-plugin-mermaid (withMermaid wraps the config).
// Dead links fail the build on purpose: the docs are self-contained and
// never link outside their own tree.
export default withMermaid({
  title: 'Note',
  markdown: { attrs: { disable: true } },
  themeConfig: {
    search: { provider: 'local' },
    sidebar: [{ text: 'Note', link: '/' }],
  },
})
