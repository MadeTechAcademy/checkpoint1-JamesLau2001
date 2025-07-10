import html2text
def write_html(theme, theme_indexes, duties, user_choice):
    html_file_index =["Bootcamp", "Automate!", "Houston, Prepare to Launch", "Going Deeper", "Assemble!", "Call Security"]
    with open(f"html_themes/{theme}_duties.html", "w") as f:
        html_contents = f"""
                <h1> List of {html_file_index[int(user_choice)-2]} Duties: </h1>
                <ol>
        """
        for index in theme_indexes:
            html_contents += f"""
                    <li>{duties[index]}</li>\n"""
        html_contents += """
                </ol>
        """
        f.write(html_contents)
        text_content = html2text.html2text(html_contents)
        print(text_content)