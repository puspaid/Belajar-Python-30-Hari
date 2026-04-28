"""
Data Cleaning Utility - Mini Project Week 1
===========================================

A comprehensive toolkit for cleaning and validating datasets that i just barelly learn.
Demonstrates functions, modular design, and best practices.

Author: Puspa
Date: April 27, 2026
Week: 1 (Day 7)
Purpose: Apply all Week 1 concepts in one practical project
"""

from typing import List, Dict, Union, Any, Tuple
import statistics
from collections import Counter


def remove_duplicates(data: List[Any]) -> Tuple[List[Any], int]:
    """
    Remove duplicate values from a list.
    
    Args:
        data: List with potential duplicates
        
    Returns:
        Tuple of (cleaned list, number of duplicates removed)
    """
    original_count = len(data)
    cleaned = list(set(data)) if data else []
    duplicates_removed = original_count - len(cleaned)
    
    return cleaned, duplicates_removed


def fill_missing_values(data: List[Union[int, float, None]], 
                       strategy: str = 'mean') -> List[Union[int, float]]:
    """
    Fill missing (None) values in numeric dataset.
    
    Args:
        data: List with potential None values
        strategy: 'mean', 'median', 'mode', or 'zero'
        
    Returns:
        List with missing values filled
        
    Raises:
        ValueError: If strategy is invalid
    """
    # Filter out None values for calculation
    valid_values = [x for x in data if x is not None]
    
    if not valid_values:
        return [0] * len(data)  # All None, return zeros
    
    # Calculate fill value based on strategy
    if strategy == 'mean':
        fill_value = statistics.mean(valid_values)
    elif strategy == 'median':
        fill_value = statistics.median(valid_values)
    elif strategy == 'mode':
        fill_value = statistics.mode(valid_values)
    elif strategy == 'zero':
        fill_value = 0
    else:
        raise ValueError(f"Invalid strategy: {strategy}. Use 'mean', 'median', 'mode', or 'zero'.")
    
    # Fill missing values
    cleaned = [x if x is not None else fill_value for x in data]
    
    return cleaned


def detect_outliers(data: List[Union[int, float]], 
                   method: str = 'iqr',
                   threshold: float = 1.5) -> Dict[str, Any]:
    """
    Detect outliers in numeric dataset.
    
    Args:
        data: Numeric list
        method: 'iqr' (Interquartile Range) or 'zscore'
        threshold: Sensitivity (1.5 for IQR, 3 for z-score)
        
    Returns:
        Dictionary with outlier information
    """
    if not data:
        return {"outliers": [], "count": 0, "indices": []}
    
    # Remove None values
    clean_data = [x for x in data if x is not None]
    
    if method == 'iqr':
        # IQR method
        sorted_data = sorted(clean_data)
        n = len(sorted_data)
        
        q1_idx = n // 4
        q3_idx = (3 * n) // 4
        
        q1 = sorted_data[q1_idx]
        q3 = sorted_data[q3_idx]
        iqr = q3 - q1
        
        lower_bound = q1 - (threshold * iqr)
        upper_bound = q3 + (threshold * iqr)
        
        outliers = [x for x in clean_data if x < lower_bound or x > upper_bound]
        indices = [i for i, x in enumerate(data) if x is not None and (x < lower_bound or x > upper_bound)]
        
    else:  # z-score method
        mean = statistics.mean(clean_data)
        stdev = statistics.stdev(clean_data) if len(clean_data) > 1 else 0
        
        if stdev == 0:
            return {"outliers": [], "count": 0, "indices": []}
        
        outliers = []
        indices = []
        
        for i, x in enumerate(data):
            if x is not None:
                z_score = abs((x - mean) / stdev)
                if z_score > threshold:
                    outliers.append(x)
                    indices.append(i)
    
    return {
        "outliers": outliers,
        "count": len(outliers),
        "indices": indices,
        "method": method
    }


def validate_data_types(data: List[Any], 
                       expected_type: type) -> Tuple[bool, List[int]]:
    """
    Validate that all items in list match expected type.
    
    Args:
        data: List to validate
        expected_type: Expected Python type (int, float, str, etc.)
        
    Returns:
        Tuple of (all_valid, list of invalid indices)
    """
    invalid_indices = []
    
    for i, item in enumerate(data):
        if item is not None and not isinstance(item, expected_type):
            invalid_indices.append(i)
    
    all_valid = len(invalid_indices) == 0
    
    return all_valid, invalid_indices


def generate_data_report(data: List[Union[int, float, None]]) -> Dict[str, Any]:
    """
    Generate comprehensive statistical report for dataset.
    
    Args:
        data: Numeric dataset
        
    Returns:
        Dictionary with dataset statistics
    """
    # Remove None values for calculations
    clean_data = [x for x in data if x is not None]
    
    if not clean_data:
        return {
            "error": "No valid data to analyze",
            "total_items": len(data),
            "missing_values": len(data)
        }
    
    report = {
        "total_items": len(data),
        "valid_items": len(clean_data),
        "missing_values": len(data) - len(clean_data),
        "missing_percentage": round(((len(data) - len(clean_data)) / len(data)) * 100, 2),
        "min": min(clean_data),
        "max": max(clean_data),
        "mean": round(statistics.mean(clean_data), 2),
        "median": statistics.median(clean_data),
        "range": max(clean_data) - min(clean_data)
    }
    
    # Add standard deviation if enough data
    if len(clean_data) > 1:
        report["std_dev"] = round(statistics.stdev(clean_data), 2)
    
    return report


def clean_dataset(data: List[Any],
                 remove_dupes: bool = True,
                 fill_strategy: str = 'mean',
                 detect_out: bool = True,
                 validate_type: type = None) -> Dict[str, Any]:
    """
    Comprehensive data cleaning pipeline.
    
    This is the main function that orchestrates all cleaning operations.
    
    Args:
        data: Input dataset
        remove_dupes: Whether to remove duplicates
        fill_strategy: Strategy for filling missing values
        detect_out: Whether to detect outliers
        validate_type: Expected data type (None to skip validation)
        
    Returns:
        Dictionary containing cleaned data and cleaning report
    """
    cleaning_report = {
        "original_size": len(data),
        "operations": []
    }
    
    cleaned_data = data.copy()
    
    # Step 1: Remove duplicates
    if remove_dupes:
        cleaned_data, dupes_removed = remove_duplicates(cleaned_data)
        cleaning_report["operations"].append({
            "step": "Remove Duplicates",
            "duplicates_removed": dupes_removed,
            "status": "✅ Complete"
        })
    
    # Step 2: Validate data types
    if validate_type:
        all_valid, invalid_idx = validate_data_types(cleaned_data, validate_type)
        cleaning_report["operations"].append({
            "step": "Type Validation",
            "expected_type": validate_type.__name__,
            "all_valid": all_valid,
            "invalid_count": len(invalid_idx),
            "status": "✅ Valid" if all_valid else "⚠️ Issues found"
        })
    
    # Step 3: Fill missing values (for numeric data)
    if all(isinstance(x, (int, float, type(None))) for x in cleaned_data):
        cleaned_data = fill_missing_values(cleaned_data, fill_strategy)
        cleaning_report["operations"].append({
            "step": "Fill Missing Values",
            "strategy": fill_strategy,
            "status": "✅ Complete"
        })
    
    # Step 4: Detect outliers
    if detect_out and all(isinstance(x, (int, float)) for x in cleaned_data):
        outlier_info = detect_outliers(cleaned_data)
        cleaning_report["operations"].append({
            "step": "Outlier Detection",
            "outliers_found": outlier_info["count"],
            "outlier_values": outlier_info["outliers"],
            "status": "✅ Complete"
        })
    
    # Step 5: Generate final report
    if all(isinstance(x, (int, float, type(None))) for x in data):
        stats = generate_data_report(cleaned_data)
        cleaning_report["statistics"] = stats
    
    cleaning_report["final_size"] = len(cleaned_data)
    cleaning_report["data_reduced_by"] = len(data) - len(cleaned_data)
    
    return {
        "cleaned_data": cleaned_data,
        "report": cleaning_report
    }


def print_cleaning_report(report: Dict[str, Any]) -> None:
    """
    Pretty print the cleaning report.
    
    Args:
        report: Cleaning report dictionary
    """
    print("\n" + "="*60)
    print("DATA CLEANING REPORT")
    print("="*60)
    
    print(f"\n📊 Original Size: {report['original_size']} items")
    print(f"📊 Final Size: {report['final_size']} items")
    print(f"📊 Reduction: {report['data_reduced_by']} items")
    
    print(f"\n🔧 Operations Performed: {len(report['operations'])}")
    print("-"*60)
    
    for i, operation in enumerate(report['operations'], 1):
        print(f"\n{i}. {operation['step']}")
        for key, value in operation.items():
            if key != 'step':
                print(f"   {key}: {value}")
    
    if 'statistics' in report:
        print("\n📈 Dataset Statistics:")
        print("-"*60)
        for key, value in report['statistics'].items():
            if key != 'error':
                print(f"   {key}: {value}")
    
    print("\n" + "="*60 + "\n")


# ============================================
# EXAMPLE USAGE & TESTING
# ============================================

if __name__ == "__main__":
    print("🧹 DATA CLEANING UTILITY - DEMO\n")
    
    # Example 1: Cleaning numeric dataset with issues
    print("Example 1: Sales Data Cleaning")
    print("-"*60)
    
    sales_data = [100, 200, 150, 200, None, 180, 100, 9999, 170, None, 160]
    
    print(f"Original data: {sales_data}")
    
    result = clean_dataset(
        sales_data,
        remove_dupes=True,
        fill_strategy='median',
        detect_out=True,
        validate_type=None
    )
    
    print(f"\nCleaned data: {result['cleaned_data']}")
    print_cleaning_report(result['report'])
    
    # Example 2: Temperature readings
    print("\nExample 2: Temperature Readings")
    print("-"*60)
    
    temperatures = [25.5, 26.0, 25.8, None, 26.2, 25.5, 100.0, 25.9, None, 26.1]
    
    print(f"Original data: {temperatures}")
    
    result = clean_dataset(
        temperatures,
        remove_dupes=False,
        fill_strategy='mean',
        detect_out=True
    )
    
    print(f"\nCleaned data: {result['cleaned_data']}")
    print_cleaning_report(result['report'])
    
    # Example 3: Custom function testing
    print("\nExample 3: Individual Function Tests")
    print("-"*60)
    
    # Test outlier detection
    test_data = [10, 12, 11, 13, 10, 12, 100, 11, 12, 10]
    outlier_result = detect_outliers(test_data, method='iqr')
    print(f"\nOutliers in {test_data}:")
    print(f"Found: {outlier_result['outliers']}")
    print(f"Count: {outlier_result['count']}")
    print(f"Indices: {outlier_result['indices']}")
    
    # Test type validation
    mixed_data = [1, 2, "three", 4, 5]
    valid, invalid_idx = validate_data_types(mixed_data, int)
    print(f"\nType validation for {mixed_data}:")
    print(f"All valid integers? {valid}")
    print(f"Invalid indices: {invalid_idx}")
    
    print("\n" + "="*60)
    print("✅ Week 1 Mini Project Complete!")
    print("="*60)
