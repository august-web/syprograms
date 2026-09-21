export const SITE_NAME = 'Southside Youth Programs';
export const SITE_TAGLINE =
	'After-school enrichment and youth development for Houston’s Southside';
export const SITE_URL = 'https://syprograms.org';

export const PHONE_MAIN = '281-536-8292';
export const PHONE_MAIN_HREF = 'tel:+12815368292';
export const PHONE_IMCO = '832-520-5031';
export const PHONE_IMCO_HREF = 'tel:+18325205031';

export const EMAIL_MAIN = 'southside917@aol.com';
export const EMAIL_IMCO = 'oraysteven@gmail.com';

export const ADDRESS_STREET = '7210 Peerless St, Suite B';
export const ADDRESS_LOCALITY = 'Houston, TX 77021';

export const MAILTO_MAIN = `mailto:${EMAIL_MAIN}`;
export const MAILTO_IMCO = `mailto:${EMAIL_IMCO}`;

/**
 * Build a mailto: link with a prefilled subject and body — this site's
 * contact "form" has no backend, so submissions open the visitor's
 * email client instead.
 */
export function mailtoLink(options: {
	subject: string;
	body?: string;
	to?: string;
}): string {
	const to = options.to ?? EMAIL_MAIN;
	const params = new URLSearchParams();
	params.set('subject', options.subject);
	if (options.body) params.set('body', options.body);
	return `mailto:${to}?${params.toString().replace(/\+/g, '%20')}`;
}
