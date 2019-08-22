%global packname  augSIMEX
%global packver   3.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.7.3
Release:          1%{?dist}
Summary:          Analysis of Data with Mixed Measurement Error andMisclassification in Covariates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-nleqslv 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-MASS 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-nleqslv 

%description
Implementation of the augmented Simulation-Extrapolation (SIMEX) algorithm
proposed by Yi et al. (2015) <doi:10.1080/01621459.2014.922777> for
analyzing the data with mixed measurement error and misclassification. The
main function provides a similar summary output as that of glm() function.
Both parametric and empirical SIMEX are considered in the package.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
