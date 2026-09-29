---
name: Vibrant Momentum
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#5c3f42'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#906f72'
  outline-variant: '#e5bdc0'
  surface-tint: '#bd0042'
  primary: '#b90040'
  on-primary: '#ffffff'
  primary-container: '#e31754'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2ba'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fd8b00'
  on-secondary-container: '#603100'
  tertiary: '#4648d4'
  on-tertiary: '#ffffff'
  tertiary-container: '#6063ee'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dc'
  primary-fixed-dim: '#ffb2ba'
  on-primary-fixed: '#400011'
  on-primary-fixed-variant: '#910030'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#e1e0ff'
  tertiary-fixed-dim: '#c0c1ff'
  on-tertiary-fixed: '#07006c'
  on-tertiary-fixed-variant: '#2f2ebe'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  subheadline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-base:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-bold:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 32px
  margin-mobile: 20px
  stack-lg: 80px
  stack-md: 48px
  stack-sm: 24px
---

## Brand & Style
The design system embodies a high-end "Expert Agency" aesthetic, merging corporate reliability with creative energy. It targets a professional audience that values precision and results but expects a modern, forward-thinking interface. 

The style is **Corporate Modern with High-Contrast Accents**. It utilizes expansive white space and a "Swiss-style" clarity in typography, punctuated by high-impact, kinetic color gradients. The goal is to evoke a sense of momentum—movement and growth—while remaining grounded in a stable, trustworthy infrastructure.

## Colors
The palette is built on a foundation of "Gallery White" (#FFFFFF) to maximize perceived space and cleanliness. 

- **Primary & Secondary:** A vibrant transition from Deep Pink to Bright Orange creates the "Momentum Gradient," used exclusively for calls to action and key brand moments.
- **Accents:** Use the Primary Pink for strategic text highlighting (keywords in paragraphs) to guide the eye and inject personality into dense information.
- **Neutrals:** Deep Slate (#0F172A) is used for primary text to ensure high readability and a professional weight, while Light Slate (#F8FAFC) provides subtle background differentiation for secondary sections.

## Typography
Plus Jakarta Sans is the sole typeface, utilized through weight contrast to establish hierarchy.

- **Headlines:** Use ExtraBold (800) or Bold (700) for primary headers. Keep letter-spacing tight (-0.02em) to create a compact, impactful look.
- **Sub-headlines:** Contrast heavy headers with Light (300) or Regular (400) weights at larger sizes. This creates an elegant, editorial feel.
- **Emphasis:** Use the primary brand pink for specific keywords within body copy to draw attention to value propositions.
- **Labels:** Small caps with increased tracking (0.05em) should be used for overlines and category labels to maintain an organized, systematic appearance.

## Layout & Spacing
This design system utilizes a **12-column fixed grid** for desktop, centering the content at 1280px. 

- **Whitespace:** Emphasize generous vertical spacing (`stack-lg`) between major sections to allow the brand to "breathe" and feel premium.
- **Grid:** Use wide 32px gutters to prevent content density. 
- **Mobile:** Transition to a 4-column fluid grid with 20px side margins. Horizontal scrolling "peek" layouts are preferred for cards on mobile to reduce page height.

## Elevation & Depth
The depth model is minimalist and light-handed. 

- **Surface Tiers:** Use the #F8FAFC off-white for full-width section backgrounds to separate content blocks without using hard lines.
- **Shadows:** Cards use a single, highly-diffused "Ambient Shadow" (0px 12px 32px rgba(15, 23, 42, 0.04)). This provides a soft lift that suggests physical presence without creating clutter.
- **Interactions:** On hover, elevation should increase slightly by deepening the shadow opacity to 0.08 and shifting the element -4px on the Y-axis.

## Shapes
A "Rounded" (0.5rem) aesthetic is applied to strike a balance between friendly approachability and professional structure. 

- **Standard Elements:** Inputs and small cards use 0.5rem (8px) corner radius.
- **Large Components:** Feature blocks and hero containers use 1rem (16px) to emphasize their importance.
- **Buttons:** Use 0.5rem (8px) for a modern, architectural look—avoid full pills for primary actions to maintain the "Expert Agency" tone.

## Components
- **Buttons:** Primary buttons must use the Momentum Gradient with white text. Apply a subtle inner-glow on the top edge for a tactile feel. Secondary buttons should use a 1.5px border in Slate with no fill.
- **Cards:** Minimalist containers with #FFFFFF fill and the defined ambient shadow. No borders. Content inside cards should have 32px of internal padding.
- **Inputs:** Use the off-white surface (#F8FAFC) for the fill and a 1px Slate-200 border. On focus, the border transitions to the Primary Pink.
- **Agency Footer:** A "Fat Footer" layout. Organise into 4-5 columns: Company, Services, Expertise, Insights, and a Newsletter Signup. The background should be the dark Neutral Slate (#0F172A) with white or light-grey text to provide a grounded "anchor" to the light-themed pages.
- **Chips:** Small, low-contrast grey backgrounds with bold label-style text, used for categories or tags.