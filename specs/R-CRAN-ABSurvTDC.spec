%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ABSurvTDC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Analysis using Time Dependent Covariate for Animal Breeding

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-readxl 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-readxl 

%description
Survival analysis is employed to model the time it takes for events to
occur. Survival model examines the relationship between survival and one
or more predictors, usually termed covariates in the survival-analysis
literature. To this end, Cox-proportional (Cox-PH) hazard rate model
introduced in a seminal paper by Cox (1972)
<doi:10.1111/j.2517-6161.1972.tb00899.x>, is a broadly applicable and the
most widely used method of survival analysis. This package can be used to
estimate the effect of fixed and time-dependent covariates and also to
compute the survival probabilities of the lactation of dairy animal. This
package has been developed using algorithm of Klein and Moeschberger
(2003) <doi:10.1007/b97377>.

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
