%global packname  RcppNLoptExample
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          'Rcpp' Package Illustrating Header-Only Access to 'NLopt'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-nloptr >= 1.2.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-nloptr >= 1.2.0
Requires:         R-CRAN-Rcpp 

%description
An example package which shows use of 'NLopt' functionality from C++ via
'Rcpp' without requiring linking, and relying just on 'nloptr' thanks to
the exporting API added there by Jelmer Ypma. This package is a fully
functioning, updated, and expanded version of the initial example by
Julien Chiquet at <https://github.com/jchiquet/RcppArmadilloNLoptExample>
also containing a large earlier pull request of mine.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
