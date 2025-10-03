%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rshift
%global packver   3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Paleoecology Functions for Regime Shift Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cargo
BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 

%description
Contains a variety of functions, based around regime shift analysis of
paleoecological data. Citations: Rodionov() from Rodionov (2004)
<doi:10.1029/2004GL019448> Lanzante() from Lanzante (1996)
<doi:10.1002/(SICI)1097-0088(199611)16:11%%3C1197::AID-JOC89%%3E3.0.CO;2-L>
Hellinger_trans from Numerical Ecology, Legendre & Legendre (ISBN
9780444538680) rolling_autoc from Liu, Gao & Wang (2018)
<doi:10.1016/j.scitotenv.2018.06.276> Sample data sets lake_data &
lake_RSI processed from Bush, Silman & Urrego (2004)
<doi:10.1126/science.1090795> Sample data set January_PDO from NOAA:
<https://www.ncei.noaa.gov/access/monitoring/pdo/>.

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
