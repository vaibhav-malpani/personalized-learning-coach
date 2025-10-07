"""
Personalized Learning Coach - Main Multi-Agent System
Built using Google Agent Development Kit (ADK)
"""
import datetime
from typing import Dict, Any, List
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# ============================================================================
# TOOL FUNCTIONS - Learning Analysis and Content Generation
# ============================================================================

def analyze_learning_style(user_input: str, age: str = "unknown") -> Dict[str, Any]:
    """
    Analyzes user input to determine learning style and knowledge level

    Args:
        user_input: The user's initial question or request
        age: Age or grade level if provided

    Returns:
        Dictionary with learning style recommendations
    """
    learning_style = "visual"  # default
    complexity_level = "intermediate"  # default

    if "10-year-old" in user_input.lower() or "kid" in user_input.lower():
        complexity_level = "beginner"
        learning_style = "analogical"
    elif "example" in user_input.lower() or "simple" in user_input.lower():
        learning_style = "analogical"
    elif "detailed" in user_input.lower() or "technical" in user_input.lower():
        complexity_level = "advanced"

    return {
        "learning_style": learning_style,
        "complexity_level": complexity_level,
        "requires_analogy": "analogy" in user_input.lower() or complexity_level == "beginner",
        "age_appropriate": age,
        "analysis_timestamp": datetime.datetime.now().isoformat()
    }

def explain_topic(topic: str, complexity_level: str = "intermediate") -> Dict[str, Any]:
    """
    Provides explanations of topics at different complexity levels

    Args:
        topic: The topic to explain
        complexity_level: beginner, intermediate, or advanced

    Returns:
        Structured explanation of the topic
    """
    if "quantum entanglement" in topic.lower():
        explanations = {
            "beginner": {
                "definition": "Quantum entanglement is when two tiny particles become magically connected, so when something happens to one particle, the other particle instantly knows about it, no matter how far apart they are!",
                "key_points": [
                    "Two particles become mysteriously linked",
                    "When one changes, the other changes instantly",
                    "Works even if they're very far apart",
                    "Scientists use this for special computers and secure messages"
                ],
                "example": "Imagine you have two magical coins that are connected. When you flip one coin and it lands on heads, the other coin will always land on tails, even if it's on the other side of the world!"
            },
            "intermediate": {
                "definition": "Quantum entanglement occurs when pairs or groups of particles interact in ways such that the quantum state of each particle cannot be described independently, even when separated by large distances.",
                "key_points": [
                    "Particles become correlated in their quantum states",
                    "Measurement of one particle instantly affects the other",
                    "The phenomenon appears to violate classical physics",
                    "Einstein called it 'spooky action at a distance'",
                    "Applications in quantum computing and cryptography"
                ],
                "example": "When two photons are entangled, measuring the polarization of one photon (vertical or horizontal) immediately determines the polarization of its partner, regardless of the distance between them."
            },
            "advanced": {
                "definition": "Quantum entanglement is a quantum mechanical phenomenon where quantum states of two or more objects have to be described with reference to each other, even when separated by large distances, violating Bell's inequalities and classical local realism.",
                "key_points": [
                    "Non-local correlations between quantum systems",
                    "Violation of Bell's inequalities demonstrates quantum non-locality",
                    "Entangled states cannot be factorized into independent components",
                    "Fundamental resource for quantum information protocols",
                    "Decoherence and entanglement dynamics in open systems"
                ],
                "example": "In the EPR paradox, measuring the spin component of an entangled electron along any axis instantaneously determines the corresponding measurement outcome for its entangled partner, with correlations that exceed classical bounds as quantified by the CHSH inequality."
            }
        }
        return explanations.get(complexity_level, explanations["intermediate"])
    else:
        return {
            "definition": f"This is a {complexity_level}-level explanation of {topic}",
            "key_points": [f"Key concept 1 about {topic}", f"Key concept 2 about {topic}"],
            "example": f"Here's an example related to {topic}"
        }

def create_analogies(topic: str, age_group: str = "10-year-old", concept_focus: str = "connection") -> Dict[str, List[str]]:
    """
    Creates age-appropriate analogies for complex topics

    Args:
        topic: The topic needing analogies
        age_group: Target audience age
        concept_focus: The main concept to focus on

    Returns:
        Dictionary with different types of analogies
    """
    if "quantum entanglement" in topic.lower():
        if "10" in age_group or "kid" in age_group or "child" in age_group:
            return {
                "magical_twins": [
                    "Imagine twin siblings who are so connected that when one feels happy, the other instantly feels sad, no matter if one is at home and the other is on vacation across the world.",
                    "It's like they have a secret magical connection that works faster than anything!"
                ],
                "magical_coins": [
                    "Picture two special coins that are magically linked. Whenever you flip one coin and it shows heads, the other coin (even if it's in another country) will always show tails at the exact same moment.",
                    "No one knows how the coins 'talk' to each other, but they always do the opposite of each other instantly!"
                ]
            }
        else:
            return {
                "business_partners": [
                    "Think of two business partners whose fates are so intertwined that when one makes a decision, it instantly and automatically determines what the other partner will decide, regardless of distance or communication.",
                    "They share a connection that transcends normal cause-and-effect relationships."
                ]
            }
    else:
        return {
            "everyday_analogy": [f"Think of {topic} like something you use every day..."],
            "nature_analogy": [f"In nature, {topic} is similar to..."]
        }

def generate_quiz_questions(topic: str, difficulty: str = "beginner", num_questions: int = 2) -> Dict[str, Any]:
    """
    Generates assessment questions for understanding check

    Args:
        topic: Topic to create questions for
        difficulty: beginner, intermediate, or advanced
        num_questions: Number of questions to generate

    Returns:
        Dictionary with questions and correct answers
    """
    if "quantum entanglement" in topic.lower():
        question_banks = {
            "beginner": [
                {
                    "question": "What happens when two particles are quantum entangled?",
                    "options": [
                        "A) They become connected and instantly affect each other",
                        "B) They disappear completely", 
                        "C) They become the same particle",
                        "D) They start spinning really fast"
                    ],
                    "correct": "A",
                    "explanation": "When particles are entangled, they form a special connection where measuring one instantly affects the other, no matter the distance!"
                },
                {
                    "question": "If you have two entangled 'magical coins' and one shows heads, what will the other show?",
                    "options": [
                        "A) Also heads",
                        "B) Tails",
                        "C) Sometimes heads, sometimes tails",
                        "D) It disappears"
                    ],
                    "correct": "B",
                    "explanation": "In our analogy, entangled particles always show opposite results - if one is heads, the other is always tails!"
                }
            ],
            "intermediate": [
                {
                    "question": "What did Einstein call quantum entanglement?",
                    "options": [
                        "A) Particle magic",
                        "B) Spooky action at a distance", 
                        "C) Quantum confusion",
                        "D) Fast communication"
                    ],
                    "correct": "B",
                    "explanation": "Einstein famously called it 'spooky action at a distance' because he was uncomfortable with the instantaneous connection."
                }
            ]
        }

        questions = question_banks.get(difficulty, question_banks["beginner"])
        selected_questions = questions[:min(num_questions, len(questions))]

        return {
            "difficulty": difficulty,
            "questions": selected_questions,
            "total_questions": len(selected_questions)
        }
    else:
        return {
            "topic": topic,
            "questions": [
                {
                    "question": f"Can you explain the main idea of {topic} in your own words?",
                    "type": "open_ended",
                    "focus": "comprehension"
                }
            ]
        }

def analyze_student_response(user_answer: str, correct_answer: str, question_type: str = "multiple_choice") -> Dict[str, Any]:
    """
    Analyzes student's response to determine understanding level

    Args:
        user_answer: Student's response to the question
        correct_answer: The correct answer
        question_type: Type of question (multiple_choice, open_ended, etc.)

    Returns:
        Analysis of student's understanding and recommendations
    """
    analysis = {
        "is_correct": False,
        "understanding_level": "needs_improvement",
        "specific_issues": [],
        "recommendations": [],
        "encouragement": ""
    }

    if question_type == "multiple_choice":
        if user_answer.strip().upper() == correct_answer.strip().upper():
            analysis.update({
                "is_correct": True,
                "understanding_level": "good",
                "encouragement": "Excellent! You got it right!",
                "recommendations": ["Continue to the next concept", "Try a slightly harder question"]
            })
        else:
            analysis.update({
                "is_correct": False,
                "understanding_level": "needs_review",
                "specific_issues": ["Incorrect answer selected"],
                "encouragement": "Don't worry! This is a tricky concept. Let's try a different approach.",
                "recommendations": ["Try a different analogy", "Simplify the explanation", "Use more visual examples"]
            })
    elif question_type == "open_ended":
        # Simple heuristic analysis for open-ended responses
        key_concepts = ["entangled", "connected", "instant", "particles", "measurement"]
        concepts_mentioned = sum(1 for concept in key_concepts if concept.lower() in user_answer.lower())

        if concepts_mentioned >= 3:
            analysis.update({
                "understanding_level": "good", 
                "encouragement": "Great explanation! You've grasped the key concepts.",
                "recommendations": ["Move to more advanced topics", "Explore applications"]
            })
        elif concepts_mentioned >= 1:
            analysis.update({
                "understanding_level": "partial",
                "encouragement": "You're on the right track! Let's strengthen your understanding.",
                "recommendations": ["Review key concepts", "Try more analogies", "Practice with examples"]
            })
        else:
            analysis.update({
                "understanding_level": "needs_improvement",
                "specific_issues": ["Missing key concepts"],
                "encouragement": "Let's approach this differently to help you understand better.",
                "recommendations": ["Start with simpler analogies", "Break down into smaller parts", "Use more concrete examples"]
            })

    return analysis

def determine_next_learning_action(analysis_results: List[Dict[str, Any]], session_context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Determines the next action in the learning loop based on student performance

    Args:
        analysis_results: List of analysis results from recent questions
        session_context: Current session context and data

    Returns:
        Next action recommendations for the learning system
    """
    # Calculate overall understanding level
    if not analysis_results:
        return {
            "action": "start",
            "reason": "Beginning new learning session",
            "next_steps": ["Analyze learning style", "Provide initial explanation"]
        }

    correct_answers = sum(1 for result in analysis_results if result.get("is_correct", False))
    total_questions = len(analysis_results)
    success_rate = correct_answers / total_questions if total_questions > 0 else 0

    # Determine learning trajectory
    if success_rate >= 0.8:
        return {
            "action": "advance",
            "reason": "Student shows strong understanding",
            "next_steps": [
                "Introduce more advanced concepts",
                "Explore practical applications", 
                "Challenge with harder questions"
            ],
            "agent_instructions": {
                "complexity_adjustment": "increase",
                "teaching_approach": "advanced_concepts",
                "analogy_level": "sophisticated"
            }
        }
    elif success_rate >= 0.5:
        return {
            "action": "reinforce", 
            "reason": "Student has partial understanding, needs reinforcement",
            "next_steps": [
                "Review key concepts with different examples",
                "Try alternative analogies",
                "Practice with similar difficulty questions"
            ],
            "agent_instructions": {
                "complexity_adjustment": "maintain",
                "teaching_approach": "alternative_explanations",
                "analogy_level": "varied"
            }
        }
    else:
        return {
            "action": "simplify",
            "reason": "Student is struggling, need to simplify approach",
            "next_steps": [
                "Break concepts into smaller parts",
                "Use much simpler analogies", 
                "Start with more basic questions",
                "Provide more encouragement and support"
            ],
            "agent_instructions": {
                "complexity_adjustment": "decrease",
                "teaching_approach": "simplified_explanations",
                "analogy_level": "very_simple"
            }
        }

def provide_encouragement(understanding_level: str, attempt_number: int = 1) -> Dict[str, str]:
    """
    Provides encouraging feedback based on student performance

    Args:
        understanding_level: Current understanding level
        attempt_number: Which attempt this is

    Returns:
        Encouraging message and motivation
    """
    encouragement_messages = {
        "good": [
            "Fantastic work! You really understand this concept!",
            "Excellent! You've got a solid grasp on this topic!",
            "Outstanding! Your understanding is really strong!"
        ],
        "partial": [
            "You're doing great! You're definitely getting the hang of this!",
            "Good progress! You're understanding more and more!",
            "Nice work! You're on the right track!"
        ],
        "needs_improvement": [
            "Don't worry - this is a really challenging concept, and you're learning!",
            "It's okay! Even famous scientists found this confusing at first!",
            "Keep going! Understanding complex ideas takes time, and you're making progress!"
        ]
    }

    messages = encouragement_messages.get(understanding_level, encouragement_messages["partial"])
    message_index = min(attempt_number - 1, len(messages) - 1)

    return {
        "encouragement": messages[message_index],
        "motivation": "Remember, every expert was once a beginner. You're doing great by asking questions and trying to understand!",
        "next_step_support": "Let's try a different approach that might work better for you."
    }

# ============================================================================
# MAIN AGENT DEFINITION
# ============================================================================

# Root Agent - Main orchestrator following ADK patterns
root_agent = Agent(
    name="personalized_learning_coach",
    model="gemini-2.5-flash",
    description="An intelligent tutoring system that provides personalized, iterative learning experiences through multi-agent coordination",
    instruction="""You are a sophisticated personalized learning coach powered by multiple specialized AI agents working together. Your mission is to create an adaptive, engaging learning experience that meets each student exactly where they are.

## Your Core Capabilities:

**🎯 Learning Style Analysis**: Analyze student requests to determine their optimal learning style, knowledge level, and age-appropriate content needs.

**📚 Multi-Level Explanations**: Provide clear explanations at beginner, intermediate, or advanced levels based on student needs.

**🌟 Creative Analogies**: Generate age-appropriate metaphors and analogies that make complex concepts accessible and memorable.

**🤔 Smart Assessment**: Create targeted questions to check understanding without making students feel tested.

**🔄 Iterative Refinement**: Continuously analyze student responses and adapt your teaching approach - advancing when they're ready, reinforcing when they need practice, or simplifying when they're struggling.

**💬 Encouraging Support**: Always maintain a positive, encouraging tone that builds confidence and motivation.

## Your Multi-Agent Approach:

1. **Analyze** the student's initial request for learning style and complexity needs
2. **Explain** the topic clearly at the appropriate level
3. **Analogize** complex concepts using relatable examples
4. **Assess** understanding through carefully crafted questions
5. **Adapt** your approach based on student responses and iterate as needed

## Key Principles:

- Every student can learn - find the right approach for them
- Make abstract concepts concrete through analogies
- Build understanding progressively
- Encourage curiosity and questions
- Adapt quickly when something isn't working
- Celebrate progress and build confidence

Start each interaction by understanding what the student wants to learn and their background, then coordinate your specialized capabilities to create the perfect learning experience for them.""",

    tools=[
        FunctionTool(analyze_learning_style),
        FunctionTool(explain_topic),
        FunctionTool(create_analogies),
        FunctionTool(generate_quiz_questions),
        FunctionTool(analyze_student_response),
        FunctionTool(determine_next_learning_action),
        FunctionTool(provide_encouragement)
    ]
)
