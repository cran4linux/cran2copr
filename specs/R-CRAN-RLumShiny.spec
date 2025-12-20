%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RLumShiny
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          'Shiny' Applications for the R Package 'Luminescence'

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.2.3
BuildRequires:    R-CRAN-markdown >= 2.0
BuildRequires:    R-CRAN-knitr >= 1.50
BuildRequires:    R-CRAN-readxl >= 1.4.5
BuildRequires:    R-CRAN-data.table >= 1.17.6
BuildRequires:    R-CRAN-shiny >= 1.11.1
BuildRequires:    R-CRAN-Luminescence >= 1.1.2
BuildRequires:    R-CRAN-googleVis >= 0.7.3
BuildRequires:    R-CRAN-shinydashboard >= 0.7.3
BuildRequires:    R-CRAN-DT >= 0.34
BuildRequires:    R-CRAN-rhandsontable >= 0.3.8
BuildRequires:    R-CRAN-RCarb >= 0.1.6
Requires:         R-CRAN-leaflet >= 2.2.3
Requires:         R-CRAN-markdown >= 2.0
Requires:         R-CRAN-knitr >= 1.50
Requires:         R-CRAN-readxl >= 1.4.5
Requires:         R-CRAN-data.table >= 1.17.6
Requires:         R-CRAN-shiny >= 1.11.1
Requires:         R-CRAN-Luminescence >= 1.1.2
Requires:         R-CRAN-googleVis >= 0.7.3
Requires:         R-CRAN-shinydashboard >= 0.7.3
Requires:         R-CRAN-DT >= 0.34
Requires:         R-CRAN-rhandsontable >= 0.3.8
Requires:         R-CRAN-RCarb >= 0.1.6

%description
A collection of 'shiny' applications for the R package 'Luminescence'.
These mainly, but not exclusively, include applications for plotting
chronometric data from e.g. luminescence or radiocarbon dating. It further
provides access to bootstraps tooltip and popover functionality and
contains the 'jscolor.js' library with a custom 'shiny' output binding.

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
