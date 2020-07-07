%global packname  nicheROVER
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          (Niche) (R)egion and Niche (Over)lap Metrics forMultidimensional Ecological Niches

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.9.0
Requires:         R-core >= 1.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
This package uses a probabilistic method to calculate niche regions and
pairwise niche overlap using multidimensional niche indicator data (e.g.,
stable isotopes, environmental variables, etc.). The niche region is
defined as the joint probability density function of the multidimensional
niche indicators at a user-defined probability alpha (e.g., 95%).
Uncertainty is accounted for in a Bayesian framework, and the method can
be extended to three or more indicator dimensions.  It provides
directional estimates of niche overlap, accounts for species-specific
distributions in multivariate niche space, and produces unique and
consistent bivariate projections of the multivariate niche region.  A
forthcoming article by Swanson et al. (Ecology, 2014) provides a detailed
description of the methodology.  See the package vignette for a worked
example using fish stable isotope data.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
