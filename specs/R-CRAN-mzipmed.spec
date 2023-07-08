%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mzipmed
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mediation using MZIP Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-sandwich 

%description
We implement functions allowing for mediation analysis to be performed in
cases where the mediator is a count variable with excess zeroes. First a
function is provided allowing users to perform analysis for zero-inflated
count variables using the marginalized zero-inflated Poisson (MZIP) model
(Long et al. 2014 <DOI:10.1002/sim.6293>). Using the counterfactual
approach to mediation and MZIP we can obtain natural direct and indirect
effects for the overall population. Using delta method processes variance
estimation can be performed instantaneously. Alternatively, bootstrap
standard errors can be used. We also provide functions for cases with
exposure-mediator interactions with four-way decomposition of total
effect.

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
