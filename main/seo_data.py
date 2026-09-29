"""SEO copy for the digital marketing pages: target keywords, FAQs and schema names.

Each page renders these through main/templates/main/dm/_seo_block.html, which also emits
FAQPage, Service and BreadcrumbList JSON-LD. Edit here to tune keywords or answers.
"""

DM_PAGES = {
    "hub": {
        "name": "Digital Marketing",
        "url_name": "digital_marketing",
        "keywords": [
            "digital marketing agency in Nepal", "digital marketing company Kathmandu",
            "best digital marketing agency Nepal", "social media marketing Nepal", "Meta ads Nepal",
            "TikTok marketing Nepal", "SEO services Kathmandu", "content marketing Nepal",
            "online marketing Nepal", "digital marketing services Lalitpur",
        ],
        "faqs": [
            ("What does a digital marketing agency in Nepal do?", "We plan and run the channels that bring customers online: social media marketing, Meta (Facebook and Instagram) ads, TikTok, content and reels, SEO and community management, so your marketing produces measurable enquiries and sales."),
            ("Which digital marketing services does Trend Crafters offer?", "Social media marketing (our most requested service), Meta ads, TikTok marketing, content and reels strategy, SEO and search, and community management, all delivered by one team from our Lalitpur studio."),
            ("How much does digital marketing cost in Nepal?", "It depends on your goals, channels and ad budget. We share a written scope and fee before we start, and ad spend is always separate and transparent."),
            ("Do you work with businesses outside Kathmandu?", "Yes. We serve brands across Nepal and internationally, including clients on Australia's Gold Coast, and work in both English and Nepali."),
            ("How soon will I see results?", "Paid campaigns can produce leads within days. Social media growth and SEO compound over months. We agree on milestones and report monthly so you always know where you stand."),
        ],
    },
    "social": {
        "name": "Social Media Marketing",
        "url_name": "dm_social_media",
        "keywords": [
            "social media marketing agency Nepal", "social media management Kathmandu",
            "Facebook marketing Nepal", "Instagram marketing Nepal", "LinkedIn marketing Nepal",
            "social media content creation Nepal", "social media agency Lalitpur",
            "social media strategy for business", "social media advertising Nepal",
            "brand growth on social media",
        ],
        "faqs": [
            ("What is included in social media marketing?", "Strategy and positioning, a content calendar, design and video, posting and scheduling, paid boosts on winning posts, community replies and a monthly report."),
            ("Which platforms should my business be on in Nepal?", "Facebook and Instagram reach the widest local audience, TikTok is strongest for discovery, and LinkedIn suits B2B and hiring. We recommend the mix that fits your customers, not every platform."),
            ("Do you create the photos and videos too?", "Yes. Our in-house production team shoots photos and 9:16 reels, so content, ads and community all come from one team."),
            ("How often will you post?", "We agree a posting rhythm in your content calendar, typically several posts and stories a week, adjusted to your goals and results."),
            ("Can you manage my social media end to end?", "Yes, from strategy and content to posting, ads, community management and reporting."),
        ],
    },
    "meta": {
        "name": "Meta Ads (Facebook & Instagram)",
        "url_name": "dm_meta_ads",
        "keywords": [
            "Facebook ads agency Nepal", "Instagram ads Nepal", "Meta ads management Kathmandu",
            "Facebook advertising Nepal", "lead generation Facebook ads Nepal",
            "click to WhatsApp ads Nepal", "retargeting ads Nepal", "boost reels Nepal",
            "Meta ads for education consultancy", "Facebook ads for restaurants Nepal",
        ],
        "faqs": [
            ("How much should I spend on Facebook and Instagram ads in Nepal?", "Start with a budget you can sustain for at least four weeks so we can test audiences and creatives. We recommend a figure after learning your goal, margin and audience size."),
            ("What is the difference between boosting a post and running Meta ads?", "Boosting promotes one post to a broad audience. Meta ad campaigns use segmented audiences, tested creatives, tracking and retargeting, so you pay for leads and sales, not just likes."),
            ("Can you run click to WhatsApp ads?", "Yes. Click to WhatsApp ads open a chat with your team and work very well in Nepal, where customers prefer to message before they buy."),
            ("What results will you report?", "Reach, click through rate, cost per lead or sale, return on ad spend and audience insights, in a plain language monthly report."),
            ("Do you run ads for international clients?", "Yes. We have run cross border campaigns, including for clients on Australia's Gold Coast, and study abroad campaigns for education partners."),
        ],
    },
    "tiktok": {
        "name": "TikTok Marketing",
        "url_name": "dm_tiktok",
        "keywords": [
            "TikTok marketing agency Nepal", "TikTok ads Nepal", "TikTok content creation Kathmandu",
            "TikTok influencer marketing Nepal", "viral video marketing Nepal",
            "short form video marketing Nepal", "TikTok for business Nepal", "Spark Ads Nepal",
            "TikTok creators Nepal", "TikTok brand growth",
        ],
        "faqs": [
            ("Is TikTok good for business in Nepal?", "Yes. TikTok reaches people who do not follow you yet, which makes it strong for brand discovery, especially for retail, food, education and lifestyle brands."),
            ("Do you work with TikTok creators?", "Yes. We source and brief Nepali creators, write scripts in your brand voice and handle usage rights and reporting."),
            ("What are Spark Ads?", "Spark Ads boost your best organic TikTok videos as ads, keeping likes and comments and usually performing better than cold ads."),
            ("How long should a TikTok video be?", "We build most videos at around 15 seconds with a hook in the first three seconds, then test longer formats when the topic needs it."),
            ("Can TikTok drive sales, not just views?", "Yes. With conversion tracking and clear calls to action, TikTok content can drive website visits, WhatsApp chats and purchases."),
        ],
    },
    "content": {
        "name": "Content & Reels Strategy",
        "url_name": "dm_content_reels",
        "keywords": [
            "reels production Nepal", "content marketing agency Nepal", "content strategy Kathmandu",
            "video content for social media Nepal", "Instagram reels agency Nepal",
            "short video production Kathmandu", "content calendar for business",
            "brand storytelling Nepal", "social media video editing Nepal", "carousel post design Nepal",
        ],
        "faqs": [
            ("How many reels do I need each month?", "Most brands start with four to eight reels a month plus carousels and statics. We tune the mix to what your audience responds to."),
            ("Do you handle scripting, shooting and editing?", "Yes. We plan ideas, write scripts, shoot with cinematic lighting, edit for mobile with captions and sound, then publish and report."),
            ("Are reels better than static posts?", "Reels usually earn more reach, while carousels and statics earn saves and drive offers. A balanced mix works best."),
            ("Can you use our own footage?", "Yes. We can edit footage you already have, or shoot new content in our studio or on location."),
            ("Do you make content in Nepali?", "Yes. We produce content in English, Nepali or both, with captions."),
        ],
    },
    "seo": {
        "name": "SEO & Search",
        "url_name": "dm_seo",
        "keywords": [
            "SEO services Kathmandu", "SEO company Nepal", "local SEO Nepal",
            "Google Business Profile optimization Nepal", "website ranking Nepal",
            "keyword research Nepal", "technical SEO audit", "on page SEO Nepal",
            "SEO agency Lalitpur", "rank on Google Nepal",
        ],
        "faqs": [
            ("How long does SEO take to work in Nepal?", "Technical fixes can help within weeks, but meaningful ranking growth usually takes three to six months depending on competition and your starting point."),
            ("What is local SEO?", "Local SEO helps you appear in map results and 'near me' searches through your Google Business Profile, consistent listings, reviews and location pages."),
            ("Do you do keyword research in Nepali and English?", "Yes. We research how customers actually search, in English, Nepali and mixed queries."),
            ("Will you audit my website first?", "Yes. Every SEO engagement starts with an audit covering speed, mobile experience, indexing, content and links, followed by a prioritised fix list."),
            ("Can you guarantee first page rankings?", "No honest agency can. We commit to a clear plan, transparent work and monthly reporting on rankings, traffic and enquiries."),
        ],
    },
    "community": {
        "name": "Community Management",
        "url_name": "dm_community",
        "keywords": [
            "community management Nepal", "social media moderation Nepal",
            "customer engagement social media Nepal", "reputation management Nepal",
            "inbox and comment management", "brand community building",
            "social media customer service Nepal", "review response management",
            "social listening Nepal", "audience engagement strategy",
        ],
        "faqs": [
            ("What does a community manager do?", "They reply to comments and messages, moderate spam and abuse, start conversations, handle complaints and report what your audience is saying."),
            ("Can you reply in Nepali and English?", "Yes, in your brand voice, with a tone guide so every reply sounds like you."),
            ("How fast do you respond?", "We agree response windows with you and escalate sales enquiries and urgent issues straight away."),
            ("Do you handle negative comments and reviews?", "Yes. We respond calmly and publicly, then move the conversation to private messages to resolve it."),
            ("Does community management help sales?", "Yes. Fast, helpful replies turn questions into orders and bookings, and loyal followers become repeat customers and advocates."),
        ],
    },
}


BR_PAGES = {
    "hub": {
        "name": "Branding & Campaigns",
        "url_name": "brand_campaign",
        "keywords": [
            "branding agency in Nepal", "brand identity design Kathmandu", "creative agency Nepal",
            "brand campaign agency Nepal", "graphic design Nepal", "brand storytelling Nepal",
            "logo design Kathmandu", "rebranding agency Nepal", "brand strategy Nepal",
            "advertising agency Lalitpur",
        ],
        "faqs": [
            ("What does a branding agency in Nepal do?", "We build the identity, campaigns, design and story that make a business recognisable and trusted: logo and visual identity, brand guidelines, campaign concepts, graphic design and brand storytelling."),
            ("What is the difference between a logo and a brand identity?", "A logo is a signature. An identity is how your business looks, sounds and feels everywhere: colours, typography, imagery, tone of voice and how they are applied on every touchpoint."),
            ("Can you rebrand an existing business?", "Yes. We audit what you have, keep the equity worth keeping, and refresh the rest so your brand feels current and premium."),
            ("How long does a brand identity project take?", "Most identity projects take four to eight weeks, from discovery and concepts to final files and guidelines. Campaigns are scoped separately."),
            ("Do you handle both local and international audiences?", "Yes. We bridge local market dynamics and global design standards, so brands work in Nepal and abroad."),
        ],
    },
    "identity": {
        "name": "Brand Identity",
        "url_name": "br_identity",
        "keywords": [
            "brand identity design Nepal", "logo design Kathmandu", "visual identity Nepal",
            "brand guidelines Nepal", "brand strategy Kathmandu", "rebranding Nepal",
            "brand colour and typography", "company logo design Nepal", "packaging and stationery design Nepal",
            "brand positioning Nepal",
        ],
        "faqs": [
            ("What do I receive in a brand identity package?", "A logo suite, colour palette, typography, imagery direction, tone of voice, stationery and social templates, plus brand guidelines so your team applies everything consistently."),
            ("Do you design logos only?", "We rarely sell a logo alone. A logo works best inside a full identity, but we can start with a focused logo project if that is what you need."),
            ("What is material realism?", "Our design philosophy: visuals that feel tactile and premium, using the weight of real textures such as polished metal, rich wood grain and raw materials, instead of flat or overly CGI looks."),
            ("Will I own the final files?", "Yes. You receive final source and export files, along with usage guidelines."),
            ("Can you refresh our existing brand?", "Yes. We review what is working and modernise the rest, so your audience still recognises you."),
        ],
    },
    "campaigns": {
        "name": "Brand Campaigns",
        "url_name": "br_campaigns",
        "keywords": [
            "brand campaign agency Nepal", "advertising campaign Kathmandu", "product launch campaign Nepal",
            "creative campaign concept Nepal", "campaign video production Nepal",
            "integrated marketing campaign Nepal", "brand film Nepal", "storyboard and ad concept",
            "multi platform campaign Nepal", "commercial ad campaign Kathmandu",
        ],
        "faqs": [
            ("What is a brand campaign?", "A coordinated idea, told across video, photography, social, print and ads, designed to change how people see and choose your brand."),
            ("What does an end to end campaign include?", "Concept and storyboard, production (photo and video), design, copy, multi platform distribution, paid amplification and measurement."),
            ("Can you run a product launch campaign?", "Yes. We plan the visual concept, shoot the hero content and roll it out across channels around your launch date."),
            ("Do you produce the video and photography in house?", "Yes. Our production team shoots with cinematic lighting and precision studio techniques."),
            ("How do you measure campaign success?", "Against goals we agree at the start: reach, engagement, leads or sales, with a report at the end of every campaign phase."),
        ],
    },
    "graphic": {
        "name": "Graphic Design",
        "url_name": "br_graphic",
        "keywords": [
            "graphic design Nepal", "graphic design agency Kathmandu", "social media design Nepal",
            "packaging design Nepal", "brochure and print design Nepal", "poster and banner design Nepal",
            "website UI design Nepal", "creative design services Lalitpur", "marketing collateral design",
            "typography and layout design",
        ],
        "faqs": [
            ("What graphic design do you offer?", "Social media graphics, packaging, print collateral, brochures, posters, presentations and website UI elements, all in one consistent style."),
            ("Can you design from our brand guidelines?", "Yes. We follow your guidelines, or build them first if you do not have any."),
            ("Do you design social media templates?", "Yes. We create reusable templates so your team can post quickly and stay on brand."),
            ("How fast can you turn around a design?", "Small pieces usually take a few working days. Larger packages and print projects are scheduled with you upfront."),
            ("Do you prepare files for print?", "Yes. We deliver print ready files with correct colour, bleed and formats."),
        ],
    },
    "story": {
        "name": "Brand Storytelling",
        "url_name": "br_story",
        "keywords": [
            "brand storytelling Nepal", "copywriting Nepal", "brand voice and messaging",
            "content storytelling Kathmandu", "brand narrative", "persuasive copywriting Nepal",
            "brand messaging strategy", "company story video Nepal", "tone of voice Nepal",
            "storytelling agency Nepal",
        ],
        "faqs": [
            ("What is brand storytelling?", "Giving your business a distinct voice and a compelling reason for people to care, through a narrative that is told consistently in words and visuals."),
            ("Do you write the copy as well?", "Yes. We combine high end visual concepts with conversion focused, persuasive copywriting in English and Nepali."),
            ("Is storytelling only for consumer brands?", "No. B2B brands use stories too: case studies, founder narratives and clear explanations of innovative services."),
            ("How do you find our story?", "Through interviews, audience research and a review of your history, customers and strengths."),
            ("Where will the story be used?", "Across your website, social media, video, ads, pitch decks and print, so it feels like one brand everywhere."),
        ],
    },
}


PR_PAGES = {
    "hub": {"name": "Production Services", "url_name": "production",
        "keywords": ["production house Nepal", "video production Kathmandu", "photography agency Nepal", "commercial ad production Nepal", "reels production Nepal", "brand photography Nepal", "studio in Lalitpur", "cinematic video Nepal", "photo and video production Nepal", "content production agency Nepal"],
        "faqs": [
            ("What production services does Trend Crafters offer?", "Commercial photography, 9:16 video and reels, and full commercial ad production, all shot by our in house team in Lalitpur and on location."),
            ("Do you have your own studio and equipment?", "Yes. We shoot with professional cinema and mirrorless cameras, prime lenses and studio lighting, in our studio or at your location."),
            ("Who works on my project?", "A project manager, a marketing lead, an editor, a graphic designer and a social media manager, coordinated so nothing gets lost between shoot and publish."),
            ("How long does a shoot take to deliver?", "Photo sets are typically delivered within days, and edited video within one to two weeks, depending on scope. We agree the schedule up front."),
            ("Can you produce for both social media and TV?", "Yes. We produce vertical reels for social as well as larger commercials for broadcast and online."),
        ]},
    "photo": {"name": "Photography", "url_name": "photo_shoot",
        "keywords": ["commercial photography Nepal", "product photography Kathmandu", "photo shoot Lalitpur", "brand photography Nepal", "food photography Kathmandu", "fashion photoshoot Nepal", "studio photography Nepal", "corporate photography Nepal", "ecommerce product photos Nepal", "hospitality photography Nepal"],
        "faqs": [
            ("What is material realism in photography?", "Capturing the authentic, tactile weight of materials such as rich wood, polished metal and textures, using precision cinematic lighting instead of artificial or overly CGI looks."),
            ("Can you shoot products in a studio?", "Yes. We shoot hero product images on glass, metal and material sets, built for launches, catalogues and ecommerce."),
            ("Do you photograph restaurants and hotels?", "Yes. Cinematic lighting that captures ambience, texture and mood for cafes, hotels and retail brands."),
            ("How many edited photos will I get?", "It depends on the shoot. We agree a shot list and the number of final edited images before we start."),
            ("Do you provide styling and props?", "We plan the concept and styling with you, including sets and props that fit the mood of the brand."),
        ]},
    "video": {"name": "Video & Reels", "url_name": "pr_video",
        "keywords": ["video production Nepal", "reels production Kathmandu", "9:16 vertical video Nepal", "short form video agency Nepal", "TikTok video production Nepal", "video editing Kathmandu", "social media video Nepal", "brand video Nepal", "product video Nepal", "cinematic video Lalitpur"],
        "faqs": [
            ("What is 9:16 vertical video?", "The full screen portrait format used by Instagram Reels, TikTok and YouTube Shorts. We design hooks specifically for it."),
            ("Do you direct on screen talent?", "Yes. We direct talent for controlled, confident performances on camera."),
            ("What editing do you do?", "Trend aware cuts, colour grading, sound design, captions and motion graphics."),
            ("How many reels should I make each month?", "Most brands start with four to eight reels a month, mixed with static posts, and we adjust as results come in."),
            ("Can you shoot on location?", "Yes. We shoot in our studio or at your business, event or product site."),
        ]},
    "ads": {"name": "Commercial Ads", "url_name": "pr_ads",
        "keywords": ["commercial ad production Nepal", "TV commercial Nepal", "ad film production Kathmandu", "brand commercial video Nepal", "advertising video production Nepal", "product commercial Nepal", "corporate video Nepal", "digital ad video Nepal", "storyboard and ad production", "commercial production house Nepal"],
        "faqs": [
            ("What does commercial ad production include?", "Concept, script, storyboard, casting, shoot, edit, colour, sound and delivery in the formats you need for TV, online and social."),
            ("Can you scale from social ads to broadcast?", "Yes. We scale from localised digital campaigns in Nepal to larger international ads."),
            ("Do you handle casting and locations?", "Yes. We arrange talent, locations, props and crew as part of the production plan."),
            ("How do you make ads that sell?", "By blending cinematic storytelling with marketing psychology, so a commercial looks beautiful and drives action."),
            ("Can you produce cut downs for social media?", "Yes. We deliver the main film plus vertical and short cut downs for Reels, Stories and ads."),
        ]},
}

IT_PAGES = {
    "hub": {"name": "IT Solutions", "url_name": "it_solutions",
        "keywords": ["IT solutions Nepal", "web development company Nepal", "software company Kathmandu", "website and app development Nepal", "SEO and website maintenance Nepal", "frontend and backend developers Nepal", "MERN stack development Nepal", "digital solutions Lalitpur", "UI UX design Nepal", "IT company Lalitpur"],
        "faqs": [
            ("What IT solutions does Trend Crafters provide?", "Website design and development, custom web apps and dashboards, brand kits and UI design, plus ongoing maintenance, security and SEO optimisation."),
            ("Do you have frontend and backend developers?", "Yes. Our frontend developers build fast, responsive interfaces from Figma designs, and our backend developers build secure Node.js, MERN, Python and PHP systems and APIs behind them."),
            ("Can you handle SEO as well as development?", "Yes. SEO is built into every site we deliver, and we offer ongoing SEO optimisation and maintenance."),
            ("Have you built websites for real clients?", "Yes. For example, we built nexomigration.com, a multilingual migration and education site with consultation booking."),
            ("Do you also create the brand kit?", "Yes. We can design your logo, colours and typography and then build the website and assets around it."),
        ]},
    "web": {"name": "Web Development", "url_name": "web_development",
        "keywords": ["web development Nepal", "website design Kathmandu", "responsive website Nepal", "corporate website Nepal", "ecommerce website Nepal", "Figma to website", "mobile first website Nepal", "fast website Nepal", "Tailwind CSS developers", "SEO friendly website Nepal"],
        "faqs": [
            ("How long does a website take to build?", "A typical business site takes four to eight weeks from design approval to launch. Larger builds are scoped separately."),
            ("Do you use templates?", "No. We hand code responsive, mobile first sites so they are fast, secure and truly yours."),
            ("Will my site be SEO friendly?", "Yes. Clean structure, fast loading, schema, sitemaps and proper metadata come as standard."),
            ("Can you build an online shop?", "Yes. We build ecommerce platforms that handle traffic and drive measurable revenue."),
            ("Do you design in Figma first?", "Yes. You approve wireframes and a clickable prototype before we write code."),
        ]},
    "app": {"name": "Web App Development", "url_name": "web_app_development",
        "keywords": ["web app development Nepal", "custom software Kathmandu", "dashboard development Nepal", "SaaS development Nepal", "CRM development Nepal", "API integration Nepal", "Node.js backend developers", "business portal Nepal", "progressive web apps Nepal", "software modernisation Nepal"],
        "faqs": [
            ("What kinds of web apps do you build?", "Admin dashboards, customer portals, ecommerce platforms, SaaS products, booking systems and internal tools."),
            ("What backend technology do you use?", "We are stack agnostic: Node.js and the MERN stack, Python, PHP and more, with secure APIs and databases, chosen to fit your needs."),
            ("Can you integrate payments and other systems?", "Yes. We connect payments, CRMs, booking and other third party services cleanly and reliably."),
            ("Can you rebuild our old system?", "Yes. We modernise ageing internal tools into something your team enjoys using."),
            ("Do you offer support after launch?", "Yes. We stay on for maintenance, fixes and new features."),
        ]},
    "maint": {"name": "Website Maintenance & SEO", "url_name": "maintenance",
        "keywords": ["website maintenance Nepal", "website support Kathmandu", "SEO optimisation Nepal", "website security Nepal", "website speed optimisation Nepal", "technical SEO Kathmandu", "website backups and updates", "SEO meta and schema management", "uptime monitoring Nepal", "website care plan Nepal"],
        "faqs": [
            ("What is included in website maintenance?", "Uptime and security monitoring, regular backups, performance tuning, SEO meta and schema management, content updates and dependency updates."),
            ("Do you maintain sites you did not build?", "Yes. We audit the site first and then take maintenance off your plate."),
            ("How does maintenance help SEO?", "It keeps pages fast, secure and accurate, so rankings are not lost to broken links, slow load times or stale metadata."),
            ("How often do you back up my site?", "Automated backups run on a schedule we agree with you, so a bad update is never a disaster."),
            ("Can you also run ongoing SEO for us?", "Yes. Our team combines technical SEO with content and local SEO for Kathmandu and international search."),
        ]},
}

AB_PAGES = {
    "about": {"name": "About Us", "url_name": "about",
        "keywords": ["about Trend Crafters", "digital marketing agency Kathmandu", "creative agency Lalitpur", "marketing team Nepal", "branding and production agency Nepal", "Saksham Karki", "local soul global standards", "growth partner Nepal", "agency in Tempo Park", "Trend Crafters Global"],
        "faqs": [
            ("Who is Trend Crafters?", "A Kathmandu Valley agency that combines digital marketing, branding, photo and video production and IT solutions into one growth ecosystem."),
            ("Where are you based?", "Our studio is at Tempo Park, Lalitpur, serving clients across Nepal and internationally."),
            ("Who leads the company?", "Saksham Karki is the founder and CEO, supported by a team of project, marketing, social media, editing and design specialists."),
            ("What makes you different?", "One team for strategy, creative, production and technology, with material realism in our visuals and data behind every decision."),
            ("How can I work with you?", "Contact us through the form, WhatsApp or email. We start with a free discovery call."),
        ]},
    "partners": {"name": "Our Partners", "url_name": "partners",
        "keywords": ["Trend Crafters partners", "agency partners Nepal", "brand partners Kathmandu", "marketing collaborators Nepal", "creative partners Nepal", "technology partners Nepal", "media partners Nepal", "creator network Nepal", "industry associations Nepal", "platform partners"],
        "faqs": [
            ("Who do you partner with?", "Media and ad platforms, creator networks, industry associations, technology providers and the brands we grow with."),
            ("Can we partner with Trend Crafters?", "Yes. Reach out with your idea and we will explore how we can collaborate."),
            ("Do you work with creators and influencers?", "Yes. We source and brief Nepali creators for social and TikTok campaigns."),
            ("Do you work with agencies?", "Yes. We collaborate with other creative and technology teams when it serves the client."),
            ("Which clients have you worked with?", "See our Work page for campaigns across education, hospitality, automotive, fashion and manufacturing."),
        ]},
}
