%global packname  MapGAM
%global packver   1.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Mapping Smoothed Effect Estimates from Individual-Level Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-gam 
Requires:         R-survival 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-colorspace 

%description
Contains functions for mapping odds ratios, hazard ratios, or other effect
estimates using individual-level data such as case-control study data,
using generalized additive models (GAMs) or Cox models for smoothing with
a two-dimensional predictor (e.g., geolocation or exposure to chemical
mixtures) while adjusting linearly for confounding variables, using
methods described by Kelsall and Diggle (1998), Webster at al. (2006), and
Bai et al. (submitted).  Includes convenient functions for mapping point
estimates and confidence intervals, efficient control sampling, and
permutation tests for the null hypothesis that the two-dimensional
predictor is not associated with the outcome variable (adjusting for
confounders).

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
