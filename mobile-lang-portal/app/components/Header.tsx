import React from "react";
import { Text, View, StyleSheet } from "react-native";

export default function Header() {
  return (
    <View style={styles.header}>
      <Text style={styles.greeting}>Happy learning, niishantgautam</Text>
      <View style={styles.streakContainer}>
        <Text style={styles.streak}>🔥 0 day streak</Text>
        <Text style={styles.today}>Today: 0/10</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  header: {
    flexDirection: "row", // Arrange items horizontally
    justifyContent: "space-between", // Distribute space between greeting and streak
    alignItems: "center", // Vertically align items
    padding: 16, // Add padding around the header
    backgroundColor: "#f0f0f0", // Example background color
  },
  greeting: {
    fontSize: 18,
    fontWeight: "bold",
  },
  streakContainer: {
    alignItems: "flex-end", // Align streak and today to the right
  },
  streak: {
    fontSize: 16,
  },
  today: {
    fontSize: 14,
    color: "#777", // Example color
  },
});
