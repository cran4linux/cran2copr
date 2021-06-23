%global __brp_check_rpaths %{nil}
%global packname  CPAT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Change Point Analysis Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-stats >= 3.2
BuildRequires:    R-utils >= 3.2
BuildRequires:    R-grDevices >= 3.2
BuildRequires:    R-methods >= 3.2
BuildRequires:    R-CRAN-Rdpack >= 0.9
BuildRequires:    R-CRAN-purrr >= 0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats >= 3.2
Requires:         R-utils >= 3.2
Requires:         R-grDevices >= 3.2
Requires:         R-methods >= 3.2
Requires:         R-CRAN-Rdpack >= 0.9
Requires:         R-CRAN-purrr >= 0.2
Requires:         R-CRAN-Rcpp >= 0.12

%description
Implements several statistical tests for structural change, specifically
the tests featured in Horváth, Rice and Miller (in press): CUSUM (with
weighted/trimmed variants), Darling-Erdös, Hidalgo-Seo, Andrews, and the
new Rényi-type test.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
