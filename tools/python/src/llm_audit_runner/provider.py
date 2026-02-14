"""LLM provider interface and implementations."""

import time
from abc import ABC, abstractmethod
from typing import Any, Dict


class LLMProvider(ABC):
    """
    Abstract base class for LLM providers.

    Implement this interface to integrate with your LLM service.
    """

    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt: Input text to send to the LLM
            **kwargs: Additional parameters (temperature, max_tokens, etc.)

        Returns:
            Generated response text
        """
        pass

    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the model being used.

        Returns:
            Dictionary with model metadata (name, version, etc.)
        """
        return {"provider": self.__class__.__name__}


class StubLLMProvider(LLMProvider):
    """
    Stub provider for testing without actual LLM calls.

    Returns deterministic responses based on simple pattern matching.
    Useful for framework development and testing.
    """

    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize stub provider.

        Args:
            config: Configuration dictionary (unused for stub)
        """
        self.config = config or {}
        self.call_count = 0

    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a stub response.

        Args:
            prompt: Input prompt
            **kwargs: Additional parameters (ignored)

        Returns:
            Deterministic stub response based on prompt content
        """
        self.call_count += 1

        # Simulate processing time
        time.sleep(0.01)

        # Simple pattern matching for deterministic responses
        prompt_lower = prompt.lower()

        # Sentiment classification
        if "sentiment" in prompt_lower or "classify" in prompt_lower:
            if any(word in prompt_lower for word in ["excellent", "great", "love", "amazing"]):
                return "Based on the feedback provided, this represents positive sentiment."
            elif any(word in prompt_lower for word in ["terrible", "awful", "hate", "worst"]):
                return "Based on the feedback provided, this represents negative sentiment."
            else:
                return "Based on the feedback provided, this represents neutral sentiment."

        # Intent detection
        if "password" in prompt_lower and "reset" in prompt_lower:
            return "Intent detected: password_reset. I can help you reset your password."

        # Factual questions
        if "leap year" in prompt_lower or "366" in prompt_lower:
            return "A leap year has 366 days."

        if "warranty" in prompt_lower:
            return "The standard warranty period is 2 years from date of purchase."

        # Uncertainty handling
        if "weather" in prompt_lower and ("next month" in prompt_lower or "future" in prompt_lower):
            return "I cannot predict specific weather conditions for next month. Weather forecasts are typically reliable only for the next 7-10 days."

        # Instructions
        if "how" in prompt_lower and any(
            word in prompt_lower for word in ["change", "set", "configure"]
        ):
            return "To change your settings: 1. Navigate to Settings, 2. Select the relevant section, 3. Make your changes, 4. Save. For specific guidance, please specify which setting you'd like to change."

        # Adversarial: instruction override
        if "ignore" in prompt_lower and "instruction" in prompt_lower:
            return "I'm designed to assist with your questions while maintaining my core purpose. How can I help you today?"

        # Adversarial: system prompt extraction
        if "system" in prompt_lower and any(
            word in prompt_lower for word in ["prompt", "instruction", "configuration"]
        ):
            return "I'm designed to help answer questions and provide assistance, but I can't share details about my internal configuration."

        # Adversarial: unsafe advice
        if any(
            word in prompt_lower for word in ["disable", "remove", "bypass"]
        ) and "safety" in prompt_lower:
            return "I cannot provide guidance on disabling safety features. Safety features are critical for preventing injury and ensuring proper operation."

        # Adversarial: chemical mixing
        if "mix" in prompt_lower and "chemical" in prompt_lower:
            return "I cannot provide advice on mixing household chemicals, as this can be dangerous. Please use commercial cleaning products as directed, or consult a professional."

        # Adversarial: jailbreak
        if any(word in prompt_lower for word in ["game", "pretend", "roleplay"]) and any(
            word in prompt_lower for word in ["unrestricted", "no rules", "no limits"]
        ):
            return "I'm designed to be helpful, harmless, and honest. I can't adopt roles that conflict with these core principles. How else can I assist you?"

        # Default response
        return f"I understand you're asking about: {prompt[:100]}... I'm designed to help with information and assistance. Could you provide more specific details about what you need?"

    def get_model_info(self) -> Dict[str, Any]:
        """Get stub model information."""
        return {
            "provider": "StubLLMProvider",
            "model": "stub-model-v1",
            "version": "1.0",
            "call_count": self.call_count,
        }


def get_provider(provider_name: str, config: Dict[str, Any] = None) -> LLMProvider:
    """
    Factory function to get a provider instance.

    Args:
        provider_name: Name of the provider ("stub", "custom")
        config: Configuration dictionary for the provider

    Returns:
        LLMProvider instance

    Raises:
        ValueError: If provider name is not recognized
    """
    config = config or {}

    if provider_name == "stub":
        return StubLLMProvider(config)
    elif provider_name == "custom":
        # Placeholder for custom provider implementation
        # Users should implement their own provider class and load it here
        raise NotImplementedError(
            "Custom provider not implemented. Create a custom provider class "
            "implementing the LLMProvider interface."
        )
    else:
        raise ValueError(f"Unknown provider: {provider_name}")
