%global __brp_check_rpaths %{nil}
%global packname  wavScalogram
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wavelet Scalogram Tools for Time Series Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-zoo 

%description
Provides scalogram based wavelet tools for time series analysis: wavelet
power spectrum, scalogram, windowed scalogram, windowed scalogram
difference (see Bolos et al. (2017) <doi:10.1016/j.amc.2017.05.046>),
scale index and windowed scale index (Benitez et al. (2010)
<doi:10.1016/j.camwa.2010.05.010>).

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
