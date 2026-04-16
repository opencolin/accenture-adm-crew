import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import TavilySearchTool, ScrapeWebsiteTool

from accenture_adm_hierarchical_delivery_crew.tools.ask_human import AskHumanTool

search_tool = TavilySearchTool()
scrape_tool = ScrapeWebsiteTool()
ask_human_tool = AskHumanTool()

NEBIUS_BASE_URL = "https://api.tokenfactory.nebius.com/v1"
NEBIUS_API_KEY = os.environ.get("NEBIUS_API_KEY", "")

default_llm = LLM(
    model="openai/deepseek-ai/DeepSeek-V3.2",
    base_url=NEBIUS_BASE_URL,
    api_key=NEBIUS_API_KEY,
)

# Tools for agents that interact with the client
client_facing_tools = [search_tool, scrape_tool, ask_human_tool]
# Tools for agents that do internal/technical work
internal_tools = [search_tool, scrape_tool]


@CrewBase
class AccentureAdmHierarchicalDeliveryCrew:
    """AccentureAdmHierarchicalDeliveryCrew crew"""

    def _create_manager(self) -> Agent:
        """Creates the manager agent for hierarchical orchestration."""
        return Agent(
            config=self.agents_config["managing_director_at_accenture"],
            tools=[],
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def associate_director_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["associate_director_at_accenture"],
            tools=client_facing_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def senior_delivery_lead_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_delivery_lead_at_accenture"],
            tools=client_facing_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def engagement_manager_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["engagement_manager_at_accenture"],
            tools=client_facing_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def program_management_lead_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["program_management_lead_at_accenture"],
            tools=internal_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def management_consultant_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["management_consultant_at_accenture"],
            tools=client_facing_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def strategy_consulting_analyst_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["strategy_consulting_analyst_at_accenture"],
            tools=client_facing_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def solution_architect_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["solution_architect_at_accenture"],
            tools=internal_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def technology_architect_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["technology_architect_at_accenture"],
            tools=internal_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def technology_delivery_lead_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["technology_delivery_lead_at_accenture"],
            tools=internal_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @agent
    def digital_project_manager_at_accenture(self) -> Agent:
        return Agent(
            config=self.agents_config["digital_project_manager_at_accenture"],
            tools=internal_tools,
            allow_delegation=True,
            llm=default_llm,
        )

    @task
    def engagement_strategy_delivery_planning(self) -> Task:
        return Task(
            config=self.tasks_config["engagement_strategy_delivery_planning"],
        )

    @task
    def strategic_engagement_approval(self) -> Task:
        return Task(
            config=self.tasks_config["strategic_engagement_approval"],
        )

    @task
    def business_requirements_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["business_requirements_analysis"],
        )

    @task
    def backlog_definition_scope_planning(self) -> Task:
        return Task(
            config=self.tasks_config["backlog_definition_scope_planning"],
        )

    @task
    def solution_architecture_design(self) -> Task:
        return Task(
            config=self.tasks_config["solution_architecture_design"],
        )

    @task
    def technical_architecture_review(self) -> Task:
        return Task(
            config=self.tasks_config["technical_architecture_review"],
        )

    @task
    def solution_development_implementation(self) -> Task:
        return Task(
            config=self.tasks_config["solution_development_implementation"],
        )

    @task
    def sprint_execution_project_tracking(self) -> Task:
        return Task(
            config=self.tasks_config["sprint_execution_project_tracking"],
        )

    @task
    def integrated_testing_solution_validation(self) -> Task:
        return Task(
            config=self.tasks_config["integrated_testing_solution_validation"],
        )

    @task
    def user_acceptance_testing_coordination(self) -> Task:
        return Task(
            config=self.tasks_config["user_acceptance_testing_coordination"],
        )

    @task
    def production_deployment_cutover(self) -> Task:
        return Task(
            config=self.tasks_config["production_deployment_cutover"],
        )

    @task
    def service_introduction_engagement_closure(self) -> Task:
        return Task(
            config=self.tasks_config["service_introduction_engagement_closure"],
            output_file="output/engagement_closure_report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AccentureAdmHierarchicalDeliveryCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=self._create_manager(),
            stream=True,
        )
