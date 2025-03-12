from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from app.rag.document_store import Document, document_store


class PolicyInfo(BaseModel):
    """Insurance policy information extracted from documents."""

    policy_number: Optional[str] = None
    policy_type: Optional[str] = None
    coverage_limits: Optional[Dict[str, Any]] = None
    deductibles: Optional[Dict[str, Any]] = None
    exclusions: List[str] = []


class InsuranceRAGService:
    """Insurance-specific RAG service."""

    async def query(self, user_query: str, max_docs: int = 3) -> dict:
        """Process an insurance-related query through the RAG pipeline."""
        # Get documents from the store
        retrieved_docs = document_store.search(user_query, k=max_docs)

        if not retrieved_docs:
            return {
                "query": user_query,
                "response": "No insurance policy documents are available. Please upload policy documents first.",
                "context": "",
                "sources": [],
            }

        # Simple simulated response for insurance domain
        context = "\n".join([doc.content[:100] + "..." for doc in retrieved_docs])
        sources = [
            doc.metadata.get("source", "Unknown Policy") for doc in retrieved_docs
        ]

        # Extract policy information if available
        policy_info = self._extract_policy_info(retrieved_docs)

        # Generate a domain-specific response
        response = self._generate_insurance_response(
            user_query, retrieved_docs, policy_info
        )

        return {
            "query": user_query,
            "response": response,
            "context": context,
            "sources": sources,
            "policy_info": policy_info.dict() if policy_info else None,
        }

    def _extract_policy_info(self, documents: List[Document]) -> Optional[PolicyInfo]:
        """Extract insurance policy information from documents."""
        if not documents:
            return None

        # Mock policy info extraction - in real app this would be more sophisticated
        policy_doc = documents[0]
        policy_number = None
        policy_type = None

        content = policy_doc.content.lower()

        # Very simple extraction logic - would be more advanced in production
        if "policy number" in content or "policy #" in content:
            policy_number = "POL-" + "".join(
                [c for c in policy_doc.metadata.get("source", "")[-6:] if c.isalnum()]
            )

        if "home" in content or "homeowner" in content:
            policy_type = "Homeowner's Insurance"
        elif "auto" in content or "vehicle" in content or "car" in content:
            policy_type = "Auto Insurance"
        elif "life" in content:
            policy_type = "Life Insurance"
        elif "health" in content:
            policy_type = "Health Insurance"
        elif "business" in content or "commercial" in content:
            policy_type = "Commercial Insurance"
        else:
            policy_type = "General Insurance Policy"

        return PolicyInfo(
            policy_number=policy_number,
            policy_type=policy_type,
            coverage_limits={"general": "$100,000"},  # Mock data
            deductibles={"standard": "$500"},  # Mock data
            exclusions=["Intentional damage", "Normal wear and tear"],  # Mock data
        )

    def _generate_insurance_response(
        self, query: str, docs: List[Document], policy_info: Optional[PolicyInfo]
    ) -> str:
        """Generate an insurance-domain specific response."""
        query_lower = query.lower()

        # Check for common insurance queries and provide tailored responses
        if "deductible" in query_lower:
            return f"Based on the policy information, the standard deductible is ${policy_info.deductibles.get('standard', 'unknown') if policy_info else 'unknown'}. For specific claims, deductibles may vary."

        elif "coverage" in query_lower or "cover" in query_lower:
            return f"The {policy_info.policy_type if policy_info else 'insurance policy'} provides coverage with general limits of {policy_info.coverage_limits.get('general', 'unknown') if policy_info else 'unknown'}. Please refer to the specific sections for detailed coverage information."

        elif "exclusion" in query_lower or "exclude" in query_lower:
            if policy_info and policy_info.exclusions:
                exclusion_list = ", ".join(policy_info.exclusions)
                return f"The policy contains several exclusions, including: {exclusion_list}. Please review the full policy for all exclusions."
            else:
                return "Every policy contains exclusions. For specific details, please review the Exclusions section of your policy."

        elif "claim" in query_lower:
            return "To file a claim, you should: 1) Document the incident with photos and notes, 2) Contact your agent or company's claims department, 3) Fill out the provided claim forms, 4) Provide any requested supporting documentation."

        # Generic response
        return f"Based on the {policy_info.policy_type if policy_info else 'insurance'} policy information, I've found some relevant details that may answer your question about '{query}'."

    async def add_documents(self, documents: List[Document]) -> int:
        """Add insurance policy documents to the document store."""
        # Pre-process documents to identify insurance-specific metadata
        for doc in documents:
            # Extract policy type if possible
            content = doc.content.lower()
            if "homeowner" in content or "home insurance" in content:
                doc.metadata["policy_type"] = "homeowners"
            elif "auto" in content or "car insurance" in content:
                doc.metadata["policy_type"] = "auto"
            elif "life insurance" in content:
                doc.metadata["policy_type"] = "life"
            elif "health insurance" in content:
                doc.metadata["policy_type"] = "health"
            else:
                doc.metadata["policy_type"] = "general"

        # Add to document store
        document_store.add_documents(documents)
        return len(documents)


# Create a global insurance RAG service instance
insurance_service = InsuranceRAGService()
