%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rempsyc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Convenience Functions for Psychology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-flextable >= 0.7.1
BuildRequires:    R-CRAN-insight >= 0.18.4
BuildRequires:    R-CRAN-performance >= 0.10.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-effectsize 
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-flextable >= 0.7.1
Requires:         R-CRAN-insight >= 0.18.4
Requires:         R-CRAN-performance >= 0.10.0
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-effectsize 

%description
Make your workflow faster and easier. Easily customizable plots (via
'ggplot2'), nice APA tables (following the style of the *American
Psychological Association*) exportable to Word (via 'flextable'), easily
run statistical tests or check assumptions, and automatize various other
tasks.

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
