%global __brp_check_rpaths %{nil}
%global packname  basictabler
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Rich Tables for Output to 'HTML'/'Excel'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-htmlwidgets >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-htmlwidgets >= 0.8
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-htmltools >= 0.3.5

%description
Easily create tables from data frames/matrices.  Create/manipulate tables
row-by-row, column-by-column or cell-by-cell. Use common
formatting/styling to output rich tables as 'HTML', 'HTML widgets' or to
'Excel'.

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
