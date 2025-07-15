from themes import duties, display_duties
def test_amount_of_duties_is_correct():
    assert len(duties) == 13

def test_all_duties_in_html(capsys):
    display_duties("1")
    captured = capsys.readouterr()
    assert "List of All Duties:" in captured.out
    assert "1. Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage." in captured.out
    assert "2. Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members." in captured.out
    assert "3. Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review." in captured.out
    assert "4. Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture." in captured.out
    assert "5. Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts" in captured.out
    assert "6. Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely." in captured.out
    assert "7. Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)." in captured.out
    assert "8. Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance." in captured.out
    assert "9. Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC)." in captured.out
    assert "10. Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable." in captured.out
    assert "11. Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications." in captured.out
    assert "12. Duty 12 Look to automate any manual tasks that are repeated, often using APIs." in captured.out
    assert "13. Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience." in captured.out

def test_correct_duties_for_bootcamp_theme(capsys):
    display_duties("2")
    captured = capsys.readouterr()
    assert "List of Bootcamp Duties:" in captured.out
    assert "1. Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage." in captured.out
    assert "2. Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members." in captured.out
    assert "3. Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review." in captured.out
    assert "4. Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture." in captured.out
    assert "5. Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience." in captured.out

def test_correct_duties_for_automate_theme(capsys):
    display_duties("3")
    captured = capsys.readouterr()
    assert "List of Automate! Duties:" in captured.out
    assert "1. Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts" in captured.out
    assert "2. Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)." in captured.out
    assert "3. Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable." in captured.out

def test_correct_duties_for_houston_prepare_to_launch_theme(capsys):
    display_duties("4")
    captured = capsys.readouterr()
    assert "List of Houston, Prepare to Launch Duties:" in captured.out
    assert "1. Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely." in captured.out
    assert "2. Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)." in captured.out
    assert "3. Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable." in captured.out
    assert "4. Duty 12 Look to automate any manual tasks that are repeated, often using APIs." in captured.out

def test_correct_duties_for_going_deeper_theme(capsys):
    display_duties("5")
    captured = capsys.readouterr()
    assert "List of Going Deeper Duties:" in captured.out
    assert "1. Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications." in captured.out

def test_correct_duties_for_assemble_theme(capsys):
    display_duties("6")
    captured = capsys.readouterr()
    assert "List of Assemble! Duties:" in captured.out
    assert "1. Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance." in captured.out

def test_correct_duties_for_call_security_theme(capsys):
    display_duties("7")
    captured = capsys.readouterr()
    assert "List of Call Security Duties:" in captured.out
    assert "1. Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC)." in captured.out
