%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  betareg
%global packver   3.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Beta Regression

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-flexmix 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-flexmix 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-modeltools 
Requires:         R-CRAN-sandwich 

%description
Beta regression for modeling beta-distributed dependent variables on the
open unit interval (0, 1), e.g., rates and proportions, see Cribari-Neto
and Zeileis (2010) <doi:10.18637/jss.v034.i02>. Moreover, extended-support
beta regression models can accommodate dependent variables with boundary
observations at 0 and/or 1, see Kosmidis and Zeileis (2024)
<doi:10.48550/arXiv.2409.07233>. For the classical beta regression model,
alternative specifications are provided: Bias-corrected and bias-reduced
estimation, finite mixture models, and recursive partitioning for beta
regression, see Grün, Kosmidis, and Zeileis (2012)
<doi:10.18637/jss.v048.i11>.

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
