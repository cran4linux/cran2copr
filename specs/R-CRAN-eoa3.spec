%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eoa3
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Wildlife Mortality Estimator for Low Fatality Rates and Imperfect Detection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-GenEst 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-GenEst 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-VGAM 

%description
Evidence of Absence software (EoA) is a user-friendly application for
estimating bird and bat fatalities at wind farms and designing search
protocols. The software is particularly useful in addressing whether the
number of fatalities has exceeded a given threshold and what search
parameters are needed to give assurance that thresholds were not exceeded.
The models are applicable even when zero carcasses have been found in
searches, following Huso et al. (2015) <doi:10.1890/14-0764.1>, Dalthorp
et al. (2017) <doi:10.3133/ds1055>, and Dalthorp and Huso (2015)
<doi:10.3133/ofr20151227>.

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
