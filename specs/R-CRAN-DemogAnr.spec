%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DemogAnr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Demographic Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Tool for demographic modeling and analysis, combining stochastic
simulation-based projections with classic demographic methods. Provides
utilities for disaggregating population data using Karup-King
interpolation, fitting Brass relational logit models, calculating
fertility and mortality metrics, building life tables, and performing
hierarchical subnational population projections. Relational life table
estimation and interpolation methods are described in Brass (1975)
"Methods for Estimating Fertility and Mortality from Limited and Defective
Data", Preston et al. (2001, ISBN:978-0631226161) "Demography: Measuring
and Modeling Population Processes", Siegel and Swanson (2004,
ISBN:978-0126419559) "The Methods and Materials of Demography", and
Raftery et al. (2012) "Bayesian probabilistic population projections for
all countries" <doi:10.1073/pnas.1211452109>.

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
