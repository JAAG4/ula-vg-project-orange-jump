from gale.state_machine import BaseState, StateMachine


class BaseEntityState(BaseState):
    def __init__(self, entity, state_machine: StateMachine) -> None:
        super().__init__(state_machine)
        self.entity = entity
