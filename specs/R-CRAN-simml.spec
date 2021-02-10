%global packname  simml
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Single-Index Models with Multiple-Links

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-mgcv 

%description
A major challenge in estimating treatment decision rules from a randomized
clinical trial dataset with covariates measured at baseline lies in
detecting relatively small treatment effect modification-related
variability (i.e., the treatment-by-covariates interaction effects on
treatment outcomes) against a relatively large non-treatment-related
variability (i.e., the main effects of covariates on treatment outcomes).
The class of Single-Index Models with Multiple-Links is a novel
single-index model specifically designed to estimate a single-index (a
linear combination) of the covariates associated with the treatment effect
modification-related variability, while allowing a nonlinear association
with the treatment outcomes via flexible link functions. The models
provide a flexible regression approach to developing treatment decision
rules based on patients' data measured at baseline. We refer to Park,
Petkova, Tarpey, and Ogden (2020) <doi:10.1016/j.jspi.2019.05.008> and
Park, Petkova, Tarpey, and Ogden (2020) <doi:10.1111/biom.13320> (that
allows an unspecified X main effect) for detail of the method. The main
function of this package is simml().

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
