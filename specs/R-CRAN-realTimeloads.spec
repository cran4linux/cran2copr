%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  realTimeloads
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyte Flux and Load from Estimates of Concentration and Discharge

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TideHarmonics 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-graphics 
Requires:         R-CRAN-imputeTS 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-signal 
Requires:         R-stats 
Requires:         R-CRAN-TideHarmonics 
Requires:         R-utils 

%description
Flux (mass per unit time) and Load (mass) are computed from timeseries
estimates of analyte concentration and discharge. Concentration timeseries
are computed from regression between surrogate and user-provided analyte.
Uncertainty in calculations is estimated using bootstrap resampling. Code
for the processing of acoustic backscatter from horizontally profiling
acoustic Doppler current profilers is provided. All methods detailed in
Livsey et al (2020) <doi:10.1007/s12237-020-00734-z>, Livsey et al (2023)
<doi:10.1029/2022WR033982>, and references therein.

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
