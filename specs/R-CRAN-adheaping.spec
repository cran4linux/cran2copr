%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adheaping
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Characteristic-Function De-Heaping Density Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Tuning-free kernel density estimation for heaped and rounded data using a
characteristic-function theory of heaping. Rounding to a grid is
convolution with a box followed by lattice sampling, so the density is
recovered by deconvolving the known box and tapering against a data-driven
noise floor. Provides a box-deconvolution de-heaping estimator, a
superposition variant, and a single combined estimator selected by a
band-capacity gate; blind grid, heaped-fraction, and mixed-grain readers;
and a spectral higher-order comb detector. Faithful base-R replicas of the
Heitjan-Rubin multiple-imputation and measurement-error deconvolution
methods are included for comparison, and the 'Kernelheaping' stochastic
expectation-maximization estimator is used when installed.

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
