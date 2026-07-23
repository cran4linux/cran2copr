%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cdtmbnma
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Component, Dose, and Time Network Meta-Analysis with Dose-Dependent Interactions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-posterior 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Bayesian component model-based network meta-analysis for treatment
combinations with explicit component dose-response and dose-dependent
interaction surfaces. The main interface fits single-timepoint arm-level
networks with continuous or binary outcomes, any number of components,
additive, bilinear, or saturating pairwise interactions, study-level
random effects, and prediction at unobserved dose combinations. A
stage-one longitudinal interface fits a two-component exponential
time-course model with a bilinear interaction on the asymptote. Estimation
uses 'Stan' through 'cmdstanr' or 'rstan'. Methods are described in Welton
et al. (2009) <doi:10.1093/aje/kwp014>, Mawdsley et al. (2016)
<doi:10.1002/psp4.12091>, Wicha et al. (2017)
<doi:10.1038/s41467-017-01929-y>, and Pedder et al. (2019)
<doi:10.1002/jrsm.1351>.

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
