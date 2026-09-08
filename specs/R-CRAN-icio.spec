%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icio
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Global Value Chain Decomposition of Inter-Country Input-Output Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixStats 

%description
Four global value chain (GVC) decompositions of gross exports from
inter-country input-output tables are implemented. The Leontief
decomposition derives the value added origin of exports by country and
industry, as in Hummels, Ishii and Yi (2001)
<doi:10.1016/S0022-1996(00)00093-3>. The Koopman, Wang and Wei (2014)
<doi:10.1257/aer.104.2.459> decomposition splits country-level exports
into 9 value added components, and the Wang, Wei and Zhu (2013)
<doi:10.3386/w19677> decomposition splits bilateral exports into 16 value
added components. The Borin and Mancini (2019)
<doi:10.1596/1813-9450-8804> decomposition splits country-, sector- or
bilateral-level exports into up to 13 value added and GVC components, and
also provides a corrected version of the (biased) Koopman-Wang-Wei
decomposition. It is the recommended method and reproduces the 'icio'
command for 'Stata' described in Belotti, Borin and Mancini (2021)
<doi:10.1177/1536867X211045573>.

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
