%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  googletraffic
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Google Traffic

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-googleway 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-plotwidgets 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-webshot2 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ColorNameR 
BuildRequires:    R-CRAN-schemr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-googleway 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-plotwidgets 
Requires:         R-CRAN-png 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-webshot2 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ColorNameR 
Requires:         R-CRAN-schemr 

%description
Create geographically referenced traffic data from the Google Maps
JavaScript API
<https://developers.google.com/maps/documentation/javascript/examples/layer-traffic>.

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
