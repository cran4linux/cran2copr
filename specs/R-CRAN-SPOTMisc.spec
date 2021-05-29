%global packname  SPOTMisc
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Misc Extensions for the 'SPOT' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-benchmarkme 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-emoa 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-SimInf 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-SPOT 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mlr 
Requires:         R-CRAN-benchmarkme 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-emoa 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggsci 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-SimInf 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-SPOT 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mlr 

%description
Implements additional models, simulation tools, and interfaces as
extensions to 'SPOT'. It provides tools for interfacing 'mlr', for
performing Markov chain simulations, and for sensitivity analysis based on
sequential bifurcation methods as described in Bettonvil and Kleijnen
(1996). Furthermore, additional plotting functions for output from 'SPOT'
runs are implemented. Bartz-Beielstein T, Lasarczyk C W G, Preuss M (2005)
<doi:10.1109/CEC.2005.1554761>. Bartz-Beielstein T, Zaefferer M, Rehbach F
(2021) <arXiv:1712.04076>. Bettonvil, B, Kleijnen JPC (1996)
<doi:10.1016/S0377-2217(96)00156-7>.

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
