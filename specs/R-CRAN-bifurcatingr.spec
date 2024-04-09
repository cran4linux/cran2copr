%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bifurcatingr
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bifurcating Autoregressive Models

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fMultivar >= 4021
Requires:         R-CRAN-fMultivar >= 4021

%description
Estimation of bifurcating autoregressive models of any order, p, BAR(p) as
well as several types of bias correction for the least squares estimators
of the autoregressive parameters as described in Zhou and Basawa (2005)
<doi:10.1016/j.spl.2005.04.024> and Elbayoumi and Mostafa (2020)
<doi:10.1002/sta4.342>. Currently, the bias correction methods supported
include bootstrap (single, double and fast-double) bias correction and
linear-bias-function-based bias correction. Functions for generating and
plotting bifurcating autoregressive data from any BAR(p) model are also
included. This new version includes calculating several type of
bias-corrected and -uncorrected confidence intervals for the least squares
estimators of the autoregressive parameters as described in Elbayoumi and
Mostafa (2023) <doi:10.6339/23-JDS1092>.

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
