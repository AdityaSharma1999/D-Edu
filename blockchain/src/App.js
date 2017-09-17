import React, { Component } from 'react'
import DEduContract from '../build/contracts/DEdu.json'
import getWeb3 from './utils/getWeb3'

import './css/oswald.css'
import './css/open-sans.css'
import './css/pure-min.css'
import './App.css'


var dedu;
var contract;
var accounts;

var current_id = 6;

class App extends Component {
    constructor(props) {
        super(props)

        this.searchStudent = this.searchStudent.bind(this);
        this.registerEnglishProblem = this.registerEnglishProblem.bind(this);
        this.registerMathProblem = this.registerMathProblem.bind(this);

        this.state = {
            storageValue: 0,
            web3: null
        }
    }

    componentWillMount() {
        // Get network provider and web3 instance.
        // See utils/getWeb3 for more info.

        getWeb3
            .then(results => {
                this.setState({
                    web3: results.web3
                })

                // Instantiate contract once web3 provided.
                this.instantiateContract()
            })
            .catch(() => {
                console.log('Error finding web3.')
            })
    }

    instantiateContract() {
        /*
         * SMART CONTRACT EXAMPLE
         *
         * Normally these functions would be called in the context of a
         * state management library, but for convenience I've placed them here.
         */

        contract = require('truffle-contract')
        dedu = contract(DEduContract)
        dedu.setProvider(this.state.web3.currentProvider)

        this.state.web3.eth.getAccounts((error, accs)=>{
            if(error != null){
                alert("There was an error fetching you accounts.");
                return;
            }
            if(accs.length == 0){
                alert("Couldn’t find any accounts! Make sure your Ethereum client is configured correctly.");
                return;
            }
            accounts = accs;
        })

        // Declaring this for later so we can chain functions on SimpleStorage.
        //Do the following functions on refresh
        this.checkOwner()
        //Fill out table of students
        this.updateValues()
    }

    updateValues(){
        this.getStudentTotal()
        this.getEngProbTotal()
        this.getMathProbTotal()
        this.getStudentName()
        this.getStudentCountry()
        this.getStudentAge()
        this.getStudentEngNum()
        this.getStudentEngDen()
        this.getStudentMathNum()
        this.getStudentMathDen()
    }

    

    checkOwner(){
        var deduInstance;

        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getOwner.call(accounts[0])
        }).then((result) => {
            // Update state with the result.
            return this.setState({ ownerValue: result })
        })
    }


    getStudentEngNum(){
        var deduInstance;
        
        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getStudentEngNum.call(accounts[current_id])
        }).then((result) => {
            console.log(result.c[0])
            // Update state with the result.
            return this.setState({studentEngNum: result.c[0]})
        })
    }

    getStudentEngDen(){
        var deduInstance;
        
        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getStudentEngDen.call(accounts[current_id])
        }).then((result) => {
            console.log(result.c[0])
            // Update state with the result.
            return this.setState({studentEngDen: result.c[0]})
        })
    }

    getStudentMathNum(){
        var deduInstance;
        
        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getStudentMathNum.call(accounts[current_id])
        }).then((result) => {
            console.log(result.c[0])
            // Update state with the result.
            return this.setState({studentMathNum: result.c[0]})
        })
    }

    getStudentMathDen(){
        var deduInstance;
        
        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getStudentMathDen.call(accounts[current_id])
        }).then((result) => {
            console.log(result.c[0])
            // Update state with the result.
            return this.setState({studentMathDen: result.c[0]})
        })
    }

    registerStudent(){
        var deduInstance;

        var studentAddress = document.getElementById("student_address").value
        var studentName = document.getElementById("student_name").value
        var studentCountry = document.getElementById("student_country").value
        var studentAge = parseInt(document.getElementById("student_age").value)
        console.log(studentAddress)
        console.log(studentName)
        console.log(studentCountry)
        console.log(studentAge)

        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.

            deduInstance.registerStudent(studentAddress, studentName, studentCountry, studentAge, {from: accounts[0], gas: 1000000})
        })
    }

    searchStudent(){
        
        current_id = parseInt(document.getElementById('search_student').value)
        console.log("current id is: " + current_id)
        console.log(this)
        this.updateValues()

    }


    getStudentTotal(){
        var deduInstance;

        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getStudentTotal.call(accounts[current_id])
        }).then((result) => {
            // Update state with the result.
            return this.setState({ studentTotal: result.c[0]})
        })
    }

    getEngProbTotal(){
        var deduInstance;

        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getEnglishProblemTotal.call(accounts[current_id])
        }).then((result) => {
            // Update state with the result.
            return this.setState({ engProbTotal: result.c[0]})
        })
    }

    getMathProbTotal(){
        var deduInstance;

        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.
            return deduInstance.getMathProblemTotal.call(accounts[current_id])
        }).then((result) => {
            // Update state with the result.
            return this.setState({ mathProbTotal: result.c[0]})
        })
    }


    getStudentName(){
        var deduInstance;
//        if(typeof(current_address)!=='undefined'){
            console.log("name working")
            
            dedu.deployed().then((instance) => {
                deduInstance = instance
                // Get the value from the contract to prove it worked.
                return deduInstance.getStudentName.call(accounts[current_id])
            }).then((result) => {
                console.log(result)
                // Update state with the result.
                return this.setState({studentName: result})
            })
 //       }

    }

    getStudentCountry(){
        var deduInstance;

  //      if(typeof(current_address)!=='undefined'){
            dedu.deployed().then((instance) => {
                deduInstance = instance
                // Get the value from the contract to prove it worked.
                return deduInstance.getStudentCountry.call(accounts[current_id])
            }).then((result) => {
                // Update state with the result.
                return this.setState({ studentCountry: result })
            })
   //     }
    }

    getStudentAge(){
        var deduInstance;

    //    if(typeof(current_address)!=='undefined'){
            dedu.deployed().then((instance) => {
                deduInstance = instance
                // Get the value from the contract to prove it worked.
                return deduInstance.getStudentAge.call(accounts[current_id])
            }).then((result) => {
                // Update state with the result.
                return this.setState({ studentAge: result.c[0]})
            })
     //   }
    }

    registerEnglishProblem(){
        var deduInstance;

        var englishProblem = document.getElementById("english_problem").value

        console.log(englishProblem)

        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.

            deduInstance.registerEnglishProblem(englishProblem, {from: accounts[0], gas: 1000000})
        })       

        this.updateValues()
    }

    registerMathProblem(){
        var deduInstance;

        var mathProblem = document.getElementById("math_problem").value
        var choice_1 = document.getElementById("choice_1").value
        var choice_2 = document.getElementById("choice_2").value
        var choice_3 = document.getElementById("choice_3").value
        var correctChoice = parseInt(document.getElementById("correct_choice").value)

        console.log(mathProblem)
        console.log(choice_1)
        console.log(choice_2)
        console.log(choice_3)
        console.log(correctChoice)

        dedu.deployed().then((instance) => {
            deduInstance = instance
            // Get the value from the contract to prove it worked.

            deduInstance.registerMathProblem(mathProblem, choice_1, choice_2, choice_3, correctChoice, {from: accounts[0], gas: 1000000})
        })       

        this.updateValues()
    }
            render() {
        return (
                <div className="App">
                <nav className="navbar pure-menu pure-menu-horizontal">
                <a href="#" className="pure-menu-heading pure-menu-link">D-Edu</a>
                </nav>

                <main className="container">
                <div className="pure-g">
                <div className="pure-u-1-1">
                <h2>Instructor</h2>
                <p>The instructor is: {this.state.ownerValue}</p>

                <h2>Add English Problem</h2>
                <p>The number of English Problems registered is: {this.state.engProbTotal}</p>
                <label htmlFor='english_problem'>Enter an English Problem: </label>
                <input id='english_problem' type='text'/>
                <br/>
                <button onClick={this.registerEnglishProblem}>Submit</button>

                <h2>Add Math Problem</h2>
                <p>The number of Math Problems registered is: {this.state.mathProbTotal}</p>
                <label htmlFor='math_problem'>Enter an Math Problem: </label>
                <input id='math_problem' type='text'/>
                <br/>
                <label htmlFor='choice_1'>Enter first choice: </label>
                <input id='choice_1' type='text'/>
                <br/>
                <label htmlFor='choice_2'>Enter second choice: </label>
                <input id='choice_2' type='text'/>
                <br/>
                <label htmlFor='choice_3'>Enter third choice: </label>
                <input id='choice_3' type='text'/>
                <br/>
                <label htmlFor='correct_choice'>Enter number of correct choice (1-3): </label>
                <input id='correct_choice' type='text'/>
                <br/>
                <button onClick={this.registerMathProblem}>Submit</button>


                <h2>Add Students</h2>

                <label htmlFor='student_address'>Student Address: </label>
                <input id='student_address' type='text'/>
                <br/>
                <label htmlFor='student_name'>Student Name: </label>
                <input id='student_name' type='text'/>
                <br/>
                <label htmlFor='student_country'>Student Country: </label>
                <input id='student_country' type='text'/>
                <br/>
                <label htmlFor='student_age'>Student Age: </label>
                <input id='student_age' type='text'/>
                <br/>
                <button onClick={this.registerStudent}>Submit</button>

                <h2>Student Information</h2>


                <p>The number of students registered is: {this.state.studentTotal}</p>

                <label htmlFor='search_student'>Search Student: </label>
                <input id='search_student' type='text'/>

                <button  onClick={this.searchStudent}>Search</button>


                <p>The student name is: {this.state.studentName}</p>
                <p>The student country is: {this.state.studentCountry}</p>
                <p>The student age is: {this.state.studentAge}</p>
                <p>English Score: {this.state.studentEngNum} out of {this.state.studentEngDen}</p>
                <p>Math Score: {this.state.studentMathNum} out of {this.state.studentMathDen}</p>
                </div>
                </div>
                </main>
                </div>

        );
    }
}

export default App
