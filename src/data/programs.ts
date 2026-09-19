import type { Program } from './types';
import afterSchoolImg from '../assets/after-school.jpg';
import culinaryImg from '../assets/gallery/culinary.jpg';
import imcoImg from '../assets/gallery/baylor-imco-music.jpg';
import keyboardImg from '../assets/gallery/learning-keyboard.jpg';
import namelessImg from '../assets/gallery/nameless-sound.jpg';
import creativityImg from '../assets/gallery/creativity.jpg';

export const programs: Program[] = [
	{
		slug: 'after-school',
		name: 'After-School Program',
		summary:
			'Homework help, enrichment activities, and a safe place to grow — every school day.',
		details: [
			'Monday through Thursday, 4:00–6:00 PM',
			'2025–26 session starts August 19, 2025',
			'Open to south side Houston youth',
			'Snacks, tutoring, and structured activities included',
		],
		image: afterSchoolImg,
		alt: 'Instructor with djembe drums surrounded by SYP kids at the after-school program',
	},
	{
		slug: 'imco',
		name: 'IMCO — Medical Careers',
		summary:
			'Inner-city Medical Career Opportunity, presented with Baylor College of Medicine.',
		details: [
			'10 sessions, the first Saturday of each month, 9:00 AM',
			'2025–26 sessions begin October 3, 2025',
			'Taught by physicians and residents from Baylor College of Medicine',
			'Hands-on, interactive labs introducing medicine and health sciences',
			'Enrollment is limited — sign up early',
		],
		image: imcoImg,
		alt: 'SYP students in the Baylor IMCO music and learning ensemble',
	},
	{
		slug: 'music',
		name: 'Music Classes',
		summary:
			'Keyboard, percussion, and marimba classes in partnership with Nameless Sound.',
		details: [
			'Group keyboard and percussion classes',
			'Instruments provided — no experience needed',
			'Led by teaching artists from the Nameless Sound collaboration',
		],
		image: keyboardImg,
		alt: 'Young man learning keyboard with drums in the background',
	},
	{
		slug: 'arts',
		name: 'Arts & Creativity',
		summary:
			'Hands-on building, crafting, and creative play that grows confidence and imagination.',
		details: [
			'Creative building and craft activities',
			'Part of the daily after-school rotation',
		],
		image: creativityImg,
		alt: 'Smiling girl with a magnetic tile construction',
	},
	{
		slug: 'culinary',
		name: 'Culinary Program',
		summary:
			'Youth cooking and healthy-eating workshops — from kitchen basics to full meals.',
		details: [
			'Cooking skills and kitchen safety',
			'Nutrition and healthy eating on a budget',
		],
		image: culinaryImg,
		alt: 'Young person in a chef’s hat and apron',
	},
];

export { namelessImg };
