app_name = "erpnext_social_media_marketing"
app_title = "Social Media Marketing"
app_publisher = "b»robotized group"
app_description = "CRM-integrated Social Media tracking for ERPNext"
app_email = "erp-devs@b-robotized.com"
app_license = "MIT"

after_install = "erpnext_social_media_marketing.install.after_install"

doc_events = {
    "Social Media Interaction": {
        "after_insert": "erpnext_social_media_marketing.doctype.social_media_interaction.social_media_interaction.create_timeline_entry"
    }
}

fixtures = [
    {"dt": "Workspace", "filters": [["title", "=", "Social Media"]]},
]
