%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brclimr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fetch Zonal Statistics of Weather Indicators for Brazilian Municipalities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-lobstr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-lobstr 
Requires:         R-CRAN-magrittr 

%description
Fetches zonal statistics from weather indicators that were calculated for
each municipality in Brazil using data from the BR-DWGD and TerraClimate
projects. Zonal statistics such as mean, maximum, minimum, standard
deviation, and sum were computed by taking into account the data cells
that intersect the boundaries of each municipality and stored in Parquet
files. This procedure was carried out for all Brazilian municipalities,
and for all available dates, for every indicator available in the weather
products (BR-DWGD and TerraClimate projects). This package queries on-line
the already calculated statistics on the Parquet files and returns
easy-to-use data.frames.

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
