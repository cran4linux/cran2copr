%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evreg
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Evidential Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-evclust 
BuildRequires:    R-stats 
Requires:         R-CRAN-evclust 
Requires:         R-stats 

%description
An implementation of the 'Evidential Neural Network for Regression' model
recently introduced in Denoeux (2023) <doi:10.36227/techrxiv.21791831.v1>.
In this model, prediction uncertainty is quantified by Gaussian random
fuzzy numbers as introduced in Denoeux (2023)
<doi:10.1016/j.fss.2022.06.004>. The package contains functions for
training the network, tuning hyperparameters by cross-validation or the
hold-out method, and making predictions. It also contains utilities for
making calculations with Gaussian random fuzzy numbers (such as, e.g.,
computing the degrees of belief and plausibility of an interval, or
combining Gaussian random fuzzy numbers).

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
