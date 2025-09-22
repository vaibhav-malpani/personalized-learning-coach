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

3. **Run Google ADK**
   ```bash
   adk web
   ```

# Usage

## **🧬 Learning About Complex Topics:**

Ask the agent to explain the concept of "quantum mechanics".

**Student**: "Can you explain quantum mechanics to me?"

**Tutor Agent**: *Analyzes learning style and knowledge level*
- "I see you're interested in quantum mechanics! Let me assess your background first. Are you familiar with basic physics concepts like atoms and energy?"

**Topic Explainer**: *Provides foundational explanation*
- "Quantum mechanics is the branch of physics that describes how matter and energy behave at the smallest scales - think atoms and subatomic particles."

**Analogy Agent**: *Creates relatable metaphors*
- "Imagine quantum particles like spinning coins in the air - until you catch and look at them, they're spinning in all directions at once!"

**Question Generator**: *Tests understanding*
- "Which of the following best describes quantum superposition? A) Particles moving very fast B) Particles existing in multiple states simultaneously C) Particles being very small"

**Feedback Agent**: *Analyzes response and guides next steps*
- "Great job! You understand the basics. Let's dive deeper into quantum entanglement..."

---

## **📊 Mathematical Concepts - Adaptive Learning:**

**Student**: "I'm struggling with calculus derivatives"

**Tutor Agent**: *Identifies specific struggles*
- "Let's break this down step by step. Can you tell me what you find most confusing about derivatives?"

**Student**: "I don't understand what they actually represent"

**Topic Explainer**: *Provides conceptual foundation*
- "A derivative measures how fast something changes. It's the mathematical way to find the rate of change at any specific point."

**Analogy Agent**: *Visual and practical analogies*
- "Think of a car's speedometer - it shows your speed (rate of change of distance) at each moment. A derivative is like having a speedometer for any changing quantity!"

**Question Generator**: *Progressive difficulty*
- "If a ball is thrown upward, and its height is h(t) = -16t² + 32t + 6, what does the derivative tell us?"

**Student**: "The speed of the ball?"

**Feedback Agent**: *Encouraging correction*
- "You're on the right track! The derivative gives us the velocity (which includes direction), and the magnitude of velocity is speed. Let's practice with simpler examples..."

---

## **🎨 Creative Learning - Visual Learner:**

**Student**: "I need to understand photosynthesis for my biology test"

**Tutor Agent**: *Detects visual learning preference*
- "I notice you learn best with visual examples. Let me coordinate a multi-sensory explanation of photosynthesis."

**Topic Explainer**: *Structured scientific explanation*
- "Photosynthesis converts sunlight, water, and carbon dioxide into glucose and oxygen through two main stages: light reactions and the Calvin cycle."

**Analogy Agent**: *Rich visual metaphors*
- "Think of a plant like a solar-powered factory! The leaves are solar panels collecting sunlight, the roots are water pumps, and the stomata are air vents bringing in CO₂. The chloroplasts are tiny green machines that combine these ingredients to make sugar food!"

**Question Generator**: *Visual assessment*
- "Imagine you're shrinking down to enter a leaf. Draw or describe the journey of a CO₂ molecule from the air to becoming part of glucose."

**Feedback Agent**: *Builds on visual understanding*
- "Excellent visualization! Now let's connect this to the chemical equation: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂..."

---

## **🏛️ Historical Context Learning:**

**Student**: "Why did World War I start? It seems so complicated."

**Tutor Agent**: *Breaks down complexity*
- "You're right - it is complicated! Let's build understanding layer by layer, starting with the key players and their relationships."

**Topic Explainer**: *Chronological framework*
- "WWI began in 1914 due to a combination of factors: militarism, alliances, imperialism, and nationalism - often called the MAIN causes."

**Analogy Agent**: *Modern parallels*
- "Imagine Europe as a high school where different friend groups (alliances) have been building up tensions. When one incident happens (assassination of Archduke Franz Ferdinand), it's like a fight breaking out that pulls in all the friend groups because of their loyalty promises."

**Question Generator**: *Critical thinking*
- "If you were a leader in 1914, knowing what you know now, what could have been done differently to prevent the war?"

**Feedback Agent**: *Historical analysis*
- "That's thoughtful reasoning! Your answer shows you understand how small diplomatic changes might have had huge consequences. Let's explore how the alliance system made the conflict inevitable..."

---

## **🧪 Hands-On Science Learning:**

**Student**: "I have to do an experiment on acids and bases but I don't really get what pH means"

**Tutor Agent**: *Connects theory to practice*
- "Perfect! Understanding pH will make your experiment much more meaningful. Let's start with what you observe daily."

**Topic Explainer**: *Practical foundation*
- "pH measures how acidic or basic a solution is on a scale from 0 to 14. Pure water is neutral at pH 7."

**Analogy Agent**: *Everyday examples*
- "Think of pH like a friendship scale! pH 7 is perfectly balanced friendship. Below 7 (acidic) is like having a friend who's a bit sour or bitter. Above 7 (basic) is like having a friend who's really sweet - sometimes too sweet!"

**Question Generator**: *Experiment design*
- "You're testing household items. Predict: Will lemon juice (citrus) be above or below pH 7? What about baking soda dissolved in water?"

**Student**: "Lemon juice below 7, baking soda above?"

**Feedback Agent**: *Experiment guidance*
- "Exactly right! Now during your experiment, you'll see these predictions confirmed. Try testing coffee, soap, and milk too - can you predict where they'll fall and why?"

---

## **📚 Language Learning - Progressive Difficulty:**

**Student**: "I'm learning Spanish but I keep mixing up ser and estar (both mean 'to be')"

**Tutor Agent**: *Identifies specific grammar challenge*
- "Ah, the classic ser vs estar challenge! This trips up many Spanish learners. Let's master this with clear patterns."

**Topic Explainer**: *Grammar rules*
- "'Ser' is for permanent characteristics and identity. 'Estar' is for temporary states and locations."

**Analogy Agent**: *Memory devices*
- "Think 'SER' = 'SERious' permanent things (who you are, what you do, where you're from). Think 'ESTAR' = 'STAte' of being right now (how you feel, where you are temporarily)."

**Question Generator**: *Pattern practice*
- "Choose ser or estar: 'María ___ doctora' (María is a doctor) vs 'María ___ enferma' (María is sick today)"

**Student**: "Ser for doctor, estar for sick?"

**Feedback Agent**: *Reinforces pattern*
- "¡Perfecto! You've got it! Doctor is her profession (permanent), sick is temporary. Let's practice with more examples: 'La fiesta ___ en mi casa' (The party is at my house)..."


