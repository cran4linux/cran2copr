%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gratis
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Generating Time Series with Diverse and Controllable Characteristics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.16
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tsfeatures 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-forecast >= 8.16
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tsfeatures 
Requires:         R-CRAN-tsibble 
Requires:         R-utils 

%description
Generates synthetic time series based on various univariate time series
models including MAR and ARIMA processes. Kang, Y., Hyndman, R.J., Li,
F.(2020) <doi:10.1002/sam.11461>.

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
