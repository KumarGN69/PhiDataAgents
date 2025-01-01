from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from custom_rag import main

from custom_configs import SEARCH_STRING, WEBSITE, PROMPT, RETRIEVED_RESPONSE

def test_answer_relevancy():
        answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
        test_case = LLMTestCase(
            input= SEARCH_STRING,
            # Replace this with the actual output of your LLM application
            actual_output=main().response,
            retrieval_context= [RETRIEVED_RESPONSE]
        )
        assert_test(test_case, [answer_relevancy_metric])
