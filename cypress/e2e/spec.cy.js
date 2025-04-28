// describe('Create and connect to an account', () => {
//   it('Visits the Oc commerce site', () => {
//     cy.visit('/home')

//     // User is able to create an account an to be redirect to login pages

//     cy.contains('SIGNUP').click()
//     cy.url().should('include', '/user/signup')
//     // cy.contains('fname')
//     cy.get('[id^=fname]').type('fakeuser')
//     cy.get('[id^=lname]').type('toto')
//     cy.get('[id^=username]').type('fakeuser')
//     cy.get('[id^=email]').type('fake@email.com')
//     cy.get('[id^=pass]').type('1hstesh<23456789')
//     cy.get('[id^=re_pass]').type('1hstesh<23456789')
//     cy.get('form').contains('Register').click()
//     cy.url().should('include', '/user/login')

//     // User is able to connect with the previously created account
//     cy.get('[id^=your_name]').type('fakeuser')
//     cy.get('[id^=your_pass]').type('1hstesh<23456789')
//     cy.get('form').contains('Log in').click()
//     cy.url().should('include', '/home')
//     cy.contains('FAVOURITE')
//   })
// })

describe('Put item in favourite', () => {
  it('Connect to OC commerce and put in favourite', () => {
    cy.visit('/home')
    cy.contains('LOGIN').click()
    cy.url().should('include', '/user/login')
    
    cy.get('[id^=your_name]').type('fakeuser')
    cy.get('[id^=your_pass]').type('1hstesh<23456789')
    cy.contains('Log in').click()
    cy.contains('FAVOURITE').click()
    //make sure there is no favourite
    cy.contains('TO-commerce').click()


    cy.get('.portfolio-item').first().within(() => {
      cy.get('a[id^=favBtn]').click()
    })

    cy.contains('FAVOURITE').click()

    cy.get('table tbody tr').first().within(() => {
      cy.get('a[id^=favBtn]').click()
    })
    //check it has been deleted

    cy.contains('LOGOUT').click()

    // You will go to favourite pages to make sure there is no favourite
    // Then go back to home
    // You will add an item to favourite
    // You will go to favourite pages to confirm item is here
    // You will then delete the item an check it has been successfully deleted

  })
})

describe('Toggle Dark Mode', () => {
  it('Connect to OC commerce and toggle dark mode', () => {
    cy.visit('/home')
    cy.contains('LOGIN').click()
    cy.url().should('include', '/user/login')
    
    cy.get('[id^=your_name]').type('fakeuser')
    cy.get('[id^=your_pass]').type('1hstesh<23456789')
    cy.contains('Log in').click()
    cy.contains('Dark Mode').click()
    cy.contains('Light Mode').click()
    

  })
})