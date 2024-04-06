%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TimeVizPro
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Data Explorer: Visualize and Forecast with 'TimeVizPro'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-sparkline 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-sparkline 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-dplyr 

%description
Unleash the power of time-series data visualization with ease using our
package. Designed with simplicity in mind, it offers three key features
through the 'shiny' package output. The first tab shows time- series
charts with forecasts, allowing users to visualize trends and changes
effortlessly. The second one displays Averages per country presented in
tables with accompanying sparklines, providing a quick and attractive
overview of the data. The last tab presents A customizable world map
colored based on user-defined variables for any chosen number of
countries, offering an advanced visual approach to understanding
geographical data distributions. This package operates with just a few
simple arguments, enabling users to conduct sophisticated analyses without
the need for complex programming skills. Transform your time-series data
analysis experience with our user-friendly tool.

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
