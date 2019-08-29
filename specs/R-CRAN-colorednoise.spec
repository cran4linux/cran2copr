%global packname  colorednoise
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Simulate Temporally Autocorrelated Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.3
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.3
Requires:         R-CRAN-purrr >= 0.2.3

%description
Temporally autocorrelated populations are correlated in their vital rates
(growth, death, etc.) from year to year. It is very common for
populations, whether they be bacteria, plants, or humans, to be temporally
autocorrelated. This poses a challenge for stochastic population modeling,
because a temporally correlated population will behave differently from an
uncorrelated one. This package provides tools for simulating populations
with white noise (no temporal autocorrelation), red noise (positive
temporal autocorrelation), and blue noise (negative temporal
autocorrelation).  The algebraic formulation for autocorrelated noise
comes from Ruokolainen et al. (2009) <doi:10.1016/j.tree.2009.04.009>.
Models for unstructured populations and for structured populations (matrix
models) are available.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
