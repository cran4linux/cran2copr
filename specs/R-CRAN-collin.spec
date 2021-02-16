%global packname  collin
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Effects of Collinearity in Distributed Lag and Other Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dlnm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-dlnm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-VGAM 

%description
Visual tool to assessing whether the results of a study could be driven by
collinearity. The methods are described in Basagana X, Barrera-Gomez J
(2021) "Visualizing the effects of collinearity in distributed lag
models". International Journal of Epidemiology (under review).

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
