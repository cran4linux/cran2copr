%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slickR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Carousels with the 'JavaScript' 'Slick' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-htmltools 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-checkmate 

%description
Create and customize interactive carousels using the 'Slick' 'JavaScript'
library and the 'htmlwidgets' package. The carousels can contain plots
produced in R, images, 'iframes', videos and other 'htmlwidgets'.  These
carousels can be created directly from the R console, and viewed in the
'RStudio' internal viewer, in 'Shiny' apps and R Markdown documents.

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
