/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*/*/**/*.{html,js}"],
  theme: {
    extend: {},
    screens: {
      hz: { max: "893px" },
      // => @media (min-width: 576px) { ... }

      tab: { max: "750px" },
      // => @media (min-width: 960px) { ... }

      ph: { max: "618px" },
      // => @media (min-width: 1440px) { ... }
    },
  },
  plugins: [],
};
