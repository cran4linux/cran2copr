%global packname  ftnonpar
%global packver   0.1-88
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.88
Release:          2%{?dist}
Summary:          Features and Strings for Nonparametric Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
The package contains R-functions to perform the methods in nonparametric
regression and density estimation, described in Davies, P. L. and Kovac,
A. (2001) Local Extremes, Runs, Strings and Multiresolution (with
discussion) Annals of Statistics. 29. p1-65 Davies, P. L. and Kovac, A.
(2004) Densities, Spectral Densities and Modality Annals of Statistics.
Annals of Statistics. 32. p1093-1136 Kovac, A. (2006) Smooth functions and
local extreme values. Computational Statistics and Data Analysis (to
appear) D"umbgen, L. and Kovac, A. (2006) Extensions of smoothing via
taut strings Davies, P. L. (1995) Data features. Statistica Neerlandica
49,185-245.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
