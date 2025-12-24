
from app.agents.architect import ArchitectAgent
from app.agents.backend import BackendAgent
from app.agents.reviewer import ReviewerAgent
from app.agents.security import SecurityAgent
from app.agents.cloud_engineer import CloudEngineerAgent
from app.agents.fullstack import FullStackAgent
from app.agents.graphics import GraphicsAgent
from app.agents.powerbi import PowerBIAgent
from app.agents.generative_ai import GenerativeAIAgent
from app.agents.tests import TestsAgent
from app.agents.devops import DevOpsAgent
from app.agents.datascience import DataScienceAgent
from app.agents.uxui import UXUIAgent
from app.agents.xai import XAIAgent
from app.agents.redteam import RedTeamAgent
from app.agents.blockchain import BlockchainAgent
from app.agents.iot import IoTAgent
from app.agents.robotics import RoboticsAgent
from app.agents.rpa import RPAAgent
from app.agents.voice import VoiceAgent
from app.agents.analytics import AnalyticsAgent
from app.agents.greenit import GreenITAgent
from app.agents.legaltech import LegalTechAgent

class Orchestrator:
    def __init__(self):
        self.pipeline = [
            ArchitectAgent(),
            BackendAgent(),
            CloudEngineerAgent(),
            FullStackAgent(),
            GraphicsAgent(),
            PowerBIAgent(),
            GenerativeAIAgent(),
            DataScienceAgent(),
            DevOpsAgent(),
            TestsAgent(),
            UXUIAgent(),
            XAIAgent(),
            RedTeamAgent(),
            BlockchainAgent(),
            IoTAgent(),
            RoboticsAgent(),
            RPAAgent(),
            VoiceAgent(),
            AnalyticsAgent(),
            GreenITAgent(),
            LegalTechAgent(),
            ReviewerAgent(),
            SecurityAgent(),
        ]

    def execute(self, requirement: str) -> dict:
        output = requirement
        history = []

        for agent in self.pipeline:
            output = agent.run(output)
            history.append({
                "agent": agent.name,
                "output": output
            })

        return {
            "final_output": output,
            "trace": history
        }


# ----------------- GOD MODE -----------------
from app.sovereign.authority import Authority
from app.sovereign.conscience import Conscience
from app.sovereign.limits import Limits
from app.sovereign.memory_of_truth import MemoryOfTruth
from app.sovereign.shutdown import ShutdownProtocol
from app.meta.planner import MetaPlanner
from app.meta.evaluator import MetaEvaluator
from app.meta.refiner import MetaRefiner

class GodModeOrchestrator:
    def __init__(self, root_key: str):
        self.authority = Authority(root_key)
        self.conscience = Conscience()
        self.limits = Limits()
        self.memory = MemoryOfTruth()
        self.shutdown = ShutdownProtocol()

        self.planner = MetaPlanner()
        self.evaluator = MetaEvaluator()
        self.refiner = MetaRefiner()

    def execute(self, intent: str) -> dict:
        if not self.authority.is_authorized():
            return {"error": "UNAUTHORIZED"}

        if not self.conscience.allow_execution(intent):
            return self.shutdown.execute()

        pipeline = self.planner.plan(intent)
        output = intent
        iterations = 0

        for _ in range(self.limits.MAX_ITERATIONS):
            output = self.refiner.improve(output)
            score = self.evaluator.score(output)
            iterations += 1

            if score >= 9:
                self.memory.store(output, score)
                break

        if not self.limits.validate(cost=iterations * 100, iterations=iterations):
            return self.shutdown.execute()

        return {
            "output": output,
            "score": score,
            "iterations": iterations,
            "pipeline": pipeline,
            "memory_truth": self.memory.recall()
        }
