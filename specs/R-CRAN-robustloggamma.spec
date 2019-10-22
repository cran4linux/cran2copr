%global packname  robustloggamma
%global packver   1.0-2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.1
Release:          1%{?dist}
Summary:          Robust Estimation of the Generalized log Gamma Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-RobustAFT >= 1.4.1
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-RobustAFT >= 1.4.1
Requires:         R-CRAN-robustbase 
Requires:         R-survival 
Requires:         R-CRAN-numDeriv 

%description
Robust estimation of the generalized log gamma model is provided using
Quantile Tau estimator, Weighted Likelihood estimator and Truncated
Maximum Likelihood estimator. Functions for regression and censored data
are also available.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHT
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
