"""
Sample video data and references for testing the Sports Talent Assessment Platform.
This module provides sample video information and test cases for different fitness assessments.
"""

import os
from typing import Dict, List, Optional

class SampleVideoManager:
    """Manages sample videos and test cases for the fitness assessment platform"""
    
    def __init__(self):
        # Sample video metadata for different test types
        self.sample_videos = {
            'Vertical Jump': [
                {
                    'id': 'vj_001',
                    'title': 'Vertical Jump - Proper Form Example',
                    'description': 'Demonstrates correct vertical jump technique with clear takeoff and landing',
                    'duration': '5 seconds',
                    'resolution': '1080x720',
                    'athlete_info': {
                        'age': 20,
                        'gender': 'Male',
                        'sport': 'Athletics'
                    },
                    'expected_metrics': {
                        'jump_height_normalized': 0.45,
                        'flight_time_seconds': 0.8,
                        'performance_score': 85
                    },
                    'key_features': [
                        'Clear pre-jump preparation',
                        'Explosive takeoff',
                        'Maximum height reach',
                        'Controlled landing'
                    ]
                },
                {
                    'id': 'vj_002',
                    'title': 'Vertical Jump - Beginner Level',
                    'description': 'Basic vertical jump performance for comparison',
                    'duration': '4 seconds',
                    'resolution': '720x480',
                    'athlete_info': {
                        'age': 16,
                        'gender': 'Female',
                        'sport': 'Basketball'
                    },
                    'expected_metrics': {
                        'jump_height_normalized': 0.25,
                        'flight_time_seconds': 0.5,
                        'performance_score': 65
                    },
                    'key_features': [
                        'Standard jump technique',
                        'Moderate height',
                        'Good form consistency'
                    ]
                }
            ],
            
            'Sit-ups (1 minute)': [
                {
                    'id': 'su_001',
                    'title': 'Sit-ups - High Performance',
                    'description': 'Fast-paced sit-ups with excellent form over 60 seconds',
                    'duration': '60 seconds',
                    'resolution': '1080x720',
                    'athlete_info': {
                        'age': 22,
                        'gender': 'Male',
                        'sport': 'Wrestling'
                    },
                    'expected_metrics': {
                        'rep_count': 55,
                        'cadence_per_minute': 55,
                        'performance_score': 90
                    },
                    'key_features': [
                        'Consistent rhythm',
                        'Full range of motion',
                        'Maintained form throughout',
                        'High repetition count'
                    ]
                },
                {
                    'id': 'su_002',
                    'title': 'Sit-ups - Standard Form',
                    'description': 'Proper sit-up technique demonstration at moderate pace',
                    'duration': '60 seconds',
                    'resolution': '720x480',
                    'athlete_info': {
                        'age': 18,
                        'gender': 'Female',
                        'sport': 'General Fitness'
                    },
                    'expected_metrics': {
                        'rep_count': 35,
                        'cadence_per_minute': 35,
                        'performance_score': 75
                    },
                    'key_features': [
                        'Proper breathing technique',
                        'Controlled movements',
                        'Good posture maintenance'
                    ]
                }
            ],
            
            '50m Sprint': [
                {
                    'id': 'sp_001',
                    'title': '50m Sprint - Elite Performance',
                    'description': 'High-speed sprint demonstrating excellent acceleration and form',
                    'duration': '8 seconds',
                    'resolution': '1080x720',
                    'athlete_info': {
                        'age': 23,
                        'gender': 'Male',
                        'sport': 'Athletics'
                    },
                    'expected_metrics': {
                        'estimated_speed': 0.15,
                        'duration_seconds': 7.2,
                        'performance_score': 92
                    },
                    'key_features': [
                        'Explosive start',
                        'Maintained speed',
                        'Proper running form',
                        'Strong finish'
                    ]
                }
            ],
            
            'Push-ups': [
                {
                    'id': 'pu_001',
                    'title': 'Push-ups - Perfect Form',
                    'description': 'Demonstrates ideal push-up technique with full range of motion',
                    'duration': '45 seconds',
                    'resolution': '1080x720',
                    'athlete_info': {
                        'age': 25,
                        'gender': 'Male',
                        'sport': 'CrossFit'
                    },
                    'expected_metrics': {
                        'rep_count': 40,
                        'cadence_per_minute': 53,
                        'performance_score': 88
                    },
                    'key_features': [
                        'Full body alignment',
                        'Complete range of motion',
                        'Steady rhythm',
                        'Proper breathing'
                    ]
                }
            ],
            
            'Flexibility Test': [
                {
                    'id': 'ft_001',
                    'title': 'Flexibility Test - Sit and Reach',
                    'description': 'Proper sit-and-reach flexibility assessment technique',
                    'duration': '15 seconds',
                    'resolution': '720x480',
                    'athlete_info': {
                        'age': 19,
                        'gender': 'Female',
                        'sport': 'Yoga'
                    },
                    'expected_metrics': {
                        'max_reach_distance': 0.22,
                        'flexibility_range': 0.18,
                        'performance_score': 85
                    },
                    'key_features': [
                        'Gradual reach progression',
                        'Sustained final position',
                        'Good posture maintenance',
                        'Controlled movement'
                    ]
                }
            ]
        }
        
        # Test case scenarios for validation
        self.test_scenarios = [
            {
                'name': 'Perfect Performance Test',
                'description': 'High-quality video with excellent performance metrics',
                'test_type': 'Vertical Jump',
                'expected_outcome': {
                    'overall_score': 90,
                    'verification_status': 'verified',
                    'authenticity_score': 95
                }
            },
            {
                'name': 'Average Performance Test',
                'description': 'Standard quality video with moderate performance',
                'test_type': 'Sit-ups (1 minute)',
                'expected_outcome': {
                    'overall_score': 65,
                    'verification_status': 'verified',
                    'authenticity_score': 88
                }
            },
            {
                'name': 'Low Quality Video Test',
                'description': 'Test system response to poor video quality',
                'test_type': 'Push-ups',
                'expected_outcome': {
                    'overall_score': 45,
                    'verification_status': 'pending_review',
                    'authenticity_score': 70
                }
            }
        ]
    
    def get_sample_videos(self, test_type: Optional[str] = None) -> List[Dict]:
        """
        Get sample videos for testing
        
        Args:
            test_type: Filter by specific test type (optional)
            
        Returns:
            List of sample video metadata
        """
        if test_type and test_type in self.sample_videos:
            return self.sample_videos[test_type]
        elif test_type is None:
            # Return all sample videos
            all_videos = []
            for videos in self.sample_videos.values():
                all_videos.extend(videos)
            return all_videos
        else:
            return []
    
    def get_test_scenarios(self) -> List[Dict]:
        """Get test scenarios for system validation"""
        return self.test_scenarios
    
    def get_video_requirements(self, test_type: str) -> Dict:
        """
        Get video recording requirements for specific test type
        
        Args:
            test_type: Name of the fitness test
            
        Returns:
            Dictionary containing video requirements
        """
        requirements = {
            'Vertical Jump': {
                'duration': '3-10 seconds',
                'min_resolution': '640x480',
                'recommended_resolution': '1280x720',
                'fps': '30 fps minimum',
                'camera_angle': 'Side profile view',
                'distance': '2-3 meters from subject',
                'lighting': 'Good natural or artificial lighting',
                'background': 'Clear, uncluttered background',
                'specific_requirements': [
                    'Full body must be visible in frame',
                    'Ground/landing surface must be visible',
                    'Camera should be stable (tripod recommended)',
                    'Subject should wear contrasting clothing'
                ]
            },
            'Sit-ups (1 minute)': {
                'duration': '60-65 seconds',
                'min_resolution': '640x480',
                'recommended_resolution': '1280x720',
                'fps': '30 fps minimum',
                'camera_angle': 'Side profile view',
                'distance': '1.5-2 meters from subject',
                'lighting': 'Consistent lighting throughout',
                'background': 'Clear floor space',
                'specific_requirements': [
                    'Full body profile must be visible',
                    'Mat or floor surface clearly visible',
                    'Start and end positions clearly shown',
                    'No interruptions during recording'
                ]
            },
            '50m Sprint': {
                'duration': '5-15 seconds',
                'min_resolution': '720x480',
                'recommended_resolution': '1920x1080',
                'fps': '60 fps recommended',
                'camera_angle': 'Side view of running path',
                'distance': '10-15 meters from running path',
                'lighting': 'Outdoor daylight preferred',
                'background': 'Clear track or open space',
                'specific_requirements': [
                    'Start and finish points must be visible',
                    'Full running motion captured',
                    'Minimal camera movement',
                    'Clear view of running form'
                ]
            },
            'Push-ups': {
                'duration': '30-90 seconds',
                'min_resolution': '640x480',
                'recommended_resolution': '1280x720',
                'fps': '30 fps minimum',
                'camera_angle': 'Side profile view',
                'distance': '1.5-2 meters from subject',
                'lighting': 'Good consistent lighting',
                'background': 'Clear floor space',
                'specific_requirements': [
                    'Full body profile visible',
                    'Floor/ground surface visible',
                    'Complete range of motion shown',
                    'Stable camera position'
                ]
            },
            'Flexibility Test': {
                'duration': '10-30 seconds',
                'min_resolution': '640x480',
                'recommended_resolution': '1280x720',
                'fps': '30 fps minimum',
                'camera_angle': 'Side view',
                'distance': '1-2 meters from subject',
                'lighting': 'Good lighting on measurement area',
                'background': 'Clear background with measurement reference',
                'specific_requirements': [
                    'Measurement scale or reference visible',
                    'Full reaching motion captured',
                    'Final position held for 2-3 seconds',
                    'Clear view of reach extension'
                ]
            }
        }
        
        return requirements.get(test_type, {
            'duration': 'Variable',
            'min_resolution': '640x480',
            'fps': '30 fps minimum',
            'general_requirements': [
                'Good lighting conditions',
                'Stable camera position',
                'Clear view of subject',
                'Minimal background distractions'
            ]
        })
    
    def get_common_issues(self) -> List[Dict]:
        """Get common video issues and solutions"""
        return [
            {
                'issue': 'Poor Video Quality',
                'symptoms': [
                    'Blurry or pixelated video',
                    'Low resolution',
                    'Compressed file'
                ],
                'solutions': [
                    'Use higher resolution camera settings',
                    'Ensure good lighting conditions',
                    'Clean camera lens',
                    'Use minimal video compression'
                ],
                'impact': 'May affect pose detection accuracy'
            },
            {
                'issue': 'Inadequate Lighting',
                'symptoms': [
                    'Dark or shadowy video',
                    'Inconsistent brightness',
                    'Overexposed areas'
                ],
                'solutions': [
                    'Record in well-lit area',
                    'Use additional lighting if needed',
                    'Avoid backlighting',
                    'Maintain consistent lighting throughout'
                ],
                'impact': 'Reduces movement analysis accuracy'
            },
            {
                'issue': 'Camera Movement',
                'symptoms': [
                    'Shaky or unstable footage',
                    'Subject moving out of frame',
                    'Changing camera angle'
                ],
                'solutions': [
                    'Use tripod or stable surface',
                    'Keep camera stationary during recording',
                    'Frame subject with some margin',
                    'Use image stabilization if available'
                ],
                'impact': 'Affects motion tracking reliability'
            },
            {
                'issue': 'Incomplete Movement Capture',
                'symptoms': [
                    'Parts of movement cut off',
                    'Subject partially out of frame',
                    'Movement starts/ends outside recording'
                ],
                'solutions': [
                    'Frame wider to include full movement',
                    'Start recording before movement begins',
                    'Continue recording until movement ends',
                    'Ensure full body visibility'
                ],
                'impact': 'Incomplete performance analysis'
            },
            {
                'issue': 'Background Distractions',
                'symptoms': [
                    'Busy or cluttered background',
                    'Moving objects in background',
                    'Poor contrast with subject'
                ],
                'solutions': [
                    'Choose plain, clear background',
                    'Ensure good contrast with clothing',
                    'Remove unnecessary objects',
                    'Use appropriate camera distance'
                ],
                'impact': 'May interfere with pose detection'
            }
        ]
    
    def validate_video_requirements(self, video_metadata: Dict, test_type: str) -> Dict:
        """
        Validate if video meets requirements for the test type
        
        Args:
            video_metadata: Video file metadata
            test_type: Type of fitness test
            
        Returns:
            Validation results with pass/fail and recommendations
        """
        requirements = self.get_video_requirements(test_type)
        validation_results = {
            'overall_pass': True,
            'checks': {},
            'warnings': [],
            'recommendations': []
        }
        
        # Duration check
        video_duration = video_metadata.get('duration', 0)
        required_duration = requirements.get('duration', '')
        
        if test_type == 'Sit-ups (1 minute)' and video_duration < 55:
            validation_results['checks']['duration'] = {
                'pass': False,
                'message': 'Video too short for 1-minute sit-up test'
            }
            validation_results['overall_pass'] = False
        elif test_type == 'Vertical Jump' and (video_duration < 3 or video_duration > 15):
            validation_results['checks']['duration'] = {
                'pass': False,
                'message': 'Video duration should be 3-15 seconds for vertical jump'
            }
            validation_results['warnings'].append('Duration outside recommended range')
        else:
            validation_results['checks']['duration'] = {
                'pass': True,
                'message': 'Duration appropriate for test type'
            }
        
        # Resolution check
        min_resolution = requirements.get('min_resolution', '640x480')
        video_resolution = video_metadata.get('resolution', '0x0')
        
        if video_resolution and 'x' in video_resolution:
            width, height = map(int, video_resolution.split('x'))
            min_width, min_height = map(int, min_resolution.split('x'))
            
            if width >= min_width and height >= min_height:
                validation_results['checks']['resolution'] = {
                    'pass': True,
                    'message': 'Resolution meets minimum requirements'
                }
            else:
                validation_results['checks']['resolution'] = {
                    'pass': False,
                    'message': f'Resolution below minimum {min_resolution}'
                }
                validation_results['warnings'].append('Low resolution may affect analysis accuracy')
        
        # Add general recommendations
        if not validation_results['overall_pass']:
            validation_results['recommendations'].extend([
                'Review video recording requirements',
                'Consider re-recording with improved settings',
                'Ensure proper camera setup and lighting'
            ])
        
        return validation_results
    
    def get_recording_tips(self, test_type: str) -> List[str]:
        """Get recording tips for specific test type"""
        tips = {
            'Vertical Jump': [
                "Set camera at waist height, 2-3 meters away",
                "Ensure full body is visible from head to feet",
                "Record in profile (side) view for best analysis",
                "Use good lighting to clearly see movement",
                "Keep camera still - use a tripod if possible",
                "Start recording before the jump and continue after landing"
            ],
            'Sit-ups (1 minute)': [
                "Position camera to show full body profile",
                "Ensure the mat/floor surface is clearly visible",
                "Record the entire 60-second duration without breaks",
                "Use consistent lighting throughout",
                "Keep camera stable and at consistent height",
                "Wear contrasting clothing for better pose detection"
            ],
            '50m Sprint': [
                "Position camera perpendicular to running path",
                "Ensure start and finish points are visible",
                "Use high frame rate (60fps) if available",
                "Record from sufficient distance to capture full run",
                "Minimize camera movement - use tripod",
                "Good outdoor lighting provides best results"
            ],
            'Push-ups': [
                "Record from the side to show full range of motion",
                "Position camera at floor level for best angle",
                "Ensure full body is visible throughout exercise",
                "Use stable camera position for entire duration",
                "Good lighting helps detect proper form",
                "Continue recording until exercise is complete"
            ],
            'Flexibility Test': [
                "Record from the side to show reaching motion",
                "Include measurement reference (ruler/scale) if possible",
                "Capture the approach, reach, and hold phases",
                "Ensure good lighting on the measurement area",
                "Hold final position for 2-3 seconds",
                "Keep camera stable and properly framed"
            ]
        }
        
        general_tips = [
            "Clean your camera lens before recording",
            "Test your setup with a short recording first",
            "Ensure adequate storage space on your device",
            "Record in a quiet environment when possible",
            "Have backup recording options ready"
        ]
        
        return tips.get(test_type, general_tips)

# Global instance for easy access
sample_video_manager = SampleVideoManager()

def get_sample_videos(test_type: Optional[str] = None) -> List[Dict]:
    """Get sample videos for testing"""
    return sample_video_manager.get_sample_videos(test_type)

def get_video_requirements(test_type: str) -> Dict:
    """Get video requirements for specific test type"""
    return sample_video_manager.get_video_requirements(test_type)

def get_recording_tips(test_type: str) -> List[str]:
    """Get recording tips for specific test type"""
    return sample_video_manager.get_recording_tips(test_type)

def get_common_issues() -> List[Dict]:
    """Get common video issues and solutions"""
    return sample_video_manager.get_common_issues()

# Example usage and test data
if __name__ == "__main__":
    # Example of how to use the sample video manager
    manager = SampleVideoManager()
    
    # Get all vertical jump samples
    vj_samples = manager.get_sample_videos('Vertical Jump')
    print(f"Found {len(vj_samples)} vertical jump samples")
    
    # Get requirements for sit-ups
    requirements = manager.get_video_requirements('Sit-ups (1 minute)')
    print(f"Sit-up requirements: {requirements['duration']}")
    
    # Get recording tips
    tips = manager.get_recording_tips('Push-ups')
    print(f"Push-up tips: {len(tips)} recommendations")
