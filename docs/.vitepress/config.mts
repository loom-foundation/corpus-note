import { withMermaid } from 'vitepress-plugin-mermaid'

// Two recorded accommodations (bake-off report):
// 1. markdown-it-attrs disabled, so brace text in prose stays literal.
// 2. Mermaid via vitepress-plugin-mermaid (withMermaid wraps the config).
// Dead links fail the build on purpose: the docs are self-contained and
// never link outside their own tree.
// docs/examples/ is excluded from the site: example files are data
// exercised by automated tests, not pages.
export default withMermaid({
  title: 'Note',
  markdown: { attrs: { disable: true } },
  srcExclude: ['examples/**'],
  themeConfig: {
    search: { provider: 'local' },
    sidebar: [
      {
        text: 'Tutorials',
        items: [
          { text: 'Your first note', link: '/tutorials/your-first-note' },
        ],
      },
      {
        text: 'Reference',
        items: [
          { text: 'The note file', link: '/reference/the-note-file' },
          { text: 'Identifiers', link: '/reference/identifiers' },
        ],
      },
      {
        text: 'Explanation',
        items: [
          { text: 'Why opaque ids', link: '/explanation/why-opaque-ids' },
        ],
      },
    ],
  },
})
