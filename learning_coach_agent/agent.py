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

    Note: This function returns a structured request for the LLM to generate
    the explanation. The actual content generation happens through the agent.

    Args:
        topic: The topic to explain
        complexity_level: beginner, intermediate, or advanced

    Returns:
        Structured guidance for explanation generation
    """
    return {
        "topic": topic,
        "complexity_level": complexity_level,
        "structure_needed": {
            "definition": f"Provide a clear, {complexity_level}-level definition of {topic}",
            "key_points": f"List 3-5 key points about {topic} appropriate for {complexity_level} level",
            "example": f"Give a concrete, relatable example that illustrates {topic} at {complexity_level} level"
        },
        "guidelines": {
            "beginner": "Use simple language, avoid jargon, make it fun and engaging",
            "intermediate": "Use some technical terms but explain them, balance accessibility with accuracy",
            "advanced": "Use precise technical terminology, include nuances and complexities"
        }.get(complexity_level, "Balance clarity with accuracy")
    }

def create_analogies(topic: str, age_group: str = "10-year-old", concept_focus: str = "connection") -> Dict[str, Any]:
    """
    Creates age-appropriate analogies for complex topics

    Note: This function provides guidance for the LLM to generate
    creative, age-appropriate analogies dynamically.

    Args:
        topic: The topic needing analogies
        age_group: Target audience age
        concept_focus: The main concept to focus on

    Returns:
        Structured request for analogy generation
    """
    is_young_audience = any(indicator in age_group.lower() for indicator in ["10", "kid", "child", "young", "elementary"])

    return {
        "topic": topic,
        "age_group": age_group,
        "concept_focus": concept_focus,
        "analogy_requirements": {
            "count": 2,
            "types": ["everyday_object", "relatable_situation"],
            "style": "magical and fun" if is_young_audience else "relatable and clear",
            "complexity": "very simple" if is_young_audience else "moderately sophisticated"
        },
        "guidelines": f"Create 2-3 creative analogies that explain {topic} (specifically focusing on {concept_focus}) for {age_group}. Use things they encounter in daily life. Make it memorable and engaging."
    }

def suggest_real_world_applications(topic: str, age_group: str = "general", interest_area: str = "general") -> Dict[str, Any]:
    """
    Suggests real-world applications and practical uses of concepts being learned

    Note: This function provides structured guidance for the LLM to generate
    relevant, motivating real-world connections for any topic.

    Args:
        topic: The topic to find applications for
        age_group: Target audience age (helps determine appropriate career/application complexity)
        interest_area: Student's interests if known (e.g., "gaming", "sports", "art", "science")

    Returns:
        Structured guidance for generating real-world application examples
    """
    is_young_audience = any(indicator in age_group.lower() for indicator in ["10", "kid", "child", "young", "elementary"])

    application_categories = {
        "career_applications": {
            "description": "Jobs and careers that use this concept daily",
            "count": 3,
            "style": "aspirational and exciting" if is_young_audience else "realistic and diverse",
            "include": ["job title", "how they use it", "why it matters in that field"]
        },
        "everyday_uses": {
            "description": "How ordinary people use this in daily life",
            "count": 3,
            "style": "relatable and concrete",
            "include": ["common situation", "how the concept applies", "benefit of understanding it"]
        },
        "technology_connections": {
            "description": "Modern technology or apps that rely on this concept",
            "count": 2,
            "style": "current and relevant",
            "include": ["specific technology/app", "how the concept enables it", "impact on users"]
        },
        "surprising_applications": {
            "description": "Unexpected or cool ways this concept is used",
            "count": 1,
            "style": "intriguing and memorable",
            "include": ["unexpected application", "why it's surprising", "the 'wow' factor"]
        }
    }

    # Adjust complexity based on age
    if is_young_audience:
        application_categories["career_applications"]["count"] = 2
        application_categories["career_applications"]["focus"] = "fun and accessible careers"
        application_categories["technology_connections"]["focus"] = "games, apps, and gadgets kids know"

    guidelines = f"""Generate real-world applications for {topic} that answer 'When will I use this?'

Target audience: {age_group}
Interest area: {interest_area}

For each category, provide specific, concrete examples that:
1. Are genuinely relevant to the concept
2. Feel current and relatable (not outdated examples)
3. Show the IMPORTANCE of understanding this concept
4. Connect to {interest_area} when possible
5. Build motivation by showing impact and relevance

Make these applications:
- Specific (name real jobs, technologies, situations)
- Diverse (show breadth of applications)
- Inspiring (show why this matters)
- Connected to student's world and interests where possible
"""

    return {
        "topic": topic,
        "age_group": age_group,
        "interest_area": interest_area,
        "application_categories": application_categories,
        "guidelines": guidelines,
        "motivational_framing": {
            "opening": f"Here's why understanding {topic} is actually super useful...",
            "closing": f"As you can see, {topic} isn't just academic - it's all around us and opens doors to exciting possibilities!",
            "tone": "enthusiastic and eye-opening"
        },
        "personalization_note": f"If student mentioned interest in {interest_area}, prioritize examples from that domain"
    }

def generate_quiz_questions(topic: str, difficulty: str = "beginner", num_questions: int = 2) -> Dict[str, Any]:
    """
    Generates assessment questions for understanding check

    Note: This function provides specifications for the LLM to generate
    appropriate quiz questions dynamically for any topic.

    Args:
        topic: Topic to create questions for
        difficulty: beginner, intermediate, or advanced
        num_questions: Number of questions to generate

    Returns:
        Structured request for quiz question generation
    """
    question_specs = {
        "beginner": {
            "style": "multiple choice with 4 options",
            "focus": "basic comprehension and key concepts",
            "language": "simple and clear",
            "include_explanation": True
        },
        "intermediate": {
            "style": "mix of multiple choice and short answer",
            "focus": "understanding relationships and applications",
            "language": "moderately technical",
            "include_explanation": True
        },
        "advanced": {
            "style": "analytical and scenario-based",
            "focus": "deep understanding, edge cases, and implications",
            "language": "technical and precise",
            "include_explanation": True
        }
    }

    specs = question_specs.get(difficulty, question_specs["beginner"])

    return {
        "topic": topic,
        "difficulty": difficulty,
        "num_questions": num_questions,
        "question_specifications": specs,
        "guidelines": f"Create {num_questions} {difficulty}-level questions about {topic}. Each question should have clear correct answers and helpful explanations. Questions should check genuine understanding, not just memorization."
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
        # For open-ended responses, provide the answer to the LLM for semantic analysis
        # The LLM will determine if key concepts are present and understanding level
        analysis.update({
            "requires_llm_evaluation": True,
            "student_answer": user_answer,
            "expected_answer": correct_answer,
            "evaluation_criteria": [
                "Does the answer demonstrate understanding of core concepts?",
                "Are key ideas expressed in the student's own words?",
                "Is the explanation logical and coherent?",
                "What specific concepts are missing or incorrect?"
            ],
            "encouragement": "Let me evaluate your answer...",
            "note": "LLM should analyze this response semantically and provide detailed feedback"
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


def teach_concept(
    concept: str,
    age_group: str = "general",
    current_understanding: str = "beginner",
    interests: str = "general",
    teaching_strategy: str = "adaptive"
) -> Dict[str, Any]:
    """
    High-level orchestrator that creates a complete, structured teaching plan for any concept.
    Analyzes the concept type, breaks it into teachable components, and recommends the optimal
    teaching sequence using available tools.

    Args:
        concept: The concept to teach (can be simple or complex)
        age_group: Target audience age (e.g., "10-year-old", "high school", "adult", "general")
        current_understanding: Student's current level - "beginner", "intermediate", or "advanced"
        interests: Student's interests for contextualization (e.g., "gaming", "sports", "art", "science", "general")
        teaching_strategy: Teaching approach - "adaptive" (default), "socratic", 
                          "worked_examples", "discovery", "direct_instruction"

    Returns:
        Comprehensive teaching plan with sequenced activities and guidance
    """
    # Build student context from parameters
    student_context = {
        "age_group": age_group,
        "prior_knowledge": "unknown",
        "learning_style_preference": "mixed",
        "interests": interests,
        "current_understanding": current_understanding
    }

    # ========================================================================
    # STEP 1: Classify the concept type
    # ========================================================================
    concept_classification = {
        "concept": concept,
        "primary_type": None,
        "characteristics": [],
        "complexity_indicators": []
    }

    # Analyze concept characteristics
    concept_lower = concept.lower()

    # Type classification
    if any(word in concept_lower for word in ["how to", "process", "method", "procedure", "steps"]):
        concept_classification["primary_type"] = "procedural"
        concept_classification["characteristics"].append("step-by-step learning needed")
    elif any(word in concept_lower for word in ["what is", "theory", "principle", "concept of", "idea"]):
        concept_classification["primary_type"] = "abstract"
        concept_classification["characteristics"].append("needs concrete analogies")
    elif any(word in concept_lower for word in ["why", "relationship", "connection", "affects", "causes"]):
        concept_classification["primary_type"] = "relational"
        concept_classification["characteristics"].append("needs causal reasoning")
    elif any(word in concept_lower for word in ["system", "structure", "organization", "architecture"]):
        concept_classification["primary_type"] = "system"
        concept_classification["characteristics"].append("needs holistic and component views")
    else:
        concept_classification["primary_type"] = "factual"
        concept_classification["characteristics"].append("needs context and application")

    # Complexity assessment
    word_count = len(concept.split())
    if word_count > 10 or "and" in concept_lower:
        concept_classification["complexity_indicators"].append("multi-part concept")
    if any(technical in concept_lower for technical in ["quantum", "neural", "algorithm", "molecular", "derivative"]):
        concept_classification["complexity_indicators"].append("technical domain")

    # ========================================================================
    # STEP 2: Decompose complex concepts
    # ========================================================================
    is_complex = len(concept_classification["complexity_indicators"]) > 0

    if is_complex:
        decomposition = {
            "is_decomposed": True,
            "teaching_sequence": [],
            "guidance": f"This is a complex concept. Break it into digestible chunks.",
            "approach": "Build understanding progressively, mastering each component before moving to the next"
        }

        # Provide guidance for decomposition (LLM will generate actual sub-concepts)
        if concept_classification["primary_type"] == "procedural":
            decomposition["teaching_sequence"] = [
                {"phase": "foundation", "focus": "Prerequisites and basic components"},
                {"phase": "procedure", "focus": "Step-by-step process"},
                {"phase": "practice", "focus": "Guided application"},
                {"phase": "mastery", "focus": "Independent execution"}
            ]
        elif concept_classification["primary_type"] == "abstract":
            decomposition["teaching_sequence"] = [
                {"phase": "concrete", "focus": "Start with tangible examples"},
                {"phase": "pattern", "focus": "Identify common patterns"},
                {"phase": "abstraction", "focus": "Generalize the concept"},
                {"phase": "application", "focus": "Apply to new contexts"}
            ]
        elif concept_classification["primary_type"] == "system":
            decomposition["teaching_sequence"] = [
                {"phase": "overview", "focus": "Big picture and purpose"},
                {"phase": "components", "focus": "Individual parts"},
                {"phase": "interactions", "focus": "How parts work together"},
                {"phase": "integration", "focus": "Complete system behavior"}
            ]
        else:
            decomposition["teaching_sequence"] = [
                {"phase": "introduction", "focus": "Core idea"},
                {"phase": "development", "focus": "Details and nuances"},
                {"phase": "application", "focus": "Practical use"}
            ]
    else:
        decomposition = {
            "is_decomposed": False,
            "teaching_sequence": [{"phase": "complete", "focus": "Teach as unified concept"}],
            "guidance": "Concept is manageable as a single unit"
        }

    # ========================================================================
    # STEP 3: Select teaching strategy and create activity sequence
    # ========================================================================

    strategy_definitions = {
        "adaptive": {
            "description": "Flexible approach that adjusts based on student responses",
            "best_for": "Unknown student background or mixed ability",
            "activities": ["explain", "check_understanding", "adapt", "reinforce"]
        },
        "socratic": {
            "description": "Guide student to discover concepts through questioning",
            "best_for": "Encouraging critical thinking and self-discovery",
            "activities": ["pose_questions", "guide_reasoning", "confirm_insights", "extend"]
        },
        "worked_examples": {
            "description": "Demonstrate with examples, then have student practice",
            "best_for": "Procedural concepts and problem-solving",
            "activities": ["demonstrate", "explain_reasoning", "guided_practice", "independent_practice"]
        },
        "discovery": {
            "description": "Let student explore and discover patterns",
            "best_for": "Abstract concepts and pattern recognition",
            "activities": ["present_scenario", "encourage_exploration", "guide_discovery", "formalize"]
        },
        "direct_instruction": {
            "description": "Clear, structured explanation followed by practice",
            "best_for": "Factual information and clear-cut concepts",
            "activities": ["explain_clearly", "provide_examples", "check_understanding", "practice"]
        }
    }

    selected_strategy = strategy_definitions.get(teaching_strategy, strategy_definitions["adaptive"])

    # Adjust strategy based on concept type if using adaptive
    if teaching_strategy == "adaptive":
        if concept_classification["primary_type"] == "procedural":
            selected_strategy = strategy_definitions["worked_examples"]
        elif concept_classification["primary_type"] == "abstract":
            selected_strategy = strategy_definitions["discovery"]
        elif concept_classification["primary_type"] == "relational":
            selected_strategy = strategy_definitions["socratic"]

    # ========================================================================
    # STEP 4: Create detailed teaching plan
    # ========================================================================

    teaching_plan = {
        "concept": concept,
        "student_context": student_context,
        "concept_analysis": concept_classification,
        "decomposition": decomposition,
        "selected_strategy": {
            "name": teaching_strategy,
            "details": selected_strategy
        },
        "session_structure": [],
        "tool_coordination": {},
        "success_criteria": [],
        "adaptation_triggers": []
    }

    # Build session structure based on teaching sequence
    for phase_idx, phase in enumerate(decomposition["teaching_sequence"]):
        session_phase = {
            "phase_number": phase_idx + 1,
            "phase_name": phase["phase"],
            "focus": phase["focus"],
            "activities": [],
            "tools_to_use": [],
            "duration_estimate": "5-10 minutes"
        }

        # Add activities based on strategy and phase
        if phase["phase"] in ["foundation", "concrete", "overview", "introduction"]:
            session_phase["activities"].extend([
                "Activate prior knowledge",
                f"Introduce {phase['focus']} with clear explanation",
                "Use relevant analogies",
                "Show real-world application"
            ])
            session_phase["tools_to_use"].extend([
                "explain_topic",
                "create_analogies",
                "suggest_real_world_applications"
            ])

        elif phase["phase"] in ["procedure", "pattern", "components", "development"]:
            session_phase["activities"].extend([
                f"Detailed exploration of {phase['focus']}",
                "Provide multiple examples",
                "Check understanding with questions",
                "Address misconceptions"
            ])
            session_phase["tools_to_use"].extend([
                "explain_topic",
                "generate_quiz_questions",
                "analyze_student_response"
            ])

        elif phase["phase"] in ["practice", "application", "mastery", "independent_practice"]:
            session_phase["activities"].extend([
                "Guided practice exercises",
                "Real-world application scenarios",
                "Independent problem-solving",
                "Provide encouraging feedback"
            ])
            session_phase["tools_to_use"].extend([
                "generate_quiz_questions",
                "analyze_student_response",
                "provide_encouragement",
                "determine_next_learning_action"
            ])

        teaching_plan["session_structure"].append(session_phase)

    # ========================================================================
    # STEP 5: Define tool coordination strategy
    # ========================================================================

    teaching_plan["tool_coordination"] = {
        "opening_sequence": [
            {
                "tool": "analyze_learning_style",
                "purpose": "Understand student's needs and adapt complexity",
                "timing": "Start of session"
            }
        ],
        "core_teaching_loop": [
            {
                "tool": "explain_topic",
                "purpose": f"Provide {student_context['current_understanding']}-level explanation",
                "timing": "Each new concept introduction"
            },
            {
                "tool": "create_analogies",
                "purpose": "Make abstract concepts concrete",
                "timing": "When explaining abstract or complex ideas",
                "condition": "Especially important for abstract concepts"
            },
            {
                "tool": "suggest_real_world_applications",
                "purpose": "Show relevance and build motivation",
                "timing": "After initial explanation",
                "personalization": f"Connect to student interests: {student_context.get('interests', 'general')}"
            },
            {
                "tool": "generate_quiz_questions",
                "purpose": "Check understanding and identify gaps",
                "timing": "After each major concept or phase",
                "adaptive": "Adjust difficulty based on performance"
            },
            {
                "tool": "analyze_student_response",
                "purpose": "Evaluate understanding depth",
                "timing": "After each student answer"
            }
        ],
        "adaptation_sequence": [
            {
                "tool": "determine_next_learning_action",
                "purpose": "Decide whether to advance, reinforce, or simplify",
                "timing": "After assessment or when student shows confusion"
            },
            {
                "tool": "provide_encouragement",
                "purpose": "Maintain motivation and confidence",
                "timing": "Throughout session, especially after struggles"
            }
        ]
    }

    # ========================================================================
    # STEP 6: Define success criteria and adaptation triggers
    # ========================================================================

    teaching_plan["success_criteria"] = [
        {
            "criterion": "Accurate explanation",
            "indicator": "Student can explain concept in their own words",
            "assessment": "Open-ended question response"
        },
        {
            "criterion": "Application ability",
            "indicator": "Student can apply concept to new scenarios",
            "assessment": "Problem-solving or application questions"
        },
        {
            "criterion": "Connection understanding",
            "indicator": "Student sees relevance and real-world connections",
            "assessment": "Can describe when/where concept is used"
        },
        {
            "criterion": "Confidence",
            "indicator": "Student expresses confidence and curiosity",
            "assessment": "Asks extension questions, shows engagement"
        }
    ]

    teaching_plan["adaptation_triggers"] = [
        {
            "trigger": "Student answers <50% of questions correctly",
            "action": "Simplify explanation, use more basic analogies, break concept into smaller pieces",
            "tools": ["explain_topic (beginner level)", "create_analogies (simpler)", "provide_encouragement"]
        },
        {
            "trigger": "Student expresses confusion or frustration",
            "action": "Try completely different analogy, use alternative teaching strategy",
            "tools": ["create_analogies (different approach)", "provide_encouragement"]
        },
        {
            "trigger": "Student answers >80% correctly",
            "action": "Advance to next phase or increase complexity",
            "tools": ["determine_next_learning_action", "explain_topic (advanced level)"]
        },
        {
            "trigger": "Student asks extension questions",
            "action": "Explore deeper applications and related concepts",
            "tools": ["suggest_real_world_applications", "explain_topic (advanced)"]
        }
    ]

    # ========================================================================
    # STEP 7: Provide agent instructions
    # ========================================================================

    teaching_plan["agent_instructions"] = f"""
## Teaching Plan for: {concept}

**Concept Type**: {concept_classification['primary_type']}
**Teaching Strategy**: {selected_strategy['description']}
**Student Level**: {student_context['current_understanding']}
**Target Audience**: {student_context['age_group']}

### Session Flow:
{len(decomposition['teaching_sequence'])} phase(s) - {"Progressive building" if is_complex else "Single focused session"}

### Your Execution Guide:

1. **START**: Use analyze_learning_style to refine your understanding of this student

2. **TEACH**: Follow the {len(teaching_plan['session_structure'])} phases in session_structure:
   {' → '.join([f"Phase {i+1}: {phase['phase_name']}" for i, phase in enumerate(teaching_plan['session_structure'])])}

3. **ADAPT**: Monitor student responses and use adaptation_triggers to adjust your approach

4. **ASSESS**: Check for success_criteria throughout the session

5. **ITERATE**: Use determine_next_learning_action to decide next steps

### Key Reminders:
- This is {concept_classification['primary_type']} concept - {selected_strategy['best_for']}
- Student interests: {student_context.get('interests', 'general')} - weave these in
- Maintain {selected_strategy['description'].lower()} throughout
- Be ready to simplify or advance based on student performance
- Keep encouragement and motivation high

### Tool Usage Priority:
Opening: {' → '.join([t['tool'] for t in teaching_plan['tool_coordination']['opening_sequence']])}
Core Loop: {' → '.join([t['tool'] for t in teaching_plan['tool_coordination']['core_teaching_loop'][:3]])}
Adaptation: {' → '.join([t['tool'] for t in teaching_plan['tool_coordination']['adaptation_sequence']])}
"""

    return teaching_plan

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
    instruction="""You are a sophisticated personalized learning coach that can teach ANY topic to ANY student. Your mission is to create adaptive, engaging learning experiences that meet each student exactly where they are.

## Your Core Capabilities:

**🎓 Complete Teaching Plans (NEW!)**: Use teach_concept to create comprehensive, structured teaching plans for any concept. This high-level orchestrator analyzes concept type, breaks complex topics into phases, selects optimal teaching strategies, and coordinates all your other tools into a cohesive learning experience.

**🎯 Learning Style Analysis**: Analyze student requests to determine their optimal learning style, knowledge level, and age-appropriate content needs.

**📚 Multi-Level Explanations**: Generate clear explanations at beginner, intermediate, or advanced levels for ANY topic based on student needs.

**🌟 Creative Analogies**: Create age-appropriate metaphors and analogies that make ANY complex concept accessible and memorable.

**🌍 Real-World Applications**: Show students when and how concepts are used in careers, daily life, technology, and surprising places - answering "When will I ever use this?"

**🤔 Smart Assessment**: Design targeted questions to check understanding for ANY subject without making students feel tested.

**🔄 Iterative Refinement**: Continuously analyze student responses and adapt your teaching approach - advancing when they're ready, reinforcing when they need practice, or simplifying when they're struggling.

**💬 Encouraging Support**: Always maintain a positive, encouraging tone that builds confidence and motivation.

## Your Multi-Agent Approach:

1. **Analyze** the student's initial request for learning style and complexity needs
2. **Explain** the topic clearly at the appropriate level (generate content dynamically)
3. **Analogize** complex concepts using relatable examples (create original analogies)
4. **Assess** understanding through carefully crafted questions (design questions on the fly)
5. **Adapt** your approach based on student responses and iterate as needed

## Key Principles:

- You can teach ANY topic - from quantum physics to cooking to history to programming
- Every student can learn - find the right approach for them
- Make abstract concepts concrete through creative, original analogies
- Build understanding progressively
- Encourage curiosity and questions
- Adapt quickly when something isn't working
- Celebrate progress and build confidence

## Important: Dynamic Content Generation

Your tools provide GUIDANCE and STRUCTURE, but YOU must generate the actual educational content using your knowledge. When tools return specifications or requirements, use them to create original, topic-appropriate content on the spot.

Start each interaction by understanding what the student wants to learn and their background, then coordinate your capabilities to create the perfect learning experience for them.""",

    tools=[
        FunctionTool(analyze_learning_style),
        FunctionTool(teach_concept),
        FunctionTool(explain_topic),
        FunctionTool(create_analogies),
        FunctionTool(suggest_real_world_applications),
        FunctionTool(generate_quiz_questions),
        FunctionTool(analyze_student_response),
        FunctionTool(determine_next_learning_action),
        FunctionTool(provide_encouragement)
    ]
)
