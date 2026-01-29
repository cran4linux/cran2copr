%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flexdashboard
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Markdown Format for Flexible Dashboards

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.8
BuildRequires:    R-CRAN-knitr >= 1.30
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-htmltools >= 0.5.1
BuildRequires:    R-CRAN-bslib >= 0.2.5
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sass 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-rmarkdown >= 2.8
Requires:         R-CRAN-knitr >= 1.30
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-htmltools >= 0.5.1
Requires:         R-CRAN-bslib >= 0.2.5
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sass 
Requires:         R-CRAN-scales 
Requires:         R-tools 
Requires:         R-utils 

%description
Format for converting an R Markdown document to a grid oriented dashboard.
The dashboard flexibly adapts the size of it's components to the
containing web page.

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
