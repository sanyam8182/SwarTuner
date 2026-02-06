/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./App.{js,jsx,ts,tsx}", "./src/**/*.{js,jsx,ts,tsx}"],
    theme: {
        extend: {
            colors: {
                background: "#080808",
                surface: "rgba(255, 255, 255, 0.05)",
                // Add other custom colors here as needed
            },
            borderRadius: {
                '3xl': '32px',
                '2xl': '16px',
            },
            fontFamily: {
                // Add font families here when they are linked
            },
        },
    },
    plugins: [],
}
