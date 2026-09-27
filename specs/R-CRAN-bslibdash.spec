%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bslibdash
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          'Bootstrap' 5 Dashboard Framework for 'shiny' Apps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-bslib >= 0.6.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-sass 
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-bslib >= 0.6.0
Requires:         R-utils 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-sass 

%description
Provides a dashboard layer for 'shiny' applications built on 'bslib' and
'Bootstrap' 5. Includes a dashboard page shell, sidebar navigation, cards,
value boxes, header drop-down menus and feedback components that inherit
the active 'bslib' theme and follow 'Bootstrap' design patterns. Function
names mirror those of the 'shinydashboard' package wherever the underlying
concepts are shared, allowing existing applications to migrate with
minimal changes.

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
