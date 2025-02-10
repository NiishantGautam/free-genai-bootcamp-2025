import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
  Image,
  SafeAreaView,
  useColorScheme,
  Dimensions,
} from 'react-native';
import Entypo from '@expo/vector-icons/Entypo';
import { lightTheme, darkTheme, Theme } from '../constants/theme';

export default function HomePage() {
  // Initialize theme based on system preference
  const systemColorScheme = useColorScheme();
  const [isDarkMode, setIsDarkMode] = useState(systemColorScheme === 'dark');
  const theme = isDarkMode ? darkTheme : lightTheme;

  // Progress and chapters data
  const progressItems = Array(7).fill(0);
  const chapters = [
    'Intro to TypeScript',
    'The any type',
    'TypeScript ES6/ES5',
    'Primitive types',
    'Union types',
    'The void type',
    'Arrays',
    'Tuples',
    'Literal types',
    'Functions',
    'Modules',
  ];

  // Theme toggle handler
  const toggleTheme = () => setIsDarkMode(!isDarkMode);

  return (
    <SafeAreaView style={[styles.container, { backgroundColor: theme.background }]}>
      <ScrollView style={styles.scrollView} showsVerticalScrollIndicator={false}>
        {/* Header Section */}
        <View style={styles.header}>
          <View style={styles.userInfo}>
            <Image
              source={{
                uri: 'https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-JqUrjNb2IUEjiEPQbp49sTqq01Jo3y.png',
              }}
              style={styles.avatar}
            />
            <Text style={[styles.username, { color: theme.text }]}>
              nishantgautam
            </Text>
          </View>
          <TouchableOpacity onPress={toggleTheme} style={styles.themeToggle}>
            <Entypo
              name={isDarkMode ? 'light-up' : 'moon'}
              size={24}
              color={theme.text}
            />
          </TouchableOpacity>
        </View>

        {/* Streak Counter */}
        <View style={[styles.streakContainer, { backgroundColor: theme.card }]}>
          <Entypo name="feather" size={20} color={theme.accent} />
          <Text style={[styles.streakText, { color: theme.text }]}>
            0 day streak
          </Text>
        </View>

        {/* Progress Indicators */}
        <View style={styles.progressContainer}>
          {progressItems.map((_, index) => (
            <View
              key={index}
              style={[
                styles.progressCircle,
                { borderColor: theme.progressCircle },
                index === 0 && { backgroundColor: theme.accent },
              ]}
            >
              <Text
                style={[
                  styles.progressText,
                  { color: index === 0 ? '#000' : theme.text },
                ]}
              >
                {index + 1}
              </Text>
            </View>
          ))}
        </View>

        {/* Action Cards */}
        <View style={styles.cardsContainer}>
          <TouchableOpacity
            style={[styles.card, { backgroundColor: theme.primary }]}
          >
            <Entypo name="feather" size={24} color="#FFF" />
            <View style={styles.cardContent}>
              <Text style={styles.cardTitle}>Practice flashcards</Text>
              <Text style={styles.cardDescription}>
                Answer questions based on the topics you are learning in the course.
              </Text>
            </View>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.card, { backgroundColor: theme.secondary }]}
          >
            <Entypo name="feather" size={24} color="#FFF" />
            <View style={styles.cardContent}>
              <Text style={styles.cardTitle}>Review flashcards</Text>
              <Text style={styles.cardDescription}>
                Refresh your memory by answering questions you've previously
                tackled.
              </Text>
            </View>
          </TouchableOpacity>
        </View>

        {/* Chapters Section */}
        <View style={styles.chaptersSection}>
          <Text style={[styles.sectionTitle, { color: theme.text }]}>
            Explore chapters
          </Text>
          <View style={styles.chaptersGrid}>
            {chapters.map((chapter, index) => (
              <TouchableOpacity
                key={index}
                style={[
                  styles.chapterButton,
                  { backgroundColor: theme.chapterButton },
                ]}
              >
                <Text style={[styles.chapterText, { color: theme.text }]}>
                  {chapter}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const { width } = Dimensions.get('window');
const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
    padding: 16,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 24,
  },
  userInfo: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  avatar: {
    width: 44,
    height: 44,
    borderRadius: 22,
    marginRight: 12,
  },
  username: {
    fontSize: 18,
    fontWeight: '600',
  },
  themeToggle: {
    padding: 8,
  },
  streakContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 16,
    borderRadius: 12,
    marginBottom: 24,
  },
  streakText: {
    marginLeft: 12,
    fontSize: 16,
    fontWeight: '500',
  },
  progressContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 32,
    paddingHorizontal: 8,
  },
  progressCircle: {
    width: 40,
    height: 40,
    borderRadius: 20,
    borderWidth: 2,
    justifyContent: 'center',
    alignItems: 'center',
  },
  progressText: {
    fontSize: 16,
    fontWeight: '500',
  },
  cardsContainer: {
    gap: 16,
    marginBottom: 32,
  },
  card: {
    padding: 20,
    borderRadius: 16,
    flexDirection: 'row',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  cardContent: {
    marginLeft: 16,
    flex: 1,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 6,
    color: '#FFF',
  },
  cardDescription: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.9)',
    lineHeight: 20,
  },
  chaptersSection: {
    marginTop: 8,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '600',
    marginBottom: 16,
  },
  chaptersGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
  },
  chapterButton: {
    padding: 16,
    borderRadius: 12,
    width: (width - 44) / 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  chapterText: {
    fontSize: 15,
    fontWeight: '500',
  },
});
