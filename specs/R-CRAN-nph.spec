%global packname  nph
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}
Summary:          Planning and Analysing Survival Studies under Non-ProportionalHazards

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 

%description
Piecewise constant hazard functions are used to flexibly model survival
distributions with non-proportional hazards and to simulate data from the
specified distributions. Also, a function to calculate weighted log-rank
tests for the comparison of two hazard functions is included. Finally, a
function to calculate a test using the maximum of a set of test statistics
from weighted log-rank tests is provided. This test utilizes the
asymptotic multivariate normal joint distribution of the separate test
statistics. The correlation is estimated from the data.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
