%global __brp_check_rpaths %{nil}
%global packname  simlandr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Landscape Construction for Dynamical Systems

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-rlang 

%description
A toolbox for constructing potential landscapes for dynamical systems
using Monte-Carlo simulation. The method is based on the generalized
potential landscape function by Wang et al. (2008)
<doi:10.1073/pnas.0800579105> (also see Zhou & Li, 2016
<doi:10.1063/1.4943096> for further mathematical discussions). Especially
suitable for psychological formal models.

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
