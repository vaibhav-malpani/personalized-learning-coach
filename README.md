# Personalized Learning Coach 🎓

A sophisticated multi-agent learning system built with Google's Agent Development Kit (ADK) that demonstrates the power of iterative refinement and intelligent tutoring through AI agents.

## Overview

This system creates a personalized learning experience where AI agents work together to:
- Analyze student learning styles and knowledge levels
- Provide tailored explanations and analogies
- Generate assessment questions
- Analyze student responses and iteratively improve teaching approaches
- Maintain encouraging feedback throughout the learning process

## System Architecture

The system consists of 5 specialized AI agents:

### 🎯 **Tutor Agent (Orchestrator)**
- Analyzes user learning style and knowledge level
- Coordinates other agents based on student needs
- Adapts teaching strategy based on feedback

### 📚 **Topic Explainer Agent**
- Provides core explanations of complex topics
- Adjusts complexity based on student level
- Focuses on scientific accuracy while maintaining accessibility

### 🌟 **Analogy Agent**
- Creates age-appropriate metaphors and analogies
- Generates multiple analogy types for different learning styles
- Simplifies complex concepts using familiar examples

### 🤔 **Question Generator Agent**
- Creates assessment questions to check understanding
- Generates mix of multiple choice and open-ended questions
- Provides explanations for correct answers

### 🔄 **Feedback Agent (Loop Controller)**
- Analyzes student responses to determine understanding level
- Controls the learning loop by directing other agents
- Provides encouraging feedback and determines next steps

## Features

- **🔄 Iterative Learning Loop**: System adapts based on student responses
- **🎯 Personalized Approach**: Tailors content to individual learning styles
- **📈 Progress Tracking**: Monitors learning progress across sessions
- **💬 Encouraging Feedback**: Maintains motivation with supportive responses
- **🧩 Multi-Level Content**: Supports beginner to advanced explanations
- **🌟 Rich Analogies**: Uses creative metaphors to clarify complex concepts

## Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Google Cloud (for full ADK functionality)**
   ```bash
   # Install Google Cloud CLI
   # Create a Google Cloud project
   # Enable Vertex AI API
   # Set up authentication
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   ```

3. **Install Google ADK**
   ```bash
   pip install google-adk
   ```

