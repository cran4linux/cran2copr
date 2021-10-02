%global __brp_check_rpaths %{nil}
%global packname  plotDK
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plot Summary Statistics as Choropleth Maps of Danish Administrative Areas

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 

%description
Provides a ggplot2 front end to plot summary statistics on danish
provinces, regions, municipalities, and zipcodes. The needed geoms of each
of the four levels are inherent in the package, thus making these types of
plots easy for the user. This is essentially an updated port of the
previously available 'mapDK' package by Sebastian Barfort.

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
