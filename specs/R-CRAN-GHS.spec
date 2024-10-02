%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GHS
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Horseshoe MCMC Sampler Using Data Augmented Block Gibbs Sampler

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Draw posterior samples to estimate the precision matrix for multivariate
Gaussian data. Posterior means of the samples is the graphical horseshoe
estimate by Li, Bhadra and Craig(2017) <arXiv:1707.06661>. The function
uses matrix decomposition and variable change from the Bayesian graphical
lasso by Wang(2012) <doi:10.1214/12-BA729>, and the variable augmentation
for sampling under the horseshoe prior by Makalic and Schmidt(2016)
<arXiv:1508.03884>. Structure of the graphical horseshoe function was
inspired by the Bayesian graphical lasso function using blocked sampling,
authored by Wang(2012) <doi:10.1214/12-BA729>.

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
