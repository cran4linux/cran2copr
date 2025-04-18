%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bench
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          High Precision Timing of R Expressions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-pillar >= 1.10.1
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-profmem >= 0.6.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-pillar >= 1.10.1
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-profmem >= 0.6.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools to accurately benchmark and analyze execution times for R
expressions.

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
