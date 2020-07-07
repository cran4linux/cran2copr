%global packname  fbRanks
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}
Summary:          Association Football (Soccer) Ranking via Poisson Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringr 

%description
This package uses time dependent Poisson regression and a record of goals
scored in matches to rank teams via estimated attack and defense
strengths.  The statistical model is based on Dixon and Coles (1997)
Modeling Association Football Scores and Inefficiencies in the Football
Betting Market, Applied Statistics, Volume 46, Issue 2, 265-280.  The
package has a some webscrapers to assist in the development and updating
of a match database.  If the match database contains unconnected clusters
(i.e. sets of teams that have only played each other and not played teams
from other sets), each cluster is ranked separately relative to the median
team strength in the cluster.  The package contains functions for
predicting and simulating tournaments and leagues from estimated models.
The package allows fitting via the glm(), speedglm(), and glmnet()
functions.  The latter allows fast and efficient fitting of very large
numbers of teams.  The fitting algorithm will analyze the match data and
determine which teams form a cluster (a set of teams where there is a path
of matches connecting every team) and fit each cluster separately.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
