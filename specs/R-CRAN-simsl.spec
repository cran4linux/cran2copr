%global packname  simsl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Single-Index Models with a Surface-Link

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
Requires:         R-mgcv 
Requires:         R-stats 

%description
An implementation of a single-index regression for optimizing
individualized dose rules from an observational study. To model
interaction effects between baseline covariates and a treatment variable
defined on a continuum, we employ two-dimensional penalized spline
regression on an index-treatment domain, where the index is defined as a
linear combination of the covariates (a single-index). An unspecified main
effect for the covariates is allowed. A unique contribution of this work
is in the parsimonious single-index parametrization specifically defined
for the interaction effect term. We refer to Park, Petkova, Tarpey, and
Ogden (2020) <doi:10.1016/j.jspi.2019.05.008> (for the case of a discrete
treatment) and Park, Petkova, Tarpey, and Ogden (2019) "A single-index
model with a surface-link for optimizing individualized dose rules"
(pre-print) for detail of the method. The main function of this package is
simsl().

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
