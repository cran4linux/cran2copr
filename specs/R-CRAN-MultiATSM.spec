%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiATSM
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multicountry Term Structure of Interest Rates Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hablar 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hablar 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-pracma 

%description
Package for estimating, analyzing, and forecasting multi-country
macro-finance affine term structure models (ATSMs). All setups build on
the single-country unspanned macroeconomic risk framework from Joslin,
Priebsch, and Singleton (2014, JF) <doi:10.1111/jofi.12131>. Multicountry
extensions by Jotikasthira, Le, and Lundblad (2015, JFE)
<doi:10.1016/j.jfineco.2014.09.004>, Candelon and Moura (2023, EM)
<doi:10.1016/j.econmod.2023.106453>, and Candelon and Moura (2024, JFEC)
<doi:10.1093/jjfinec/nbae008> are also available. The package also
provides tools for bias correction as in Bauer Rudebusch and Wu (2012,
JBES) <doi:10.1080/07350015.2012.693855>, bootstrap analysis, and several
graphical/numerical outputs.

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
