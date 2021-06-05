%global packname  factormodel
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Model Estimation Using Proxy Variables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-gtools 

%description
Functions to estimate a factor model using discrete and continuous proxy
variables. The function 'dproxyme' estimates a factor model of discrete
proxy variables using an EM algorithm (Dempster, Laird, Rubin (1977)
<doi:10.1111/j.2517-6161.1977.tb01600.x>; Hu (2008)
<doi:10.1016/j.jeconom.2007.12.001>; Hu(2017)
<doi:10.1016/j.jeconom.2017.06.002> ). The function 'cproxyme' estimates a
linear factor model (Cunha, Heckman, and Schennach (2010)
<doi:10.3982/ECTA6551>).

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
