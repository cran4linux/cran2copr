%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pillar
%global packver   1.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          Coloured Formatting for Columns

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 2.3.0
BuildRequires:    R-CRAN-utf8 >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 2.3.0
Requires:         R-CRAN-utf8 >= 1.1.0
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-utils 

%description
Provides 'pillar' and 'colonnade' generics designed for formatting columns
of data using the full range of colours provided by modern terminals.

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
