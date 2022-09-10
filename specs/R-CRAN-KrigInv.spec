%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KrigInv
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Kriging-Based Inversion for Deterministic and Noisy Computer Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-anMC 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-anMC 
Requires:         R-CRAN-mvtnorm 

%description
Criteria and algorithms for sequentially estimating level sets of a
multivariate numerical function, possibly observed with noise.

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
