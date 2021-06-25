%global __brp_check_rpaths %{nil}
%global packname  OenoKPM
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling the Kinetics of CO2 Production in Alcoholic Fermentation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-openxlsx 
Requires:         R-grDevices 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-extrafont 

%description
Developed to help researchers who need to model the kinetics of carbon
dioxide (CO2) production in alcoholic fermentation of wines, beers and
other fermented products. The following models are available for modeling
the CO2 production curve as a function of time: 5PL, Gompertz and 4PL.
This package has different functions, which applied can: perform the
modeling of the data obtained in the fermentation and return the
coefficients, analyze the model fit and return different statistical
metrics, and calculate the kinetic parameters: Maximum production of
carbon dioxide; Maximum rate of production of CO2; Moment in which maximum
fermentation rate occurs; Duration of the latency phase for CO2
production; CO2 Produced until Maximum fermentation rate occurs. In
addition, a function that generates graphs with the observed and predicted
data from the models, isolated and combined, is available. Gava, A.,
Borsato, D., & Ficagna, E. (2020). "Effect of mixture of fining agents on
the fermentation kinetics of base wine for sparkling wine production: Use
of methodology for modeling". <doi:10.1016/j.lwt.2020.109660>.

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
