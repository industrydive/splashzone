prompts = [
    {
        'title': 'Add a "What we are reading" section to News Posts section (back-end)',
        'description': '''
            In order to boost our editorial reputation, as a Dive Site Editor,
            I want to be able to add links to relevant sources which would appear at the end of newsposts.
            Editors should be able to add up to 3 "What we are reading" (WWAR) links per News Post. Some
            WWAR links will likely be used by more than one News Post.
        ''',
        'AC': [
            'A new model and subsequent migration exist in the news app which will store WWAR links',
            'Model properties match the fields described in the scenarios',
            'Admin form matches the interactions described in the scenarios',
            'Limit News Posts to 3 WWAR links',
            'Any given WWAR link should be able to be associated with any News Post for the dive site it is on'
        ],
        'objectives': [
            'Understand how to create new models in Django',
            'Understand how to manage multiple models from one admin page in Django',
            'Understand many-to-many relationships in the Django ORM'
        ],
        'scenarios': [
            {
                'title': 'A WWAR model and admin pages exist under the news app',
                'steps': [
                    'Given I am a Dive Site Editor and I am signed in to the divesite admin',
                    'When I am on the admin home page',
                    'Then a link to "What We Are Reading" is listed under "NEWS"',
                ]
            },
            {
                'title': 'An admin user can add/edit/delete a WWAR link using standard admin pages',
                'steps': [
                    'Given I am a Dive Site Editor and I on the "What We Are Reading" admin list page',
                    'When I click "ADD WHAT WE ARE READING +"',
                    'Then I see a form with the fields',
                    'label: "title", type: text input',
                    'label: "link", type: url input',
                    'label: "source", type: text input',
                    'label: "published", type: date input, help text: "the date that the linked article was originally published"',  # noqa
                ]
            },
            {
                'title': 'An inline form is added to the News Post edit page in the admin',
                'steps': [
                    'Given I am a Dive Site Editor and I am signed in to the divesite admin',
                    'When I go to a newspost detail edit page',
                    'And I scroll to the bottom of the form',
                    'Then I see a "What we are reading" inline form',
                    'And I can select existing WWAR links to add to this News Post',
                    'And I can remove WWAR links from this News Post',
                ]
            }
        ]
    },
    {
        'title': 'Add a "What we are reading" section to News Posts section (front-end)',
        'description': '''
            In order to get more information about topics covered on a given Dive Site story, as a reader,
            I want a list with links to related coverage from other sources.
        ''',
        'AC': [
            'A new feed section is added to the newspost template which contains the WWAR links associated with a given News Post',  # noqa
            'The title of the section should be "What we\'re reading"',
            'The sub-title of the section should be "Sources from other publications"',
            'The title of each feed item should be the title of the WWAR link and link to the URL',
            'Links should open in a new tab',
            'The secondary label for each item should be "<source name> • <pub month> <pub day>, <pub year>',
            'The layout should match the attached screenshot mockups'
        ],
        'objectives': [
            'Understand how to create a feed using Snorkel',
            'Understand how to use blocks in Django templates',
            'Understand how use conditionals in Django templates',
        ],
        'scenarios': [
            {
                'title': 'A reader sees WWAR links in a section for the news post they are currently viewing',
                'steps': [
                    'Given I am a Dive Site Reader',
                    'And the WWAR links exist',
                    '''
                        <table>
                        <tr><th>News Post ID</th><th>WWAR Link</th></tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>"Click On Some Ads Around This Article And We’ll Split The Loot 60/40"</td>
                        </tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>"Man Who Comfortably Achieved Yoga Pose Doing It Completely Wrong"</td>
                        </tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>"Nation\'s Stage Managers Announce 5 Minutes To Places"</td>
                        </tr>
                        <tr>
                        <td>YYY</td>
                        <td>"Macarena turns 25"</td>
                        </tr>
                        <tr>
                        <td>YYY</td>
                        <td>"Elizabeth Holmes Arrives To Trial With Prototype For Black Box
                        That Will Prove Her Innocence"</td>
                        </tr>
                        <tr>
                        <td>YYY</td>
                        <td>"Man Arrested For Stealing 21 Tons Of Pistachios"</td>
                        </tr>
                        </table>
                    ''',
                    'When I am on the News Post ZZZ detail page',
                    'Then the newspost contains a "What we are reading" section',
                    'And the "What we are reading" section contains the links',
                    '''
                        <table>
                        <tr><th>WWAR Link</th></tr>
                        <tr>
                        <td>"Click On Some Ads Around This Article And We’ll Split The Loot 60/40"</td>
                        </tr>
                        <tr>
                        <td>"Man Who Comfortably Achieved Yoga Pose Doing It Completely Wrong"</td>
                        </tr>
                        <tr>
                        <td>"Nation\'s Stage Managers Announce 5 Minutes To Places"</td>
                        </tr>
                        </table>
                    ''',
                ],
            },
            {
                'title': 'WWAR section is hidden when there are no WWAR links for a given News Post',
                'steps': [
                    'Given I am a Dive Site Reader',
                    'And there are no WWAR links saved for News Post ZZZ',
                    'When I am on the News Post ZZZ detail page',
                    'Then the WWAR section is hidden'
                ]
            },
        ]
    },
    {
        'title': 'Add a related Dive News Posts sidebar',
    },
    {
        'title': 'Add a search form to archive page',
    },
]
