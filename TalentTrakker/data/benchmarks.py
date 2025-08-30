"""
Performance benchmarks for fitness tests based on age groups and gender.
These benchmarks are used for scoring and comparison purposes.
"""

# Age group definitions
AGE_GROUPS = {
    (12, 15): "Youth",
    (16, 19): "Junior",
    (20, 25): "Adult", 
    (26, 30): "Senior",
    (31, 40): "Masters"
}

# Gender adjustment factors for performance comparison
GENDER_FACTORS = {
    'Male': 1.0,
    'Female': 0.9,  # Adjusted for physiological differences
    'Other': 0.95   # Default adjustment
}

# Performance benchmarks by test type, age group, and gender
# Values are in normalized units based on video analysis metrics
PERFORMANCE_BENCHMARKS = {
    'Vertical Jump': {
        'Youth': {
            'Male': {
                'jump_height': {'excellent': 45, 'good': 35, 'average': 25, 'poor': 15},
                'flight_time': {'excellent': 0.8, 'good': 0.6, 'average': 0.4, 'poor': 0.2},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'jump_height': {'excellent': 40, 'good': 30, 'average': 22, 'poor': 12},
                'flight_time': {'excellent': 0.7, 'good': 0.55, 'average': 0.35, 'poor': 0.18},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Junior': {
            'Male': {
                'jump_height': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 20},
                'flight_time': {'excellent': 0.9, 'good': 0.7, 'average': 0.5, 'poor': 0.25},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'jump_height': {'excellent': 48, 'good': 38, 'average': 28, 'poor': 18},
                'flight_time': {'excellent': 0.8, 'good': 0.6, 'average': 0.4, 'poor': 0.22},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Adult': {
            'Male': {
                'jump_height': {'excellent': 60, 'good': 50, 'average': 40, 'poor': 25},
                'flight_time': {'excellent': 1.0, 'good': 0.8, 'average': 0.6, 'poor': 0.3},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'jump_height': {'excellent': 52, 'good': 42, 'average': 32, 'poor': 22},
                'flight_time': {'excellent': 0.85, 'good': 0.65, 'average': 0.45, 'poor': 0.25},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Senior': {
            'Male': {
                'jump_height': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 22},
                'flight_time': {'excellent': 0.9, 'good': 0.7, 'average': 0.5, 'poor': 0.28},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'jump_height': {'excellent': 48, 'good': 38, 'average': 28, 'poor': 18},
                'flight_time': {'excellent': 0.8, 'good': 0.6, 'average': 0.4, 'poor': 0.22},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Masters': {
            'Male': {
                'jump_height': {'excellent': 50, 'good': 40, 'average': 30, 'poor': 20},
                'flight_time': {'excellent': 0.8, 'good': 0.6, 'average': 0.45, 'poor': 0.25},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'jump_height': {'excellent': 42, 'good': 32, 'average': 24, 'poor': 16},
                'flight_time': {'excellent': 0.7, 'good': 0.5, 'average': 0.35, 'poor': 0.2},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        }
    },
    
    'Sit-ups (1 minute)': {
        'Youth': {
            'Male': {
                'rep_count': {'excellent': 45, 'good': 35, 'average': 25, 'poor': 15},
                'cadence': {'excellent': 50, 'good': 40, 'average': 30, 'poor': 20},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'rep_count': {'excellent': 40, 'good': 30, 'average': 22, 'poor': 12},
                'cadence': {'excellent': 45, 'good': 35, 'average': 26, 'poor': 16},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Junior': {
            'Male': {
                'rep_count': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 20},
                'cadence': {'excellent': 60, 'good': 50, 'average': 40, 'poor': 25},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'rep_count': {'excellent': 50, 'good': 40, 'average': 30, 'poor': 18},
                'cadence': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 22},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Adult': {
            'Male': {
                'rep_count': {'excellent': 60, 'good': 50, 'average': 40, 'poor': 25},
                'cadence': {'excellent': 65, 'good': 55, 'average': 45, 'poor': 30},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'rep_count': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 22},
                'cadence': {'excellent': 60, 'good': 50, 'average': 40, 'poor': 26},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Senior': {
            'Male': {
                'rep_count': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 22},
                'cadence': {'excellent': 60, 'good': 50, 'average': 40, 'poor': 28},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'rep_count': {'excellent': 48, 'good': 38, 'average': 28, 'poor': 18},
                'cadence': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 24},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Masters': {
            'Male': {
                'rep_count': {'excellent': 50, 'good': 40, 'average': 30, 'poor': 20},
                'cadence': {'excellent': 55, 'good': 45, 'average': 35, 'poor': 25},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'rep_count': {'excellent': 42, 'good': 32, 'average': 24, 'poor': 16},
                'cadence': {'excellent': 48, 'good': 38, 'average': 28, 'poor': 20},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        }
    },
    
    '50m Sprint': {
        'Youth': {
            'Male': {
                'speed': {'excellent': 12, 'good': 10, 'average': 8, 'poor': 6},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'speed': {'excellent': 10, 'good': 8.5, 'average': 7, 'poor': 5},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Junior': {
            'Male': {
                'speed': {'excellent': 15, 'good': 12, 'average': 10, 'poor': 7},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'speed': {'excellent': 13, 'good': 10.5, 'average': 8.5, 'poor': 6},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Adult': {
            'Male': {
                'speed': {'excellent': 18, 'good': 15, 'average': 12, 'poor': 8},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'speed': {'excellent': 15, 'good': 12, 'average': 10, 'poor': 7},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Senior': {
            'Male': {
                'speed': {'excellent': 16, 'good': 13, 'average': 10, 'poor': 7},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'speed': {'excellent': 13, 'good': 10.5, 'average': 8.5, 'poor': 6},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Masters': {
            'Male': {
                'speed': {'excellent': 14, 'good': 11, 'average': 9, 'poor': 6},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'speed': {'excellent': 11, 'good': 9, 'average': 7.5, 'poor': 5},
                'acceleration': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        }
    },
    
    'Push-ups': {
        'Youth': {
            'Male': {
                'rep_count': {'excellent': 35, 'good': 25, 'average': 18, 'poor': 10},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            },
            'Female': {
                'rep_count': {'excellent': 25, 'good': 18, 'average': 12, 'poor': 6},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            }
        },
        'Junior': {
            'Male': {
                'rep_count': {'excellent': 45, 'good': 35, 'average': 25, 'poor': 15},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            },
            'Female': {
                'rep_count': {'excellent': 30, 'good': 22, 'average': 16, 'poor': 8},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            }
        },
        'Adult': {
            'Male': {
                'rep_count': {'excellent': 50, 'good': 40, 'average': 30, 'poor': 18},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            },
            'Female': {
                'rep_count': {'excellent': 35, 'good': 25, 'average': 18, 'poor': 10},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            }
        },
        'Senior': {
            'Male': {
                'rep_count': {'excellent': 45, 'good': 35, 'average': 25, 'poor': 15},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            },
            'Female': {
                'rep_count': {'excellent': 30, 'good': 22, 'average': 16, 'poor': 8},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            }
        },
        'Masters': {
            'Male': {
                'rep_count': {'excellent': 40, 'good': 30, 'average': 22, 'poor': 12},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            },
            'Female': {
                'rep_count': {'excellent': 25, 'good': 18, 'average': 12, 'poor': 6},
                'form_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40},
                'endurance': {'excellent': 85, 'good': 70, 'average': 55, 'poor': 35}
            }
        }
    },
    
    'Flexibility Test': {
        'Youth': {
            'Male': {
                'reach_distance': {'excellent': 15, 'good': 10, 'average': 5, 'poor': 0},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'reach_distance': {'excellent': 18, 'good': 13, 'average': 8, 'poor': 2},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Junior': {
            'Male': {
                'reach_distance': {'excellent': 18, 'good': 13, 'average': 8, 'poor': 2},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'reach_distance': {'excellent': 22, 'good': 17, 'average': 12, 'poor': 5},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Adult': {
            'Male': {
                'reach_distance': {'excellent': 20, 'good': 15, 'average': 10, 'poor': 3},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'reach_distance': {'excellent': 25, 'good': 20, 'average': 15, 'poor': 8},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Senior': {
            'Male': {
                'reach_distance': {'excellent': 18, 'good': 13, 'average': 8, 'poor': 2},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'reach_distance': {'excellent': 22, 'good': 17, 'average': 12, 'poor': 5},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        },
        'Masters': {
            'Male': {
                'reach_distance': {'excellent': 15, 'good': 10, 'average': 5, 'poor': 0},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            },
            'Female': {
                'reach_distance': {'excellent': 18, 'good': 13, 'average': 8, 'poor': 2},
                'stability': {'excellent': 95, 'good': 85, 'average': 70, 'poor': 50},
                'technique_score': {'excellent': 90, 'good': 75, 'average': 60, 'poor': 40}
            }
        }
    }
}

# Sport-specific performance standards for talent identification
SPORT_SPECIFIC_BENCHMARKS = {
    'Athletics': {
        'critical_tests': ['Vertical Jump', '50m Sprint'],
        'weight_factors': {'Vertical Jump': 0.4, '50m Sprint': 0.6},
        'elite_threshold': 85,
        'talent_threshold': 75
    },
    'Football': {
        'critical_tests': ['50m Sprint', 'Push-ups'],
        'weight_factors': {'50m Sprint': 0.5, 'Push-ups': 0.5},
        'elite_threshold': 80,
        'talent_threshold': 70
    },
    'Swimming': {
        'critical_tests': ['Push-ups', 'Flexibility Test'],
        'weight_factors': {'Push-ups': 0.6, 'Flexibility Test': 0.4},
        'elite_threshold': 82,
        'talent_threshold': 72
    },
    'Wrestling': {
        'critical_tests': ['Sit-ups (1 minute)', 'Push-ups'],
        'weight_factors': {'Sit-ups (1 minute)': 0.5, 'Push-ups': 0.5},
        'elite_threshold': 83,
        'talent_threshold': 73
    },
    'Basketball': {
        'critical_tests': ['Vertical Jump', '50m Sprint'],
        'weight_factors': {'Vertical Jump': 0.7, '50m Sprint': 0.3},
        'elite_threshold': 84,
        'talent_threshold': 74
    },
    'Boxing': {
        'critical_tests': ['Push-ups', 'Sit-ups (1 minute)'],
        'weight_factors': {'Push-ups': 0.5, 'Sit-ups (1 minute)': 0.5},
        'elite_threshold': 81,
        'talent_threshold': 71
    }
}

# National and international performance comparison data
PERFORMANCE_PERCENTILES = {
    'national': {
        50: {'score_range': (40, 60), 'description': 'Average national performance'},
        75: {'score_range': (60, 75), 'description': 'Above average national performance'},
        90: {'score_range': (75, 85), 'description': 'Excellent national performance'},
        95: {'score_range': (85, 95), 'description': 'Elite national performance'},
        99: {'score_range': (95, 100), 'description': 'World-class performance'}
    },
    'state': {
        50: {'score_range': (35, 55), 'description': 'Average state performance'},
        75: {'score_range': (55, 70), 'description': 'Above average state performance'},
        90: {'score_range': (70, 82), 'description': 'Excellent state performance'},
        95: {'score_range': (82, 92), 'description': 'Elite state performance'},
        99: {'score_range': (92, 100), 'description': 'Outstanding state performance'}
    }
}

def get_benchmark(test_type: str, age: int, gender: str) -> dict:
    """
    Get performance benchmark for specific test, age, and gender
    
    Args:
        test_type: Name of the fitness test
        age: Athlete's age
        gender: Athlete's gender
        
    Returns:
        Dictionary containing benchmark data
    """
    # Determine age group
    age_group = "Adult"  # Default
    for age_range, group_name in AGE_GROUPS.items():
        min_age, max_age = age_range
        if min_age <= age <= max_age:
            age_group = group_name
            break
    
    # Get benchmark data
    if (test_type in PERFORMANCE_BENCHMARKS and 
        age_group in PERFORMANCE_BENCHMARKS[test_type] and
        gender in PERFORMANCE_BENCHMARKS[test_type][age_group]):
        
        return PERFORMANCE_BENCHMARKS[test_type][age_group][gender]
    
    # Return default benchmark if specific one not found
    return {
        'excellent': 90, 'good': 75, 'average': 60, 'poor': 40
    }

def get_sport_specific_assessment(sport: str, test_scores: dict) -> dict:
    """
    Get sport-specific talent assessment
    
    Args:
        sport: Sport of interest
        test_scores: Dictionary of test scores
        
    Returns:
        Dictionary containing sport-specific assessment
    """
    if sport not in SPORT_SPECIFIC_BENCHMARKS:
        return {
            'sport_score': 0,
            'talent_level': 'Unknown',
            'recommendation': 'Sport-specific benchmarks not available'
        }
    
    sport_config = SPORT_SPECIFIC_BENCHMARKS[sport]
    critical_tests = sport_config['critical_tests']
    weight_factors = sport_config['weight_factors']
    
    # Calculate weighted sport-specific score
    weighted_score = 0
    total_weight = 0
    
    for test in critical_tests:
        if test in test_scores:
            score = test_scores[test]
            weight = weight_factors.get(test, 1.0)
            weighted_score += score * weight
            total_weight += weight
    
    sport_score = weighted_score / total_weight if total_weight > 0 else 0
    
    # Determine talent level
    if sport_score >= sport_config['elite_threshold']:
        talent_level = 'Elite Potential'
        recommendation = f'Exceptional talent for {sport}. Recommend immediate advanced training program.'
    elif sport_score >= sport_config['talent_threshold']:
        talent_level = 'High Potential'
        recommendation = f'Strong potential for {sport}. Recommend specialized training and development.'
    elif sport_score >= 60:
        talent_level = 'Moderate Potential'
        recommendation = f'Shows promise for {sport}. Focus on specific skill development.'
    else:
        talent_level = 'Developing'
        recommendation = f'Continue training fundamentals. Consider other sports that match strengths.'
    
    return {
        'sport_score': sport_score,
        'talent_level': talent_level,
        'recommendation': recommendation,
        'critical_tests_performance': {test: test_scores.get(test, 0) for test in critical_tests}
    }

def compare_to_national_standards(score: float) -> dict:
    """
    Compare performance score to national standards
    
    Args:
        score: Performance score (0-100)
        
    Returns:
        Dictionary containing national comparison data
    """
    national_percentiles = PERFORMANCE_PERCENTILES['national']
    
    for percentile in sorted(national_percentiles.keys(), reverse=True):
        score_range = national_percentiles[percentile]['score_range']
        if score_range[0] <= score <= score_range[1]:
            return {
                'percentile': percentile,
                'description': national_percentiles[percentile]['description'],
                'performance_level': f'{percentile}th percentile nationally'
            }
    
    # Handle edge cases
    if score > 95:
        return {
            'percentile': 99,
            'description': 'World-class performance',
            'performance_level': '99th percentile nationally'
        }
    else:
        return {
            'percentile': 25,
            'description': 'Below average performance',
            'performance_level': 'Below 25th percentile nationally'
        }
