%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  acpbvar
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Structural VARs with Asymmetric Conjugate Priors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Implements Bayesian estimation of structural Vector Autoregressions in the
asymmetric A-form of Chan (2022) <doi:10.3982/QE1381>, with an asymmetric
Minnesota prior whose own-lag and cross-lag hyperparameters are selected
by empirical Bayes via the closed-form marginal likelihood. Exact
equation-by-equation posterior simulation in the structural form
(independent Normal-Inverse-Gamma draws) provides posterior draws of the
reduced-form parameters; structural identification through sign
restrictions follows the algorithm of Rubio-Ramirez, Waggoner and Zha
(2010) <doi:10.1111/j.1467-937X.2009.00578.x>. Impulse responses,
posterior bands, and acceptance diagnostics are computed from the accepted
draws.

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
