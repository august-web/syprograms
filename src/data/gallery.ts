import type { GalleryPhoto } from './types';
import namelessSound from '../assets/gallery/nameless-sound.jpg';
import baylorImco from '../assets/gallery/baylor-imco-music.jpg';
import villagePeople from '../assets/gallery/village-people.jpg';
import musicClass from '../assets/gallery/music-class.jpg';
import learningKeyboard from '../assets/gallery/learning-keyboard.jpg';
import creativity from '../assets/gallery/creativity.jpg';
import pride from '../assets/gallery/pride.jpg';
import culinary from '../assets/gallery/culinary.jpg';

export const galleryPhotos: GalleryPhoto[] = [
	{
		src: namelessSound,
		caption: 'Nameless Sound',
		alt: 'Girl playing a djembe-style hand drum',
	},
	{
		src: baylorImco,
		caption: 'Baylor SYP IMCO',
		alt: 'Group music class with keyboard, congas, xylophone, and drum circle',
	},
	{
		src: villagePeople,
		caption: 'The Village People',
		alt: 'Group photo in the green-walled SYP center',
	},
	{
		src: musicClass,
		caption: 'Music Class',
		alt: 'Two girls playing an electronic keyboard together',
	},
	{
		src: learningKeyboard,
		caption: 'Learning Keyboard',
		alt: 'Young man at the keyboard with djembe and marimba behind him',
	},
	{
		src: creativity,
		caption: 'Creativity',
		alt: 'Smiling girl with magnetic tile construction on a colorful rug',
	},
	{
		src: pride,
		caption: 'Pride',
		alt: 'Diverse hands joined in a team huddle',
	},
	{
		src: culinary,
		caption: 'Culinary',
		alt: 'Young person in a white chef’s hat and apron',
	},
];
