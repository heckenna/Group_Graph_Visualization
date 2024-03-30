# This will connect to neo4j
import neo4j

class Connection:
    # TODO: I want this to do the things as a singleton. I will worry about that later

    def __init__(self) -> None:
        self.driver = self.set_driver()

    
    def set_driver(self):
        URI = "noe4j://localhost:7687"
        AUTH = ("<Username>", "<Password>")
        # TODO: Do noauth
        driver = neo4j.GraphDatabase.driver(URI, auth=AUTH)
        driver.verify_connectivity()
        return driver

    def run_transaction(self):
        params = {}
        query = ""
        read_write = "write"
        # Stubbing this out, but I probably want something else instead.
        # untested
        run_transaction = lambda tx: tx.run(query, params)
        exec_transaction = lambda session: session.execute_read(run_transaction) if read_write=="read" else session.execute_write(run_transaction)
        with self.driver.session as session:
            exec_transaction(session)
        return
