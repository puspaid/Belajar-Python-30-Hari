"""
OMR Scanner - Automatic Answer Sheet Correction System
======================================================

A complete system for automatically grading multiple-choice exams.
Perfect for teachers who need to quickly process answer sheets.

Author: Puspaid
Date: April 29, 2026
Purpose: Automate exam correction and generate analytics

Features:
- Multiple exam version support (A, B, C, etc.)
- Batch processing of student answers
- CSV export of results
- Statistical analysis (mean, median, distribution)
- Performance categorization
- Error detection and validation

Use Case: Islamic School Exam Processing
Target: SMP/SMA IT Darul Musthofa
"""

from typing import List, Dict, Tuple, Optional
import csv
from datetime import datetime


# ============================================
# CORE GRADING FUNCTIONS
# ============================================

def validate_answer_format(answers: List[str], 
                          valid_options: List[str] = ['A', 'B', 'C', 'D', 'E']) -> Tuple[bool, str]:
    """
    Validate that all answers are in acceptable format.
    
    Args:
        answers: List of student answers
        valid_options: Valid answer choices
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    for i, answer in enumerate(answers):
        if answer not in valid_options and answer != '':
            return False, f"Invalid answer at question {i+1}: '{answer}'"
    
    return True, ""


def grade_answer_sheet(student_answers: List[str], 
                      answer_key: List[str],
                      points_per_question: float = 1.0,
                      penalty_wrong: float = 0.0) -> Dict:
    """
    Grade a single answer sheet.
    
    Args:
        student_answers: Student's answers
        answer_key: Correct answers
        points_per_question: Points for correct answer
        penalty_wrong: Points deducted for wrong answer
        
    Returns:
        Dictionary with detailed results
    """
    if len(student_answers) != len(answer_key):
        raise ValueError(f"Answer count mismatch: {len(student_answers)} vs {len(answer_key)}")
    
    correct = 0
    wrong = 0
    blank = 0
    details = []
    
    for i, (student_ans, correct_ans) in enumerate(zip(student_answers, answer_key)):
        question_num = i + 1
        
        if student_ans == '':
            blank += 1
            result = 'blank'
            points = 0
        elif student_ans == correct_ans:
            correct += 1
            result = 'correct'
            points = points_per_question
        else:
            wrong += 1
            result = 'wrong'
            points = -penalty_wrong
        
        details.append({
            'question': question_num,
            'student_answer': student_ans if student_ans else '-',
            'correct_answer': correct_ans,
            'result': result,
            'points': points
        })
    
    total_points = (correct * points_per_question) - (wrong * penalty_wrong)
    max_points = len(answer_key) * points_per_question
    percentage = (total_points / max_points * 100) if max_points > 0 else 0
    
    return {
        'correct': correct,
        'wrong': wrong,
        'blank': blank,
        'total_questions': len(answer_key),
        'raw_score': total_points,
        'max_score': max_points,
        'percentage': round(percentage, 2),
        'details': details
    }


def determine_grade(percentage: float) -> str:
    """
    Convert percentage to letter grade.
    
    Args:
        percentage: Score percentage
        
    Returns:
        Letter grade (A, B, C, D, E)
    """
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'E'


def categorize_performance(percentage: float) -> str:
    """
    Categorize student performance.
    
    Args:
        percentage: Score percentage
        
    Returns:
        Performance category
    """
    if percentage >= 85:
        return 'Excellent (Mumtaz)'
    elif percentage >= 75:
        return 'Very Good (Jayyid Jiddan)'
    elif percentage >= 65:
        return 'Good (Jayyid)'
    elif percentage >= 55:
        return 'Satisfactory (Maqbul)'
    else:
        return 'Needs Improvement (Dha\'if)'


# ============================================
# BATCH PROCESSING
# ============================================

def process_class_exam(student_data: List[Dict],
                      answer_keys: Dict[str, List[str]],
                      points_per_question: float = 1.0,
                      penalty_wrong: float = 0.0) -> List[Dict]:
    """
    Process exam results for entire class.
    
    Args:
        student_data: List of student info with answers
            Format: [{'name': 'Ahmad', 'version': 'A', 'answers': ['B','C'...]}, ...]
        answer_keys: Dictionary of answer keys per version
            Format: {'A': ['B','C'...], 'B': ['C','A'...]}
        points_per_question: Points per correct answer
        penalty_wrong: Penalty for wrong answers
        
    Returns:
        List of results for each student
    """
    results = []
    
    for student in student_data:
        name = student['name']
        student_id = student.get('id', '')
        version = student['version']
        answers = student['answers']
        
        # Validate version exists
        if version not in answer_keys:
            print(f"Warning: Unknown version '{version}' for {name}")
            continue
        
        # Get answer key for this version
        key = answer_keys[version]
        
        # Validate answers
        is_valid, error_msg = validate_answer_format(answers)
        if not is_valid:
            print(f"Warning: {name} - {error_msg}")
            continue
        
        # Grade the answer sheet
        grading_result = grade_answer_sheet(answers, key, points_per_question, penalty_wrong)
        
        # Combine student info with results
        result = {
            'student_id': student_id,
            'name': name,
            'version': version,
            'correct': grading_result['correct'],
            'wrong': grading_result['wrong'],
            'blank': grading_result['blank'],
            'total_questions': grading_result['total_questions'],
            'raw_score': grading_result['raw_score'],
            'percentage': grading_result['percentage'],
            'letter_grade': determine_grade(grading_result['percentage']),
            'category': categorize_performance(grading_result['percentage']),
            'details': grading_result['details']
        }
        
        results.append(result)
    
    return results


# ============================================
# STATISTICS & ANALYSIS
# ============================================

def calculate_class_statistics(results: List[Dict]) -> Dict:
    """
    Calculate class-wide statistics.
    
    Args:
        results: List of student results
        
    Returns:
        Dictionary with statistics
    """
    if not results:
        return {}
    
    scores = [r['percentage'] for r in results]
    
    # Basic stats
    mean_score = sum(scores) / len(scores)
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    
    # Median
    if n % 2 == 0:
        median = (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2
    else:
        median = sorted_scores[n//2]
    
    # Mode (most common score range)
    score_ranges = {
        '90-100': sum(1 for s in scores if s >= 90),
        '80-89': sum(1 for s in scores if 80 <= s < 90),
        '70-79': sum(1 for s in scores if 70 <= s < 80),
        '60-69': sum(1 for s in scores if 60 <= s < 70),
        'Below 60': sum(1 for s in scores if s < 60)
    }
    
    # Grade distribution
    grade_dist = {}
    for result in results:
        grade = result['letter_grade']
        grade_dist[grade] = grade_dist.get(grade, 0) + 1
    
    # Performance categories
    category_dist = {}
    for result in results:
        category = result['category']
        category_dist[category] = category_dist.get(category, 0) + 1
    
    return {
        'total_students': len(results),
        'mean': round(mean_score, 2),
        'median': round(median, 2),
        'highest': max(scores),
        'lowest': min(scores),
        'score_ranges': score_ranges,
        'grade_distribution': grade_dist,
        'category_distribution': category_dist,
        'pass_rate': sum(1 for s in scores if s >= 60) / len(scores) * 100
    }


def identify_difficult_questions(results: List[Dict]) -> List[Dict]:
    """
    Identify questions that most students got wrong.
    
    Args:
        results: List of student results with details
        
    Returns:
        List of difficult questions with statistics
    """
    if not results:
        return []
    
    # Aggregate by question
    question_stats = {}
    total_students = len(results)
    
    for result in results:
        for detail in result['details']:
            q_num = detail['question']
            
            if q_num not in question_stats:
                question_stats[q_num] = {
                    'question': q_num,
                    'correct': 0,
                    'wrong': 0,
                    'blank': 0
                }
            
            question_stats[q_num][detail['result']] += 1
    
    # Calculate percentages and identify difficult ones
    difficult_questions = []
    
    for q_num, stats in question_stats.items():
        correct_rate = stats['correct'] / total_students * 100
        
        question_analysis = {
            'question': q_num,
            'correct_count': stats['correct'],
            'wrong_count': stats['wrong'],
            'blank_count': stats['blank'],
            'correct_rate': round(correct_rate, 2),
            'difficulty': 'Hard' if correct_rate < 40 else 'Medium' if correct_rate < 70 else 'Easy'
        }
        
        # Flag difficult questions (less than 50% got it right)
        if correct_rate < 50:
            difficult_questions.append(question_analysis)
    
    # Sort by difficulty (lowest correct rate first)
    difficult_questions.sort(key=lambda x: x['correct_rate'])
    
    return difficult_questions


# ============================================
# EXPORT FUNCTIONS
# ============================================

def export_results_to_csv(results: List[Dict], 
                         filename: str = 'exam_results.csv') -> None:
    """
    Export results to CSV file.
    
    Args:
        results: List of student results
        filename: Output CSV filename
    """
    if not results:
        print("No results to export")
        return
    
    headers = [
        'Student ID', 'Name', 'Version', 
        'Correct', 'Wrong', 'Blank', 'Total Questions',
        'Raw Score', 'Percentage', 'Letter Grade', 'Category'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for result in results:
            row = [
                result['student_id'],
                result['name'],
                result['version'],
                result['correct'],
                result['wrong'],
                result['blank'],
                result['total_questions'],
                result['raw_score'],
                result['percentage'],
                result['letter_grade'],
                result['category']
            ]
            writer.writerow(row)
    
    print(f"✅ Results exported to {filename}")


def export_statistics_report(results: List[Dict], 
                            filename: str = 'class_statistics.txt') -> None:
    """
    Generate text report with statistics.
    
    Args:
        results: List of student results
        filename: Output text filename
    """
    stats = calculate_class_statistics(results)
    difficult_qs = identify_difficult_questions(results)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write("EXAM STATISTICS REPORT\n")
        f.write("="*60 + "\n\n")
        
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Students: {stats['total_students']}\n\n")
        
        f.write("SCORE STATISTICS:\n")
        f.write("-"*60 + "\n")
        f.write(f"Mean Score: {stats['mean']}%\n")
        f.write(f"Median Score: {stats['median']}%\n")
        f.write(f"Highest Score: {stats['highest']}%\n")
        f.write(f"Lowest Score: {stats['lowest']}%\n")
        f.write(f"Pass Rate (≥60%): {stats['pass_rate']:.1f}%\n\n")
        
        f.write("SCORE DISTRIBUTION:\n")
        f.write("-"*60 + "\n")
        for range_name, count in stats['score_ranges'].items():
            percentage = count / stats['total_students'] * 100
            bar = '█' * int(percentage / 2)
            f.write(f"{range_name:12s}: {count:3d} ({percentage:5.1f}%) {bar}\n")
        
        f.write("\nGRADE DISTRIBUTION:\n")
        f.write("-"*60 + "\n")
        for grade in ['A', 'B', 'C', 'D', 'E']:
            count = stats['grade_distribution'].get(grade, 0)
            percentage = count / stats['total_students'] * 100
            bar = '█' * int(percentage / 2)
            f.write(f"Grade {grade}: {count:3d} ({percentage:5.1f}%) {bar}\n")
        
        if difficult_qs:
            f.write("\nDIFFICULT QUESTIONS (< 50% correct):\n")
            f.write("-"*60 + "\n")
            for q in difficult_qs:
                f.write(f"Question {q['question']:2d}: {q['correct_rate']:5.1f}% correct ")
                f.write(f"({q['correct_count']}/{stats['total_students']}) - {q['difficulty']}\n")
        
        f.write("\n" + "="*60 + "\n")
    
    print(f"✅ Statistics report saved to {filename}")


# ============================================
# DISPLAY FUNCTIONS
# ============================================

def print_student_result(result: Dict, show_details: bool = False) -> None:
    """
    Print formatted result for one student.
    
    Args:
        result: Student result dictionary
        show_details: Whether to show question-by-question breakdown
    """
    print("\n" + "="*60)
    print(f"STUDENT: {result['name']} ({result['student_id']})")
    print("="*60)
    print(f"Exam Version: {result['version']}")
    print(f"Correct: {result['correct']}/{result['total_questions']}")
    print(f"Wrong: {result['wrong']}")
    print(f"Blank: {result['blank']}")
    print(f"Score: {result['raw_score']}/{result['total_questions']} ({result['percentage']}%)")
    print(f"Grade: {result['letter_grade']}")
    print(f"Category: {result['category']}")
    
    if show_details:
        print("\nQUESTION DETAILS:")
        print("-"*60)
        for detail in result['details']:
            status_symbol = '✓' if detail['result'] == 'correct' else '✗' if detail['result'] == 'wrong' else '-'
            print(f"Q{detail['question']:2d}: {detail['student_answer']:1s} "
                  f"(Correct: {detail['correct_answer']}) {status_symbol}")


def print_class_summary(results:
