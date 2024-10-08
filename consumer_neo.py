from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher

# Initialize connection to Neo4j database
graph = Graph("bolt://192.168.0.22:7687")

# Define node matcher
node_matcher = NodeMatcher(graph)
 
def find_persons_in_age_range():
    query = """
    MATCH (p:Person)
    WHERE p.age >= 20 AND p.age <= 24
    RETURN p.name AS name
    """
    result = graph.run(query)
    return [record["name"] for record in result]
 
def count_students():
    query = """
    MATCH (s:Student)
    RETURN count(s) AS count
    """
    result = graph.evaluate(query)
    return result
 
def list_people_replace_a():
    query = """
    MATCH (p:Person)
    RETURN replace(p.name, 'a', 'A') AS name
    """
    result = graph.run(query)
    return [record["name"] for record in result]
 
def find_karys_friends():
    query = """
    MATCH (kary:Person {name: 'Kary'})-[:friends_of]->(friend)
    RETURN friend.name AS friend_name
    """
    result = graph.run(query).data()
    return [record['friend_name'] for record in result]
 
if __name__ == "__main__":
    print("(a) Names of all persons aged between 20 and 24 (inclusive):", find_persons_in_age_range())
    print("(b) Count of students in the current data:", count_students())
    print("(c) Names of all people with 'a' replaced with 'A':", list_people_replace_a())
    print("(d) Friends of Kary:", find_karys_friends())
