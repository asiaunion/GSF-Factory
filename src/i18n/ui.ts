export const languages = {
  en: 'English',
  ko: '한국어',
  ja: '日本語',
};

export const defaultLang = 'en';

export const ui = {
  en: {
    'nav.posts': 'Posts',
    'nav.tags': 'Tags',
    'nav.about': 'About',
    'nav.archives': 'Archives',
    'nav.search': 'Search',
    'recent.title': 'Recent Posts',
    'featured.title': 'Featured',
  },
  ko: {
    'nav.posts': '포스트',
    'nav.tags': '태그',
    'nav.about': '소개',
    'nav.archives': '기록',
    'nav.search': '검색',
    'recent.title': '최근 포스팅',
    'featured.title': '주요 포스팅',
  },
  ja: {
    'nav.posts': '記事',
    'nav.tags': 'タグ',
    'nav.about': '紹介',
    'nav.archives': 'アーカイブ',
    'nav.search': '検索',
    'recent.title': '最近の記事',
    'featured.title': 'おすすめ記事',
  },
} as const;

export function useTranslations(lang: keyof typeof ui) {
  return function t(key: keyof typeof ui[typeof defaultLang]) {
    return ui[lang][key] || ui[defaultLang][key];
  }
}
