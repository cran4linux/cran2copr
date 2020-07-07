%global packname  flexsurv
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Flexible Parametric Survival and Multi-State Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-mstate >= 0.2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-muhaz 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-mstate >= 0.2.10
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-survival 
Requires:         R-CRAN-muhaz 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 

%description
Flexible parametric models for time-to-event data, including the
Royston-Parmar spline model, generalized gamma and generalized F
distributions.  Any user-defined parametric distribution can be fitted,
given at least an R function defining the probability density or hazard.
There are also tools for fitting and predicting from fully parametric
multi-state models.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
