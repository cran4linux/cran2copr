%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SAMBA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Selection and Misclassification Bias Adjustment for Logistic Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-survey 

%description
Health research using data from electronic health records (EHR) has gained
popularity, but misclassification of EHR-derived disease status and lack
of representativeness of the study sample can result in substantial bias
in effect estimates and can impact power and type I error for association
tests. Here, the assumed target of inference is the relationship between
binary disease status and predictors modeled using a logistic regression
model. 'SAMBA' implements several methods for obtaining bias-corrected
point estimates along with valid standard errors as proposed in Beesley
and Mukherjee (2020) <doi:10.1111/biom.13400>, Biometrics.

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
