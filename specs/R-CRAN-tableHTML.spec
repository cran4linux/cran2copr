%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tableHTML
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool to Create HTML Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jpeg 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-webshot 

%description
A tool to create and style HTML tables with CSS. These can be exported and
used in any application that accepts HTML (e.g. 'shiny', 'rmarkdown',
'PowerPoint'). It also provides functions to create CSS files (which also
work with shiny).

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
