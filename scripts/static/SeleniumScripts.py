SeleniumScripts = {
    "start_conv": "return arguments[0].shadowRoot.querySelector('.apply-chat-prompt').click()",
    "read_last_message": "var eleme = arguments[0].shadowRoot.querySelectorAll('.ae8f46'); return eleme[eleme.length-1];",
    "list_all_messages": "return arguments[0].shadowRoot.querySelector('me-messages__inner')",
    "open_text_area": "return arguments[0].shadowRoot.querySelector('textarea')",
    "jobs_script": "var eleme = arguments[0].shadowRoot.querySelectorAll('.job-item__title'); return Array.from(eleme).map(x => x.innerHTML);",
}
