from agents.specialists.test_planner_agent.agent import planner_agent
from agents.specialists.scenario_generator_agent.agent import scenario_agent
from agents.specialists.risk_analysis_agent.agent import risk_agent
from agents.specialists.execution_agent.agent import execution_agent
from agents.specialists.reporting_agent.agent import reporting_agent


class SupplyChainCrew:

    def __init__(self):

        self.planner = planner_agent
        self.scenario = scenario_agent
        self.risk = risk_agent
        self.execution = execution_agent
        self.reporting = reporting_agent