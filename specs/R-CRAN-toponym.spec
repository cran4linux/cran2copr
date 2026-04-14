%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toponym
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze and Visualize Toponyms

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-geodata 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-geodata 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
A tool to analyze and visualize toponym distributions. This package is
intended as an interface to the GeoNames data. A regular expression
filters data and in a second step a map is created displaying all
locations in the filtered data set. The functions make data and plots
available for further analysis—either within R or in a chosen directory.
Users can select regions within countries, provide coordinates to define
regions, or specify a region within the package to restrict the data
selection to that region or compare regions with the remainder of
countries. This package relies on the R packages 'geodata' for map data
and 'ggplot2' for plotting purposes. For more information on the study of
toponyms, see Wichmann & Chevallier (2025) <doi:10.5195/names.2025.2616>.

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
