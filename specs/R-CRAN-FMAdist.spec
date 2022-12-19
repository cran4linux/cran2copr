%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FMAdist
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Frequentist Model Averaging Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quadprog 

%description
Creation of an input model (fitted distribution) via the frequentist model
averaging (FMA) approach and generate random-variates from the
distribution specified by "myfit" which is the fitted input model via the
FMA approach. See W. X. Jiang and B. L. Nelson (2018), "Better Input
Modeling via Model Averaging," Proceedings of the 2018 Winter Simulation
Conference, IEEE Press, 1575-1586.

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
