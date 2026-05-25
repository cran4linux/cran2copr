%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hbsaems
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Bayesian Area-Level Small Area Estimation Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-mice >= 3.14.0
BuildRequires:    R-CRAN-rstantools >= 2.4.0
BuildRequires:    R-CRAN-brms >= 2.18.0
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-mice >= 3.14.0
Requires:         R-CRAN-rstantools >= 2.4.0
Requires:         R-CRAN-brms >= 2.18.0
Requires:         R-CRAN-coda >= 0.19.4
Requires:         R-stats 
Requires:         R-utils 

%description
Fits area-level Hierarchical Bayesian Small Area Estimation models. The
methodological foundation follows the standard area-level Small Area
Estimation literature, primarily Rao and Molina (2015, ISBN:
9781118735787) <doi:10.1002/9781118735855>, while computational
implementation is adapted to the parameterisation and prior-specification
conventions of the 'brms' package <doi:10.18637/jss.v080.i01>, which
targets the Stan back-end. Supports a principled Bayesian workflow
<doi:10.48550/arXiv.2011.01808>, with prior predictive checks, convergence
diagnostics, model comparison, spatial random effects, custom
distributions, missing-data handling, and a bilingual 'shiny' application
for non-programmer analysts.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
