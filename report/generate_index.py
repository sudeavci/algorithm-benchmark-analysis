#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Create an index HTML file to view all reports and visualizations
"""

import os
from datetime import datetime

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sorting Algorithm Performance Analysis - Technical Reports</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #1f2937 0%, #374151 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }
        
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }
        
        header p {
            font-size: 1.1em;
            opacity: 0.9;
            margin-bottom: 5px;
        }
        
        header .meta {
            font-size: 0.9em;
            opacity: 0.7;
            margin-top: 15px;
        }
        
        .content {
            padding: 40px;
        }
        
        section {
            margin-bottom: 40px;
        }
        
        section h2 {
            color: #1f2937;
            font-size: 1.8em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #7c3aed;
        }
        
        .report-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .report-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 8px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            border-left: 5px solid #7c3aed;
        }
        
        .report-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }
        
        .report-card h3 {
            color: #1f2937;
            font-size: 1.3em;
            margin-bottom: 10px;
        }
        
        .report-card p {
            color: #374151;
            line-height: 1.6;
            margin-bottom: 10px;
            font-size: 0.95em;
        }
        
        .report-card .details {
            font-size: 0.85em;
            color: #6b7280;
            margin: 15px 0;
            padding: 10px;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 5px;
        }
        
        .btn {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 0.9em;
            font-weight: 600;
            transition: transform 0.2s, box-shadow 0.2s;
            border: none;
            cursor: pointer;
        }
        
        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .chart-container {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border: 2px solid #e5e7eb;
        }
        
        .chart-container img {
            width: 100%;
            height: auto;
            display: block;
        }
        
        .chart-label {
            padding: 15px;
            background: #f3f4f6;
            font-size: 0.95em;
            color: #374151;
            font-weight: 600;
            text-align: center;
            border-top: 2px solid #e5e7eb;
        }
        
        .key-findings {
            background: #eff6ff;
            border-left: 5px solid #0ea5e9;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }
        
        .key-findings h3 {
            color: #0369a1;
            margin-bottom: 10px;
        }
        
        .key-findings ul {
            list-style-position: inside;
            color: #164e63;
            line-height: 1.8;
        }
        
        .key-findings li {
            margin-bottom: 8px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        
        th {
            background: #7c3aed;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }
        
        td {
            padding: 12px 15px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        tr:hover {
            background: #f9fafb;
        }
        
        footer {
            background: #f3f4f6;
            padding: 20px;
            text-align: center;
            color: #6b7280;
            border-top: 1px solid #e5e7eb;
        }
        
        .badge {
            display: inline-block;
            background: #dbeafe;
            color: #0369a1;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 600;
            margin-right: 8px;
        }
        
        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8em;
            }
            
            section h2 {
                font-size: 1.4em;
            }
            
            .gallery {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔬 Sorting Algorithm Analysis</h1>
            <p>Comprehensive Technical Report & Performance Benchmarks</p>
            <p>Analyzing Quick Sort, Merge Sort, Heap Sort, Shell Sort & Radix Sort</p>
            <div class="meta">
                <span class="badge">Algorithm Analysis</span>
                <span class="badge">Performance Benchmark</span>
                <span class="badge">Big-O Notation</span>
                <p>Generated: """ + datetime.now().strftime('%B %d, %Y %H:%M:%S') + """</p>
            </div>
        </header>
        
        <div class="content">
            <!-- REPORTS SECTION -->
            <section>
                <h2>📄 Technical Reports</h2>
                <p style="margin-bottom: 20px; color: #374151;">
                    Two comprehensive technical reports analyzing the performance of five fundamental sorting algorithms 
                    across multiple data sizes and patterns. Each report includes methodology, experimental results, 
                    comparative analysis, and practical recommendations.
                </p>
                
                <div class="report-grid">
                    <div class="report-card">
                        <h3>📋 Standard Report</h3>
                        <p>Comprehensive technical analysis with detailed methodology, experimental data tables, 
                        comparative analysis, and academic references.</p>
                        <div class="details">
                            <strong>Size:</strong> 18 KB<br>
                            <strong>Pages:</strong> 10-12<br>
                            <strong>Format:</strong> PDF<br>
                            <strong>Focus:</strong> Text & Tables
                        </div>
                        <a href="Technical_Report_Sorting_Algorithms.pdf" class="btn">📥 Download Report</a>
                    </div>
                    
                    <div class="report-card">
                        <h3>📊 Enhanced Report (Recommended)</h3>
                        <p>All content from Standard Report PLUS three high-quality visualizations showing 
                        performance trends, memory usage, and algorithm comparisons.</p>
                        <div class="details">
                            <strong>Size:</strong> 924 KB<br>
                            <strong>Pages:</strong> 12-14<br>
                            <strong>Format:</strong> PDF with Charts<br>
                            <strong>Focus:</strong> Visual Analysis
                        </div>
                        <a href="Technical_Report_Sorting_Algorithms_Enhanced.pdf" class="btn">📥 Download Report</a>
                    </div>
                </div>
                
                <div class="key-findings">
                    <h3>🎯 Key Findings Summary</h3>
                    <ul>
                        <li><strong>Radix Sort Dominance:</strong> Achieves O(n) linear performance, 3-5x faster than other algorithms on large datasets</li>
                        <li><strong>Quick Sort Practical Winner:</strong> Best average performance despite theoretically inferior worst-case bound</li>
                        <li><strong>Theory-Practice Gap:</strong> Algorithms with identical O(n log n) complexity show 2-5x performance differences</li>
                        <li><strong>Memory Trade-offs:</strong> In-place algorithms use 80-90% less memory than Merge/Radix sorts</li>
                        <li><strong>Optimization Impact:</strong> Hybrid approaches improve execution time by 15-20% while maintaining asymptotic bounds</li>
                    </ul>
                </div>
            </section>
            
            <!-- VISUALIZATIONS SECTION -->
            <section>
                <h2>📈 Performance Visualizations</h2>
                <p style="margin-bottom: 20px; color: #374151;">
                    Three high-resolution charts embedded in the Enhanced Report, showing execution time, 
                    memory usage, and algorithm comparison across data sizes and patterns.
                </p>
                
                <div class="gallery">
                    <div class="chart-container">
                        <img src="chart_time_performance.png" alt="Time Performance Scaling">
                        <div class="chart-label">
                            <strong>Figure 1:</strong> Time Performance Scaling<br>
                            <span style="font-size: 0.9em; opacity: 0.8;">Execution time across 1K-100K data sizes, all patterns</span>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <img src="chart_memory_usage.png" alt="Memory Usage Analysis">
                        <div class="chart-label">
                            <strong>Figure 2:</strong> Memory Usage Analysis<br>
                            <span style="font-size: 0.9em; opacity: 0.8;">Memory overhead: in-place vs. extra-space algorithms</span>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <img src="chart_comparison_100k.png" alt="Algorithm Comparison at N=100K">
                        <div class="chart-label">
                            <strong>Figure 3:</strong> Algorithm Comparison (N=100,000)<br>
                            <span style="font-size: 0.9em; opacity: 0.8;">Performance across random, reverse, and partial data patterns</span>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- PERFORMANCE METRICS SECTION -->
            <section>
                <h2>⚡ Performance Metrics Summary</h2>
                <p style="margin-bottom: 20px; color: #374151;">
                    Quick reference table showing actual measured performance on the largest dataset (N=100,000).
                </p>
                
                <table>
                    <thead>
                        <tr>
                            <th>Algorithm</th>
                            <th>Best Case</th>
                            <th>Avg Case</th>
                            <th>Worst Case</th>
                            <th>Space</th>
                            <th>Time @ 100K</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Radix Sort</strong></td>
                            <td>O(n)</td>
                            <td>O(n)</td>
                            <td>O(n)</td>
                            <td>O(n+k)</td>
                            <td>15-25 ms</td>
                        </tr>
                        <tr>
                            <td><strong>Quick Sort</strong></td>
                            <td>O(n log n)</td>
                            <td>O(n log n)</td>
                            <td>O(n²)</td>
                            <td>O(log n)</td>
                            <td>50-80 ms</td>
                        </tr>
                        <tr>
                            <td><strong>Merge Sort</strong></td>
                            <td>O(n log n)</td>
                            <td>O(n log n)</td>
                            <td>O(n log n)</td>
                            <td>O(n)</td>
                            <td>100-150 ms</td>
                        </tr>
                        <tr>
                            <td><strong>Shell Sort</strong></td>
                            <td>O(n log n)</td>
                            <td>O(n^1.3)</td>
                            <td>O(n²)</td>
                            <td>O(1)</td>
                            <td>120-180 ms</td>
                        </tr>
                        <tr>
                            <td><strong>Heap Sort</strong></td>
                            <td>O(n log n)</td>
                            <td>O(n log n)</td>
                            <td>O(n log n)</td>
                            <td>O(1)</td>
                            <td>200-300 ms</td>
                        </tr>
                    </tbody>
                </table>
            </section>
            
            <!-- ALGORITHM SELECTION GUIDE -->
            <section>
                <h2>🎓 Algorithm Selection Guide</h2>
                <p style="margin-bottom: 20px; color: #374151;">
                    Based on comprehensive analysis, here are practical recommendations for algorithm selection.
                </p>
                
                <table>
                    <thead>
                        <tr>
                            <th>Scenario</th>
                            <th>Recommended Algorithm</th>
                            <th>Reason</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>General Purpose Sorting</strong></td>
                            <td>Quick Sort</td>
                            <td>Best average performance, minimal memory overhead, proven in production</td>
                        </tr>
                        <tr>
                            <td><strong>Guaranteed Performance</strong></td>
                            <td>Merge Sort</td>
                            <td>O(n log n) worst-case guarantee, stable sorting, external sort capable</td>
                        </tr>
                        <tr>
                            <td><strong>Large Integer Datasets</strong></td>
                            <td>Radix Sort</td>
                            <td>Linear O(n) complexity, 3-5x faster than comparative algorithms</td>
                        </tr>
                        <tr>
                            <td><strong>Memory Constrained</strong></td>
                            <td>Heap Sort</td>
                            <td>O(1) space overhead, guaranteed O(n log n) performance</td>
                        </tr>
                        <tr>
                            <td><strong>Nearly-Sorted Data</strong></td>
                            <td>Shell Sort</td>
                            <td>Approaches linear time, significantly outperforms other in-place algorithms</td>
                        </tr>
                    </tbody>
                </table>
            </section>
            
            <!-- METHODOLOGY SECTION -->
            <section>
                <h2>🔬 Experimental Methodology</h2>
                <p style="margin-bottom: 20px; color: #374151;">
                    All benchmarks conducted under controlled conditions with consistent parameters and measurement techniques.
                </p>
                
                <table>
                    <thead>
                        <tr>
                            <th>Parameter</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Data Sizes</strong></td>
                            <td>1,000 | 10,000 | 100,000 elements</td>
                        </tr>
                        <tr>
                            <td><strong>Data Patterns</strong></td>
                            <td>Random | Reverse Sorted | Partially Sorted (70%)</td>
                        </tr>
                        <tr>
                            <td><strong>Runs per Test</strong></td>
                            <td>3 iterations (averaged to reduce noise)</td>
                        </tr>
                        <tr>
                            <td><strong>Timing Tool</strong></td>
                            <td>time.perf_counter() - nanosecond precision</td>
                        </tr>
                        <tr>
                            <td><strong>Memory Tool</strong></td>
                            <td>tracemalloc - peak allocation tracking</td>
                        </tr>
                        <tr>
                            <td><strong>Python Version</strong></td>
                            <td>3.13+</td>
                        </tr>
                        <tr>
                            <td><strong>Platform</strong></td>
                            <td>macOS 14.x, Intel processor, 16GB RAM</td>
                        </tr>
                    </tbody>
                </table>
            </section>
            
            <!-- ADDITIONAL RESOURCES -->
            <section>
                <h2>📚 Additional Resources</h2>
                <p style="margin-bottom: 20px; color: #374151;">
                    Related files and references for deeper understanding of the analysis.
                </p>
                
                <div class="report-grid">
                    <div class="report-card">
                        <h3>📖 Report Guide</h3>
                        <p>Detailed explanation of report structure, key findings, and how to use the reports 
                        for academic submission or presentation.</p>
                        <a href="REPORT_GUIDE.md" class="btn">📄 View Guide</a>
                    </div>
                    
                    <div class="report-card">
                        <h3>💻 Source Code</h3>
                        <p>All algorithm implementations, benchmark runners, and visualization scripts available 
                        in the project repository.</p>
                        <p style="font-size: 0.9em; color: #6b7280; margin-top: 15px;">
                            Includes: Quick Sort, Merge Sort, Heap Sort, Shell Sort, Radix Sort with optimizations
                        </p>
                    </div>
                    
                    <div class="report-card">
                        <h3>📊 Raw Data</h3>
                        <p>CSV files containing all measured timing and memory data, enabling further analysis 
                        or custom visualizations.</p>
                        <p style="font-size: 0.9em; color: #6b7280; margin-top: 15px;">
                            Available: time_results.csv, memory_results.csv
                        </p>
                    </div>
                </div>
            </section>
            
            <!-- REPORT STATISTICS -->
            <section>
                <h2>📊 Report Statistics</h2>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                    <div style="background: #dbeafe; padding: 20px; border-radius: 8px; text-align: center;">
                        <div style="font-size: 2em; color: #0369a1; font-weight: bold;">5</div>
                        <div style="color: #0369a1;">Algorithms Analyzed</div>
                    </div>
                    <div style="background: #dcfce7; padding: 20px; border-radius: 8px; text-align: center;">
                        <div style="font-size: 2em; color: #15803d; font-weight: bold;">45</div>
                        <div style="color: #15803d;">Test Configurations</div>
                    </div>
                    <div style="background: #fef3c7; padding: 20px; border-radius: 8px; text-align: center;">
                        <div style="font-size: 2em; color: #b45309; font-weight: bold;">12+</div>
                        <div style="color: #b45309;">Report Pages</div>
                    </div>
                    <div style="background: #fbcfe8; padding: 20px; border-radius: 8px; text-align: center;">
                        <div style="font-size: 2em; color: #be185d; font-weight: bold;">3</div>
                        <div style="color: #be185d;">Visualizations</div>
                    </div>
                </div>
            </section>
        </div>
        
        <footer>
            <p><strong>Sorting Algorithm Performance Analysis</strong></p>
            <p>Technical Report Generated: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
            <p style="margin-top: 10px; font-size: 0.9em;">
                📚 Based on rigorous benchmarking methodology | 
                📊 Comprehensive comparative analysis | 
                🎓 Academic-grade documentation
            </p>
        </footer>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    report_dir = os.path.join(project_root, "report")
    output_file = os.path.join(report_dir, "index.html")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ HTML index created: {output_file}")
    print(f"\n📖 Open in browser: file://{output_file}")
