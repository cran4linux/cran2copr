%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GIMMEgVAR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Group Iterative Multiple Model Estimation with 'graphicalVAR'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-graphicalVAR 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-graphicalVAR 
Requires:         R-CRAN-here 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-png 

%description
Data-driven approach for arriving at person-specific time series models
from within a Graphical Vector Autoregression (VAR) framework. The method
first identifies which relations replicate across the majority of
individuals to detect signal from noise. These group-level relations are
then used as a foundation for starting the search for person-specific (or
individual-level) relations. All estimates are obtained uniquely for each
individual in the final models. The method for the 'graphicalVAR' approach
is found in Epskamp, Waldorp, Mottus & Borsboom (2018)
<doi:10.1080/00273171.2018.1454823>.

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
