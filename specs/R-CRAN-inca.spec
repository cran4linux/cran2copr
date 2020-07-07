%global packname  inca
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}
Summary:          Integer Calibration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-stats 
Requires:         R-Matrix 

%description
Specific functions are provided for rounding real weights to integers and
performing an integer programming algorithm for calibration problems. They
are useful for census-weights adjustments, or for performing linear
regression with integer parameters. This research was supported in part by
the U.S. Department of Agriculture, National Agriculture Statistics
Service. The findings and conclusions in this publication are those of the
authors and should not be construed to represent any official USDA, or US
Government determination or policy.

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
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/INSTALL.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
