from flask import Flask, render_template, jsonify
import subprocess
import os
import signal
import time

app = Flask(__name__)
process = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Run", methods=["POST"])
def run_model():
    global process
    if process is None:
        try:
            # Get the absolute path to your project directory
            project_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Change to the project directory
            os.chdir(project_dir)
            
            print(f"Running from: {project_dir}")
            print("Files in directory:", os.listdir(project_dir))
            
            # Run the object detection script
            process = subprocess.Popen(
                ["python", "object-ident.py"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a moment to see if it starts successfully
            time.sleep(3)
            
            # Check if process is still running
            if process.poll() is None:
                return jsonify({"message": "Camera started, object detection running!", "status": "running"})
            else:
                # Try to get error output
                try:
                    stdout, stderr = process.communicate(timeout=1)
                    error_msg = stderr if stderr else stdout if stdout else "Unknown error - process exited immediately"
                except:
                    error_msg = "Could not retrieve error message"
                
                process = None
                print(f"Error starting process: {error_msg}")
                return jsonify({"message": f"Failed to start: {error_msg}", "status": "error"})
                
        except Exception as e:
            error_msg = f"Error starting process: {str(e)}"
            print(error_msg)
            return jsonify({"message": error_msg, "status": "error"})
    else:
        return jsonify({"message": "Already running!", "status": "running"})

@app.route("/Stop", methods=["POST"])
def stop_model():
    global process
    if process is not None:
        try:
            # Try to terminate gracefully
            process.terminate()
            
            # Wait a moment
            time.sleep(1)
            
            # Force kill if still running
            if process.poll() is None:
                process.kill()
            
            process.wait(timeout=2)
            process = None
            return jsonify({"message": "Camera stopped.", "status": "stopped"})
        except Exception as e:
            return jsonify({"message": f"Error stopping process: {str(e)}", "status": "error"})
    else:
        return jsonify({"message": "Nothing is running.", "status": "stopped"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)