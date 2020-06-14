%global packname  cope
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Coverage Probability Excursion (CoPE) Sets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.34
BuildRequires:    R-CRAN-fields >= 7.1
BuildRequires:    R-nlme >= 3.1.122
BuildRequires:    R-CRAN-maps >= 2.3.7
BuildRequires:    R-CRAN-abind >= 1.4.3
BuildRequires:    R-Matrix >= 1.2.3
BuildRequires:    R-CRAN-mvtnorm >= 1.0.0
Requires:         R-MASS >= 7.3.34
Requires:         R-CRAN-fields >= 7.1
Requires:         R-nlme >= 3.1.122
Requires:         R-CRAN-maps >= 2.3.7
Requires:         R-CRAN-abind >= 1.4.3
Requires:         R-Matrix >= 1.2.3
Requires:         R-CRAN-mvtnorm >= 1.0.0

%description
Provides functions to compute and plot Coverage Probability Excursion
(CoPE) sets for real valued functions on a 2-dimensional domain. CoPE sets
are obtained from repeated noisy observations of the function on the
entire domain. They are designed to bound the excursion set of the target
function at a given level from above and below with a predefined
probability. The target function can be a parameter in spatially-indexed
linear regression. Support by NIH grant R01 CA157528 is gratefully
acknowledged.

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
