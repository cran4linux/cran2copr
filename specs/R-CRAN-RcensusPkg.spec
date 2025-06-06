%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcensusPkg
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Access US Census Bureau Survey and Geographic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-jsonlite >= 1.8.9
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-data.table >= 1.16.4
BuildRequires:    R-CRAN-httr2 >= 1.1.2
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-sf >= 1.0.19
BuildRequires:    R-CRAN-downloader >= 0.4.1
BuildRequires:    R-CRAN-gtable >= 0.3.6
BuildRequires:    R-CRAN-RplotterPkg >= 0.1.3
BuildRequires:    R-CRAN-ggplotify >= 0.1.2
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-jsonlite >= 1.8.9
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-data.table >= 1.16.4
Requires:         R-CRAN-httr2 >= 1.1.2
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-sf >= 1.0.19
Requires:         R-CRAN-downloader >= 0.4.1
Requires:         R-CRAN-gtable >= 0.3.6
Requires:         R-CRAN-RplotterPkg >= 0.1.3
Requires:         R-CRAN-ggplotify >= 0.1.2

%description
The key function 'get_vintage_data()' returns a dataframe and is the
window into the Census Bureau API requiring just a dataset name,
vintage(year), and vector of variable names for survey
estimates/percentages. Other functions assist in searching for available
datasets, geographies, group/variable concepts of interest.  Also provided
are functions to access and layer (via standard piping) displayable
geometries for the US, states, counties, blocks/tracts, roads, landmarks,
places, and bodies of water. Joining survey data with many of the geometry
functions is built-in to produce choropleth maps.

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
