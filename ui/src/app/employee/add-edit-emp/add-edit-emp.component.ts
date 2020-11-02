import { Component, OnInit,Input } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-emp',
  templateUrl: './add-edit-emp.component.html',
  styleUrls: ['./add-edit-emp.component.css']
})
export class AddEditEmpComponent implements OnInit {

  constructor(private service:SharedService) { }

  @Input() emp:any;
  EmployeeId:string;
  EmployeeName:string;
  DateOfBirth:string;
  DateOfJoining:string;
  MobileNo:string;
  EmailId:string;
  Department:string;
  Designation:string;
  Location:string;

  DepartmentsList:any=[];

  ngOnInit(): void {
 
  }

  addEmployee(){
    var val = { EmployeeId:this.EmployeeId,
                EmployeeName:this.EmployeeName,
                MobileNo:this.MobileNo,
                EmailId:this.EmailId,
                DateOfBirth:this.DateOfBirth,
                DateOfJoining:this.DateOfJoining,
                Department:this.Department,
                Designation:this.Designation,
                Location:this.Location };
    this.service.addEmployee(val).subscribe(res=>{
      alert(res.toString());
    });
  }

  updateEmployee(){
    var val = { EmployeeId:this.EmployeeId,
      EmployeeName:this.EmployeeName,
      MobileNo:this.MobileNo,
      EmailId:this.EmailId,
      DateOfBirth:this.DateOfBirth,
      DateOfJoining:this.DateOfJoining,
      Department:this.Department,
      Designation:this.Designation,
      Location:this.Location };
      console.log(val);
    this.service.updateEmployee(val).subscribe(res=>{
    alert(res.toString());
    },
    error => {
      alert("Employee ID cannot be edited");
    }
    );
  }



}

