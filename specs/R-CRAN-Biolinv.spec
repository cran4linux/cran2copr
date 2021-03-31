%global packname  Biolinv
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling and Forecasting Biological Invasions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 8.3
BuildRequires:    R-grDevices >= 3.3.2
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-raster >= 2.5.2
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-sp >= 1.2.4
BuildRequires:    R-CRAN-classInt >= 0.1.23
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.core 
Requires:         R-CRAN-fields >= 8.3
Requires:         R-grDevices >= 3.3.2
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-raster >= 2.5.2
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-sp >= 1.2.4
Requires:         R-CRAN-classInt >= 0.1.23
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.core 

%description
Analysing and forecasting biological invasions time series with a
stochastic approach that accounts for human-aided dispersal, habitat
suitability and provides estimates confidence level.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
