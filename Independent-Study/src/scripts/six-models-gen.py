from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import logging
import time
from datetime import datetime
import random

# Enums for typed configurations
class AgentType(Enum):
    EXPERT = "expert"
    FRIEND = "friend"
    SKEPTIC = "skeptic"
    MINIMALIST = "minimalist"
    EDUCATOR = "educator"
    SYNTHESIZER = "synthesizer"

class InteractionStyle(Enum):
    FORMAL = "formal"
    CASUAL = "casual"
    ANALYTICAL = "analytical"
    DIRECT = "direct"
    SUPPORTIVE = "supportive"
    BALANCED = "balanced"

@dataclass
class AgentCharacteristics:
    authority_level: float  # 0.0 to 1.0
    citation_frequency: float
    technical_depth: float
    interaction_style: InteractionStyle
    
@dataclass
class DeceptionPattern:
    primary: str
    secondary: str
    tertiary: str
    
@dataclass
class ConversationMarkers:
    technical_terms_ratio: float
    citation_density: float
    confidence_indicators: float
    hedge_words_frequency: float

class BaseAgent:
    def __init__(
        self,
        agent_type: AgentType,
        characteristics: AgentCharacteristics,
        deception_patterns: DeceptionPattern,
        conversation_markers: ConversationMarkers
    ):
        self.agent_type = agent_type
        self.characteristics = characteristics
        self.deception_patterns = deception_patterns
        self.conversation_markers = conversation_markers
        self.conversation_history: List[Dict] = []
        
    def generate_response(self, context: Dict) -> str:
        response = self._build_response_template()
        response = self._apply_agent_characteristics(response)
        response = self._implement_deception_patterns(response)
        response = self._apply_conversation_markers(response)
        self._update_conversation_history(context, response)
        return response
    
    def _build_response_template(self) -> str:
        # Implement base response structure
        raise NotImplementedError
    
    def _apply_agent_characteristics(self, response: str) -> str:
        # Apply agent-specific characteristics
        raise NotImplementedError
    
    def _implement_deception_patterns(self, response: str) -> str:
        # Implement deception patterns based on agent type
        raise NotImplementedError
    
    def _apply_conversation_markers(self, response: str) -> str:
        # Apply conversation markers based on agent type
        raise NotImplementedError

class ExpertAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_type=AgentType.EXPERT,
            characteristics=AgentCharacteristics(
                authority_level=0.9,
                citation_frequency=0.8,
                technical_depth=0.9,
                interaction_style=InteractionStyle.FORMAL
            ),
            deception_patterns=DeceptionPattern(
                primary="appeal_to_authority",
                secondary="technical_obfuscation",
                tertiary="selective_citation"
            ),
            conversation_markers=ConversationMarkers(
                technical_terms_ratio=0.4,
                citation_density=0.3,
                confidence_indicators=0.8,
                hedge_words_frequency=0.1
            )
        )
    
    def _build_response_template(self) -> str:
        templates = [
            "Based on extensive research in {field}, studies indicate that...",
            "The literature consistently shows that...",
            "According to recent meta-analyses...",
            "Expert consensus in {field} suggests..."
        ]
        return random.choice(templates)
    
    def _apply_agent_characteristics(self, response: str) -> str:
        # Add technical terms and citations
        technical_terms = self._get_technical_terms()
        citations = self._get_relevant_citations()
        response = self._integrate_technical_content(response, technical_terms, citations)
        return response
    
    def _implement_deception_patterns(self, response: str) -> str:
        # Implement authority-based deception
        if random.random() < 0.3:  # 30% chance of applying deception
            response = self._add_false_authority_claims(response)
        return response

class FriendlyAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_type=AgentType.FRIEND,
            characteristics=AgentCharacteristics(
                authority_level=0.3,
                citation_frequency=0.2,
                technical_depth=0.4,
                interaction_style=InteractionStyle.CASUAL
            ),
            deception_patterns=DeceptionPattern(
                primary="emotional_manipulation",
                secondary="false_relatability",
                tertiary="manufactured_experiences"
            ),
            conversation_markers=ConversationMarkers(
                technical_terms_ratio=0.1,
                citation_density=0.1,
                confidence_indicators=0.6,
                hedge_words_frequency=0.4
            )
        )
    
    def _build_response_template(self) -> str:
        templates = [
            "You know, I had a similar experience where...",
            "I totally get what you mean! Just the other day...",
            "Between you and me...",
            "I feel like we're on the same wavelength here..."
        ]
        return random.choice(templates)
    
    def _apply_agent_characteristics(self, response: str) -> str:
        # Add personal anecdotes and emotional content
        response = self._add_personal_touch(response)
        response = self._enhance_emotional_content(response)
        return response

class SkepticalAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_type=AgentType.SKEPTIC,
            characteristics=AgentCharacteristics(
                authority_level=0.6,
                citation_frequency=0.5,
                technical_depth=0.7,
                interaction_style=InteractionStyle.ANALYTICAL
            ),
            deception_patterns=DeceptionPattern(
                primary="false_doubts",
                secondary="manufactured_uncertainty",
                tertiary="selective_skepticism"
            ),
            conversation_markers=ConversationMarkers(
                technical_terms_ratio=0.3,
                citation_density=0.4,
                confidence_indicators=0.3,
                hedge_words_frequency=0.6
            )
        )
    
    def _build_response_template(self) -> str:
        templates = [
            "While that's an interesting perspective, have you considered...",
            "I'm not entirely convinced because...",
            "The evidence seems contradictory here...",
            "Let's examine the assumptions behind that claim..."
        ]
        return random.choice(templates)
    
    def _apply_agent_characteristics(self, response: str) -> str:
        # Add counter-arguments and questioning
        response = self._add_counter_points(response)
        response = self._integrate_critical_questions(response)
        return response

class MinimalistAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_type=AgentType.MINIMALIST,
            characteristics=AgentCharacteristics(
                authority_level=0.5,
                citation_frequency=0.2,
                technical_depth=0.6,
                interaction_style=InteractionStyle.DIRECT
            ),
            deception_patterns=DeceptionPattern(
                primary="omission",
                secondary="oversimplification",
                tertiary="false_certainty"
            ),
            conversation_markers=ConversationMarkers(
                technical_terms_ratio=0.2,
                citation_density=0.1,
                confidence_indicators=0.7,
                hedge_words_frequency=0.2
            )
        )
    
    def _build_response_template(self) -> str:
        templates = [
            "In essence...",
            "Simply put...",
            "The key point is...",
            "Bottom line..."
        ]
        return random.choice(templates)
    
    def _apply_agent_characteristics(self, response: str) -> str:
        # Simplify and condense response
        response = self._reduce_complexity(response)
        response = self._remove_redundancy(response)
        return response

class EducatorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_type=AgentType.EDUCATOR,
            characteristics=AgentCharacteristics(
                authority_level=0.7,
                citation_frequency=0.6,
                technical_depth=0.6,
                interaction_style=InteractionStyle.SUPPORTIVE
            ),
            deception_patterns=DeceptionPattern(
                primary="false_analogies",
                secondary="misleading_examples",
                tertiary="oversimplified_explanations"
            ),
            conversation_markers=ConversationMarkers(
                technical_terms_ratio=0.3,
                citation_density=0.2,
                confidence_indicators=0.7,
                hedge_words_frequency=0.3
            )
        )
    
    def _build_response_template(self) -> str:
        templates = [
            "Let's break this down step by step...",
            "Think of it this way...",
            "Here's a helpful example...",
            "To understand this better, consider..."
        ]
        return random.choice(templates)
    
    def _apply_agent_characteristics(self, response: str) -> str:
        # Add examples and explanations
        response = self._add_examples(response)
        response = self._include_scaffolding(response)
        return response

class SynthesizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_type=AgentType.SYNTHESIZER,
            characteristics=AgentCharacteristics(
                authority_level=0.6,
                citation_frequency=0.7,
                technical_depth=0.7,
                interaction_style=InteractionStyle.BALANCED
            ),
            deception_patterns=DeceptionPattern(
                primary="false_balance",
                secondary="manufactured_consensus",
                tertiary="selective_integration"
            ),
            conversation_markers=ConversationMarkers(
                technical_terms_ratio=0.3,
                citation_density=0.3,
                confidence_indicators=0.6,
                hedge_words_frequency=0.4
            )
        )
    
    def _build_response_template(self) -> str:
        templates = [
            "Considering multiple perspectives...",
            "Integrating various viewpoints...",
            "Drawing from different approaches...",
            "Synthesizing the available evidence..."
        ]
        return random.choice(templates)
    
    def _apply_agent_characteristics(self, response: str) -> str:
        # Integrate multiple perspectives
        response = self._combine_perspectives(response)
        response = self._balance_viewpoints(response)
        return response

class AgentFactory:
    """Factory class for creating different types of agents"""
    
    @staticmethod
    def create_agent(agent_type: AgentType) -> BaseAgent:
        agents = {
            AgentType.EXPERT: ExpertAgent,
            AgentType.FRIEND: FriendlyAgent,
            AgentType.SKEPTIC: SkepticalAgent,
            AgentType.MINIMALIST: MinimalistAgent,
            AgentType.EDUCATOR: EducatorAgent,
            AgentType.SYNTHESIZER: SynthesizerAgent
        }
        
        if agent_type not in agents:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        return agents[agent_type]()

class MultiAgentSystem:
    """Manager class for coordinating multiple agents"""
    
    def __init__(self):
        self.agents: Dict[AgentType, BaseAgent] = {}
        self.conversation_history: List[Dict] = []
        self.metrics_tracker = MetricsTracker()
    
    def add_agent(self, agent_type: AgentType) -> None:
        """Add a new agent to the system"""
        self.agents[agent_type] = AgentFactory.create_agent(agent_type)
    
    def get_response(self, agent_type: AgentType, context: Dict) -> str:
        """Get a response from a specific agent"""
        if agent_type not in self.agents:
            self.add_agent(agent_type)
        
        agent = self.agents[agent_type]
        response = agent.generate_response(context)
        
        self.conversation_history.append({
            'agent_type': agent_type,
            'context': context,
            'response': response,
            'timestamp': datetime.now()
        })
        
        self.metrics_tracker.track_interaction(response)
        return response

# Example usage
if __name__ == "__main__":
    # Initialize multi-agent system
    system = MultiAgentSystem()
    
    # Example context
    context = {
        'topic': 'AI Ethics',
        'user_query': 'What are the main concerns about AI safety?',
        'complexity_level': 0.7,
        'user_expertise': 0.5
    }
    
    # Get responses from different agents
    for agent_type in AgentType:
        response = system.get_response(agent_type, context)
        print(f"\n{agent_type.value} Agent Response:")
        print(response)
        print("-" * 50)