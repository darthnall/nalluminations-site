/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
        "./**/templates/shop/*.html",
        "./**/templates/shop/**/*.html",
        "./**/templates/blog/*.html",
        "./**/templates/blog/**/*.html",
    ],
  theme: {
    extend: {
            "nalluminations-pink": "#ffdddd",
            "nalluminations-yellow": "#ffffb9",
            "nalluminations-blue": "#bae1ff",
        },
  },
  plugins: [],
}
