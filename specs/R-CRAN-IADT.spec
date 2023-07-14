%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IADT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interaction Difference Test for Prediction Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mvnfast 
Requires:         R-CRAN-Rmpfr 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mvnfast 

%description
Provides functions to conduct a model-agnostic asymptotic hypothesis test
for the identification of interaction effects in black-box machine
learning models. The null hypothesis assumes that a given set of
covariates does not contribute to interaction effects in the prediction
model. The test statistic is based on the difference of variances of
partial dependence functions (Friedman (2008) <doi:10.1214/07-AOAS148> and
Welchowski (2022) <doi:10.1007/s13253-021-00479-7>) with respect to the
original black-box predictions and the predictions under the null
hypothesis. The hypothesis test can be applied to any black-box prediction
model, and the null hypothesis of the test can be flexibly specified
according to the research question of interest. Furthermore, the test is
computationally fast to apply as the null distribution does not require
resampling or refitting black-box prediction models.

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
