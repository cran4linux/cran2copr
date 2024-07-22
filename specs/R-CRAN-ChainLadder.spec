%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ChainLadder
%global packver   0.2.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.19
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods and Models for Claims Reserving in General Insurance

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cplm >= 0.7.3
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tweedie 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-cplm >= 0.7.3
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-actuar 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-grid 
Requires:         R-CRAN-tweedie 
Requires:         R-utils 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 

%description
Various statistical methods and models which are typically used for the
estimation of outstanding claims reserves in general insurance, including
those to estimate the claims development result as required under Solvency
II.

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
