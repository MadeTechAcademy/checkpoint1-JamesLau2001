from utility_functions.write_html import write_html
import html2text
duties = [
    "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
    "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
    "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.",
    "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
    "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts",
    "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
    "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).",
    "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
    "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
    "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
    "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.",
    "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience.",
]
def display_duties(user_choice):
    if user_choice == "1":
        with open("html_themes/all_duties.html", "w") as f:
            html_contents = """
                    <h1> List of All Duties: </h1>
                    <ol>
            """
            for duty in duties:
                html_contents += f"""
                        <li>{duty}</li>\n"""
            html_contents += """
                    </ol>
            """
            f.write(html_contents)
            text_content = html2text.html2text(html_contents)
            print(text_content)
    
    elif user_choice == "2":
        bootcamp_indexes = [0,1,2,3,12]
        write_html("bootcamp", bootcamp_indexes, duties, user_choice)

    elif user_choice == "3":
        automate_indexes = [4,6,9]
        write_html("automate", automate_indexes, duties, user_choice)

    elif user_choice == "4":
        houston_indexes = [5,6,9,11]
        write_html("houston", houston_indexes, duties, user_choice)

    elif user_choice == "5":
        going_deeper_indexes = [10]
        write_html("going_deeper", going_deeper_indexes, duties, user_choice)

    elif user_choice == "6":
        assemble_indexes = [7]
        write_html("assemble", assemble_indexes, duties, user_choice)

    elif user_choice == "7":
        call_security_indexes = [8]
        write_html("call_security", call_security_indexes, duties, user_choice)
        

if __name__=="__main__":
    user_choice = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Press (2) to list the Bootcamp duties\n
    Press (3) to list the Automate! duties\n
    Press (4) to list the Houston, Prepare to Launch duties\n
    Press (5) to list the Going Deeper duties\n
    Press (6) to list the Assemble! duties\n
    Press (7) to list the Call Security duties\n
    Enter your choice:
    """)
    display_duties(user_choice)