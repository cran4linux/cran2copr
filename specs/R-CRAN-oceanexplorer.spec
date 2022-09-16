%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oceanexplorer
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Explore Our Planet's Oceans with NOAA

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maps >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-RNetCDF >= 2.6.1
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-fs >= 1.5.2
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-sf >= 1.0.5
BuildRequires:    R-CRAN-stars >= 0.5.5
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-shinyFeedback >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-bslib >= 0.3.1
BuildRequires:    R-CRAN-ncmeta >= 0.3.0
BuildRequires:    R-CRAN-DT >= 0.20
BuildRequires:    R-CRAN-waiter >= 0.2.5
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-CRAN-thematic >= 0.1.2.1
BuildRequires:    R-CRAN-miniUI >= 0.1.1.1
Requires:         R-CRAN-maps >= 3.4.0
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-RNetCDF >= 2.6.1
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-fs >= 1.5.2
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-sf >= 1.0.5
Requires:         R-CRAN-stars >= 0.5.5
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-shinyFeedback >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-bslib >= 0.3.1
Requires:         R-CRAN-ncmeta >= 0.3.0
Requires:         R-CRAN-DT >= 0.20
Requires:         R-CRAN-waiter >= 0.2.5
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-CRAN-thematic >= 0.1.2.1
Requires:         R-CRAN-miniUI >= 0.1.1.1

%description
Provides tools for easy exploration of the world ocean atlas of the US
agency National Oceanic and Atmospheric Administration (NOAA). It includes
functions to extract NetCDF data from the repository and code to visualize
several physical and chemical parameters of the ocean. A Shiny app further
allows interactive exploration of the data. The methods for data
collecting and quality checks are described in several papers, which can
be found here: <https://www.ncei.noaa.gov/products/world-ocean-atlas>.

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
