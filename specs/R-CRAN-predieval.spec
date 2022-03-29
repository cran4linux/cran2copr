%global __brp_check_rpaths %{nil}
%global packname  predieval
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Performance of Prediction Models for Predicting Patient-Level Treatment Benefit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-Matching >= 4.9.11
BuildRequires:    R-CRAN-Hmisc >= 4.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-Matching >= 4.9.11
Requires:         R-CRAN-Hmisc >= 4.6.0
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-stats 

%description
Methods for assessing the performance of a prediction model with respect
to identifying patient-level treatment benefit. All methods are applicable
for continuous and binary outcomes, and for any type of statistical or
machine-learning prediction model as long as it uses baseline covariates
to predict outcomes under treatment and control.

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
