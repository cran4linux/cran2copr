%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hyreg2
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Latent Classes on a Mixture of Continuous and Dichotomous Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
The hybrid model likelihood as described by Ramos-Goñi et al. (2017)
<doi:10.1097/MLR.0000000000000283> is implemented and and embedded in a
latent class framework. The package is based on 'flexmix' and among others
contains an M-step-driver as described by Leisch (2004)
<doi:10.18637/jss.v011.i08>. Users can, for example, estimate latent
classes for EQ-5D value sets and address preference heterogeneity. Both
uncensored and censored data are supported. Furthermore,
heteroscedasticity can be taken into account. It is possible to control
for different covariates on the continuous and dichotomous data and start
values can differ between the expected latent classes.

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
