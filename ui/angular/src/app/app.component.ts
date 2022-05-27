import { Component } from '@angular/core';
import {FormArray, FormBuilder, FormControl, FormGroup} from "@angular/forms";

@Component({
  selector: 'app-root',
  templateUrl: '../../../../../forms/ui/angular/src/app/app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'angular10';

  customForm: FormGroup;

  constructor(private fb: FormBuilder) {

    this.customForm = this.fb.group({
      title: '',
      fields: this.fb.array([this.createField()]),
      choices: this.fb.array([this.createChoice()])
    })
  }

  get choice(): FormArray {
    return <FormArray> this.customForm.get('choices');
  }

  get field(): FormArray {
    return <FormArray> this.customForm.get('fields')
  }

  addChoice() {
    this.choice.push(this.createChoice());
  }

  addField() {
    this.field.push(this.createField());
  }

  createField(): FormGroup {
    return this.fb.group({
      type: '',
      name: '',
      desc: '',
    })
  }

  createChoice(): FormGroup {
    return this.fb.group({
      choice: ''
    })
  }

  removeField(i: number) {
    this.field.removeAt(i);
  }

  removeChoice(n: number) {
    this.choice.removeAt(n);
  }

  onSubmit() {
    console.log(this.customForm.value);

  }

  private selectedLink: string = "Select";

  setradio(e: string): void {
    this.selectedLink = e;
  }

  isSelected(name: string): boolean {
    if (!this.selectedLink) { // if no radio button is selected, always return false so every nothing is shown
      return false;
    }

    return (this.selectedLink === name); // if current radio button is selected, return true, else return false
  }
}


