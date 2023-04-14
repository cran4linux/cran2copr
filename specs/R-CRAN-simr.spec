%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simr
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Power Analysis for Generalised Linear Mixed Models by Simulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lmerTest >= 3.0.0
BuildRequires:    R-CRAN-lme4 >= 1.1.16
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-lmerTest >= 3.0.0
Requires:         R-CRAN-lme4 >= 1.1.16
Requires:         R-CRAN-binom 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-pbkrtest 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RLRsim 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-car 

%description
Calculate power for generalised linear mixed models, using simulation.
Designed to work with models fit using the 'lme4' package. Described in
Green and MacLeod, 2016 <doi:10.1111/2041-210X.12504>.

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
