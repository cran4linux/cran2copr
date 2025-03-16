%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fmx
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Finite Mixture Parametrization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-param2moment 
BuildRequires:    R-CRAN-TukeyGH77 
Requires:         R-methods 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-param2moment 
Requires:         R-CRAN-TukeyGH77 

%description
A parametrization framework for finite mixture distribution using S4
objects. Density, cumulative density, quantile and simulation functions
are defined. Currently normal, Tukey g-&-h, skew-normal and skew-t
distributions are well tested. The gamma, negative binomial distributions
are being tested.

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
