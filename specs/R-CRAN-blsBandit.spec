%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blsBandit
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Viewer for Bureau of Labor Statistics Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.10.2
BuildRequires:    R-CRAN-RSQLite >= 2.2.16
BuildRequires:    R-CRAN-jsonlite >= 1.8.4
BuildRequires:    R-CRAN-zoo >= 1.8.12
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-DBI >= 1.1.3
Requires:         R-CRAN-plotly >= 4.10.2
Requires:         R-CRAN-RSQLite >= 2.2.16
Requires:         R-CRAN-jsonlite >= 1.8.4
Requires:         R-CRAN-zoo >= 1.8.12
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-DBI >= 1.1.3

%description
Allows users to easily visualize data from the BLS (United States of
America Bureau of Labor Statistics) <https://www.bls.gov>. Currently
unemployment data series U1-U6 are available. Not affiliated with the
Bureau of Labor Statistics or United States Government.

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
