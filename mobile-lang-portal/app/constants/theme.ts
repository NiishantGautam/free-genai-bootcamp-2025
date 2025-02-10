export type Theme = {
  background: string;
  text: string;
  textSecondary: string;
  primary: string;
  secondary: string;
  accent: string;
  card: string;
  cardDark: string;
  border: string;
  progressCircle: string;
  chapterButton: string;
  chapterButtonActive: string;
};

export const lightTheme: Theme = {
  background: '#FFFFFF',
  text: '#1A1A1A',
  textSecondary: '#666666',
  primary: '#0095FF',
  secondary: '#FF6B2C',
  accent: '#FFA500',
  card: '#F5F5F5',
  cardDark: '#2A2A2A',
  border: '#E5E5EA',
  progressCircle: '#E5E5EA',
  chapterButton: '#F2F2F7',
  chapterButtonActive: '#0095FF',
};

export const darkTheme: Theme = {
  background: '#1C1C1E',
  text: '#FFFFFF',
  textSecondary: '#A0A0A0',
  primary: '#0095FF',
  secondary: '#FF6B2C',
  accent: '#FFA500',
  card: '#2A2A2A',
  cardDark: '#232323',
  border: '#3A3A3C',
  progressCircle: '#3A3A3C',
  chapterButton: '#2A2A2A',
  chapterButtonActive: '#0095FF',
};
