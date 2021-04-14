%global packname  pillar
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Coloured Formatting for Columns

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-utf8 >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-vctrs >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-utils 
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-utf8 >= 1.1.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-vctrs >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-fansi 
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
