%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wdiexplorer
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Explore World Development Indicators Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-WDI 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fabletools 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggnewscale 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-WDI 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fabletools 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggnewscale 

%description
Provides a workflow for exploring World Development Indicators (WDI)
country-level panel data. It downloads WDI data using the 'WDI' package
and computes diagnostic indices that capture the temporal behaviour of the
data by incorporating the grouping structure of the data. The set of
diagnostic indices implemented includes variation features, trend and
shape features, and sequential temporal features. This method is described
in Akinfenwa, Cahill, and Hurley (2025) "'wdiexplorer': An R package
Designed for Exploratory Analysis of World Development Indicators (WDI)
Data" <doi:10.48550/arXiv.2511.07027>. We adapt the clustering diagnostics
and visualisation methodology described in Rousseeuw (1987)
<doi:10.1016/0377-0427(87)90125-7> and selected time series features from
Hyndman and Athanasopoulos (2021) "Forecasting: Principles and Practice"
<https://otexts.com/fpp3/>.

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
