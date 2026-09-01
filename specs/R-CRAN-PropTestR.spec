%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PropTestR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Two-Proportion Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ratesci >= 1.1.0
BuildRequires:    R-CRAN-DescTools >= 0.99.60
BuildRequires:    R-stats 
Requires:         R-CRAN-ratesci >= 1.1.0
Requires:         R-CRAN-DescTools >= 0.99.60
Requires:         R-stats 

%description
Unified methods for comparing two independent or paired proportions.
Provides classical, exact, score-based, non-inferiority, equivalence,
effect-size, confidence-interval, and stratified procedures with
standardized publication-ready output. Farrington-Manning inference is
supported through established score-based methods described by Farrington
and Manning (1990) <doi:10.2307/2532443> and implemented through
'ratesci', while additional established methods are provided through
'DescTools' and base R.

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
