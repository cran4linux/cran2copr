%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boot.pval
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrap p-Values

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-flextable 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-car 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-flextable 

%description
Computation of bootstrap p-values through inversion of confidence
intervals, including convenience functions for regression models.

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
