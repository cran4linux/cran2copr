%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gt
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Create Presentation-Ready Display Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-magrittr >= 2.0.2
BuildRequires:    R-CRAN-commonmark >= 1.8.1
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-fs >= 1.6.1
BuildRequires:    R-CRAN-htmlwidgets >= 1.6.1
BuildRequires:    R-CRAN-markdown >= 1.5
BuildRequires:    R-CRAN-xml2 >= 1.3.3
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-bitops >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-htmltools >= 0.5.4
BuildRequires:    R-CRAN-sass >= 0.4.5
BuildRequires:    R-CRAN-reactable >= 0.4.3
BuildRequires:    R-CRAN-bigD >= 0.2
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-CRAN-juicyjuice >= 0.1.0
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-magrittr >= 2.0.2
Requires:         R-CRAN-commonmark >= 1.8.1
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-fs >= 1.6.1
Requires:         R-CRAN-htmlwidgets >= 1.6.1
Requires:         R-CRAN-markdown >= 1.5
Requires:         R-CRAN-xml2 >= 1.3.3
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-bitops >= 1.0.7
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-htmltools >= 0.5.4
Requires:         R-CRAN-sass >= 0.4.5
Requires:         R-CRAN-reactable >= 0.4.3
Requires:         R-CRAN-bigD >= 0.2
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-CRAN-juicyjuice >= 0.1.0

%description
Build display tables from tabular data with an easy-to-use set of
functions. With its progressive approach, we can construct display tables
with a cohesive set of table parts. Table values can be formatted using
any of the included formatting functions. Footnotes and cell styles can be
precisely added through a location targeting system. The way in which 'gt'
handles things for you means that you don't often have to worry about the
fine details.

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
