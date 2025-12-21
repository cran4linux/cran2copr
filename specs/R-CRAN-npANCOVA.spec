%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npANCOVA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric ANCOVA Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Nonparametric methods for analysis of covariance (ANCOVA) are
distribution-free and provide a flexible statistical framework for
situations where the assumptions of parametric ANCOVA are violated or when
the response variable is ordinal. This package implements several
well-known nonparametric ANCOVA procedures, including Quade, Puri and Sen,
McSweeney and Porter, Burnett and Barr, Hettmansperger and McKean,
Shirley, and Puri-Sen-Harwell-Serlin. The package provides user-friendly
functions to apply these methods in practice. These methods are described
in Olejnik et al. (1985) <doi:10.1177/0193841X8500900104> and Harwell et
al. (1988) <doi:10.1037/0033-2909.104.2.268>.

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
