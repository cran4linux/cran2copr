%global packname  blrm
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Dose Escalation Design in Phase I Oncology Trial Using BayesianLogistic Regression Modeling

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-boot 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-reshape2 

%description
Plan dose escalation design using adaptive Bayesian logistic regression
modeling in Phase I oncology trial.

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
%{rlibdir}/%{packname}/INDEX
