%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  moose
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mean Squared Out-of-Sample Error Projection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Projects mean squared out-of-sample error for a linear regression based
upon the methodology developed in Rohlfs (2022)
<doi:10.48550/arXiv.2209.01493>.  It consumes as inputs the lm object from
an estimated OLS regression (based on the "training sample") and a
data.frame of out-of-sample cases (the "test sample") that have
non-missing values for the same predictors. The test sample may or may not
include data on the outcome variable; if it does, that variable is not
used. The aim of the exercise is to project what what mean squared
out-of-sample error can be expected given the predictor values supplied in
the test sample. Output consists of a list of three elements: the
projected mean squared out-of-sample error, the projected out-of-sample
R-squared, and a vector of out-of-sample "hat" or "leverage" values, as
defined in the paper.

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
