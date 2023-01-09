%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gfonts
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Offline 'Google' Fonts for 'Markdown' and 'Shiny'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-crayon 
Requires:         R-utils 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-crayon 

%description
Download 'Google' fonts and generate 'CSS' to use in 'rmarkdown' documents
and 'shiny' applications. Some popular fonts are included and ready to
use.

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
