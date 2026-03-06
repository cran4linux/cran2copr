%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiviz
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Data Visualisation Functions for Epidemiological Data Science Products

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ISOweek 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-slider 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ellmer 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-grDevices 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ISOweek 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-slider 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ellmer 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 

%description
Tools for making epidemiological reporting easier with consistent static
and dynamic charts and maps. Builds on 'ggplot2' for static visualizations
as described in Wickham (2016) <doi:10.1007/978-3-319-24277-4> and
'plotly' for interactive visualizations as described in Sievert (2020)
<doi:10.1201/9780429447273>.

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
