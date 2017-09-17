pragma solidity ^0.4.2;
import 'zeppelin-solidity/contracts/ownership/Ownable.sol';


contract DEdu is Ownable{


  uint eng_problem_num = 1;
  mapping (uint => englishProblem) public englishProblems;

  struct englishProblem{
    string problem;
  }

  uint math_problem_num = 1;
  mapping (uint => mathProblem) public mathProblems;

  struct mathProblem{
    string problem;
    string choice_1;
    string choice_2;
    string choice_3;
    uint correct;
  }

  //Student Variables
  uint current_id = 1;
  mapping (uint => address) public studentAddresses;

  

  struct Student {
    uint id;
    string name;
    string country;
    uint age;
    bool isValue;
    uint englishScoreNum;
    uint englishScoreDen;
    uint mathScoreNum;
    uint mathScoreDen;
  }

  mapping (address => Student) public students;

  function getEnglishQuestion(uint num) constant returns (string){
    return englishProblems[num].problem;
  }

  function addEnglishScore(address _stuaddr, uint _num, uint _den){
    students[_stuaddr].englishScoreNum += _num;
    students[_stuaddr].englishScoreDen += _den;
  }

  function addMathScore(address _stuaddr, uint _num, uint _den){
    students[_stuaddr].mathScoreNum += _num;
    students[_stuaddr].mathScoreDen += _den;
  }

  function registerEnglishProblem(string _problem) onlyOwner{
    englishProblems[eng_problem_num] = englishProblem({problem: _problem});
    eng_problem_num ++;
  }

  function registerMathProblem(string _problem, string _choice_1, string _choice_2, string _choice_3, uint _correct) onlyOwner{
    mathProblems[math_problem_num] = mathProblem({problem: _problem, choice_1: _choice_1, choice_2: _choice_2, choice_3: _choice_3, correct: _correct});
    math_problem_num ++;
  }

  function getMathQuestion(uint num) constant returns (string){
    return mathProblems[num].problem;
  }

  function getMathChoice1(uint num) constant returns (string){
    return mathProblems[num].choice_1;
  }

  function getMathChoice2(uint num) constant returns (string){
    return mathProblems[num].choice_2;
  }

  function getMathChoice3(uint num) constant returns (string){
    return mathProblems[num].choice_3;
  }

  function getMathCorrect(uint num) constant returns (uint){
    return mathProblems[num].correct;
  }

  function getEnglishProblemTotal() constant returns (uint){
    return eng_problem_num -1;
  }

  function getMathProblemTotal() constant returns (uint){
    return math_problem_num -1;
  }

  function registerStudent(address _stuaddr, string _name, string _country, uint _age){
    if(students[_stuaddr].isValue) throw; //prevent duplicate registered student
    studentAddresses[current_id] = _stuaddr;
    students[_stuaddr] = Student({id: current_id, name: _name, country: _country,
          age: _age, isValue: true, englishScoreNum: 0, englishScoreDen: 0, mathScoreNum: 0, mathScoreDen: 0});
    current_id ++;
  }

  function getStudentName(address _stuaddr) constant returns (string){
    return students[_stuaddr].name;
  }

  function getStudentCountry(address _stuaddr) constant returns (string){
    return students[_stuaddr].country;
  }

  function getStudentAge(address _stuaddr) constant returns (uint){
    return students[_stuaddr].age;
  }

  function getStudentTotal() constant returns (uint){
    return current_id - 1;
  }

  function getStudentEngNum(address _stuaddr) constant returns (uint){
    return students[_stuaddr].englishScoreNum;
  }

  function getStudentEngDen(address _stuaddr) constant returns (uint){
    return students[_stuaddr].englishScoreDen;
  }

  function getStudentMathNum(address _stuaddr) constant returns (uint){
    return students[_stuaddr].mathScoreNum;
  }

  function getStudentMathDen(address _stuaddr) constant returns (uint){
    return students[_stuaddr].mathScoreDen;
  }

  //Owner may add course material to the contract
  function getOwner() constant returns (address){
    return owner;
  }

}
