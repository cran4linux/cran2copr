%global __brp_check_rpaths %{nil}
%global packname  gratis
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generating Time Series with Diverse and Controllable Characteristics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tsfeatures 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tsibble 
Requires:         R-CRAN-tsfeatures 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tsibble 

%description
Generates time series based on mixture autoregressive models.
Kang,Y.,Hyndman,R.,Li,F.(2020)<doi:10.1002/sam.11461>.

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
