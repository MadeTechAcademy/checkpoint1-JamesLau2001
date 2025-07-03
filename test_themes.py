from themes import duties
def test_amount_of_duties_is_correct():
    assert len(duties) == 13

def test_all_duties_in_html():
    with open("html_themes/themes.html", "r") as all_themes:
        content = all_themes.read()

        assert "<title>Display Duties</title>" in content
        assert "<h1> List of All Duties: </h1>" in content
        assert "<li>Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.</li>" in content
        assert "<li>Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.</li>" in content
        assert "<li>Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.</li>" in content
        assert "<li>Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.</li>" in content
        assert "<li>Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts</li>" in content
        assert "<li>Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.</li>" in content
        assert "<li>Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).</li>" in content
        assert "<li>Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.</li>" in content
        assert "<li>Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).</li>" in content
        assert "<li>Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.</li>" in content
        assert "<li>Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.</li>" in content
        assert "<li>Duty 12 Look to automate any manual tasks that are repeated, often using APIs.</li>" in content
        assert "<li>Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience.</li>" in content

def test_correct_duties_for_bootcamp_theme():
    with open("html_themes/bootcamp_themes.html", "r") as bootcamp_themes:
        content = bootcamp_themes.read()

        assert "<title>Display Duties</title>" in content
        assert "<h1> List of Bootcamp Duties: </h1>" in content
        assert "<li>Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.</li>" in content
        assert "<li>Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.</li>" in content
        assert "<li>Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.</li>" in content
        assert "<li>Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.</li>" in content
        assert "<li>Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience.</li>" in content
