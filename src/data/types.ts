import type { ImageMetadata } from 'astro';

export interface Program {
	slug: string;
	name: string;
	summary: string;
	details: string[];
	image: ImageMetadata;
	alt: string;
}

export interface GalleryPhoto {
	src: ImageMetadata;
	caption: string;
	alt: string;
}
