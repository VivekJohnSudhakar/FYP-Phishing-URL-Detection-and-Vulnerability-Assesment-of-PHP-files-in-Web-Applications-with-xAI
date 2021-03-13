<html>
  <head>
    <title>Phishing Module</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="../js/script.js"></script>
    <script src="../index.js"></script>
    <link href="../css/style.css" rel="stylesheet">
	</head>
	<body>
		<div class="fixed-top">
			<nav class="navbar navbar-expand-lg navbar-dark mx-background-top-linear">
				<div class="container">
					<a class="navbar-brand" href="../mainpage.php" style="text-transform: uppercase;color:white">Detecting Phising URL's</a>
					<span style="font-size:20px;margin-top:8px;color:white;float:right">CEG,Anna University,Chennai</span>
				</div>
			</nav>
		</div>

		<div class="row">
			<div class="col-md-1">
			</div>
			<div class="col-md-5">
				<div class="panel panel-default">
					<div class="panel-heading text-center panel-relative"><b>Phishing Test</b></div>
					<div class="panel-body"></div>

					<form action="tempoutput.php" method="POST">	<!-- action should have the script where we send the url to -->
						<div class="row">
							<div class="col-md-3">
								<label class="home_label">Enter URL:</label>
							</div>
							<div class="col-md-8">
								<div class="input-group input-group-md">
									<span class="input-group-addon" id="sizing-addon1"><span class="glyphicon glyphicon-link"></span></span>
									<input type="text" name="url" class="form-control" id="url" placeholder="http://www.samplewebsite.com" aria-describedby="sizing-addon1" required>
								</div>
							</div>
						</div><br/>
						<div class="row">
							<div class="col-md-8">
							</div>
							<div class="col-md-11">
								<input type="submit" style="float:right" name="submit" class="btn btn-default"  value="Submit" id="redirect_submit">
							</div>

						</div>
					</form>
				</div>
			</div>
		</div>

		<!-- Modal -->
		<div class="modal fade" id="myModal" role="dialog">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal">&times;</button>
						<h4 class="modal-title">Analysis using Python</h4>
					</div>
					<div class="modal-body">
						<p style="color:red">Make the array copied to the script</p>
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
					</div>
				</div>
			</div>
		</div>
		<div class="col-md-1">
		</div>
		<div class="fixed-bottom">
			<nav class="navbar navbar-expand-lg navbar-dark mx-background-bottom-linear">
				<div class="container">
					<a class="navbar-brand" href="../mainpage.php" style="text-transform: uppercase;"> 2021 CEG</a>
				</div>
			</nav>
		</div>
	</body>
</html>
