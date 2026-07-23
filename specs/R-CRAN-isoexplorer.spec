%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  isoexplorer
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          GUI Components to Explore Stable Isotope Data Files

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-isoreader2 >= 0.6.0
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-rlog 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-isoreader2 >= 0.6.0
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-rlog 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Provides graphical user interface components to explore stable isotope
data files using the 'isoreader2' package, including browsing,
visualizing, and exporting isotope data.

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
