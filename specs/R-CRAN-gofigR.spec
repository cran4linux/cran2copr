%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gofigR
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Client for 'GoFigr.io'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-qrcode 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-scriptName 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-qrcode 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-scriptName 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 

%description
Integrates with your 'RMarkdown' documents to automatically publish
figures to the <https://GoFigr.io> service. Supports both 'knitr' and
interactive execution within 'RStudio'.

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
