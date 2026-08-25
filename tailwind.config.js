/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./js/**/*.js"],
  theme: {
    container: {
      center: true,
      padding: { DEFAULT: '1.25rem', sm: '2rem', lg: '3rem', xl: '4rem' },
    },
    extend: {
      colors: {
        navy: {
          50:  '#eef2fb',
          100: '#dbe4f6',
          200: '#b0c3ea',
          300: '#84a1dd',
          400: '#4f74c4',
          500: '#2b4fa3',
          600: '#1c3a86',
          700: '#132b6b',
          800: '#0d2054',
          900: '#0a1a44',
          950: '#060f2b',
        },
        brick: {
          50:  '#fdecec',
          100: '#fad2d1',
          200: '#f3a3a1',
          300: '#e9726f',
          400: '#e14a46',
          500: '#d9201d',
          600: '#c11916',
          700: '#9c1512',
          800: '#7a1210',
          900: '#5c0e0c',
        },
        ink: {
          50:  '#f5f6f8',
          100: '#e7e9ee',
          400: '#6b7280',
          500: '#4b5468',
          600: '#333c52',
          700: '#232a3d',
          800: '#161c2c',
          900: '#0b0f1a',
        },
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        sans: ['"Inter"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        'display-xl': ['clamp(2.75rem, 5vw + 1rem, 5rem)', { lineHeight: '1.02', letterSpacing: '-0.02em' }],
        'display-lg': ['clamp(2.25rem, 3.5vw + 1rem, 3.5rem)', { lineHeight: '1.05', letterSpacing: '-0.02em' }],
        'display-md': ['clamp(1.75rem, 2vw + 1rem, 2.5rem)', { lineHeight: '1.1', letterSpacing: '-0.01em' }],
      },
      boxShadow: {
        soft: '0 2px 8px -2px rgba(10,26,68,0.08), 0 12px 32px -12px rgba(10,26,68,0.12)',
        card: '0 1px 2px rgba(10,26,68,0.06), 0 8px 24px -8px rgba(10,26,68,0.10)',
        'card-hover': '0 8px 16px -4px rgba(10,26,68,0.12), 0 24px 48px -16px rgba(10,26,68,0.20)',
        glow: '0 0 0 1px rgba(255,255,255,0.06), 0 20px 60px -10px rgba(11,39,96,0.55)',
      },
      backgroundImage: {
        'grid-fade': 'linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 100%)',
      },
      animation: {
        'float-slow': 'float 7s ease-in-out infinite',
        'float-slower': 'float 10s ease-in-out infinite',
        'pulse-soft': 'pulseSoft 3.5s ease-in-out infinite',
        'marquee': 'marquee 38s linear infinite',
        'marquee-reverse': 'marqueeReverse 42s linear infinite',
        'spin-slow': 'spin 18s linear infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-14px)' },
        },
        pulseSoft: {
          '0%, 100%': { opacity: 0.55, transform: 'scale(1)' },
          '50%': { opacity: 1, transform: 'scale(1.06)' },
        },
        marquee: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        marqueeReverse: {
          '0%': { transform: 'translateX(-50%)' },
          '100%': { transform: 'translateX(0)' },
        },
      },
    },
  },
  plugins: [],
}
