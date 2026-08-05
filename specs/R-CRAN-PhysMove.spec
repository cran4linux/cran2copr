%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PhysMove
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Quantifying Animal Movement and Space-Use Patterns with Statistical Physics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-rootSolve >= 1.8.2.3
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-broom >= 1.0.5
BuildRequires:    R-CRAN-sf >= 1.0.16
BuildRequires:    R-CRAN-poweRlaw >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-rootSolve >= 1.8.2.3
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-RColorBrewer >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-broom >= 1.0.5
Requires:         R-CRAN-sf >= 1.0.16
Requires:         R-CRAN-poweRlaw >= 1.0.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides tools to analyse animal movement and space-use patterns from
telemetry data using methods derived from statistical physics. Methods
span displacement-based approaches, distribution fitting, space-use
metrics (including the influence of correlations on space-use),
network-based community detection, and measures of entropy and
predictability. The package enables characterisation of these patterns
across spatial and temporal scales, including variation within and among
individuals (inter- and intraspecific analyses). Outputs include
interpretable metrics and visualisations to support ecological analysis
and the investigation of fundamental movement processes. For applications
of these methods in ecological studies see Rodríguez et al. (2017)
<doi:10.1038/s41598-017-00165-0> and Sequeira et al. (2018)
<doi:10.1073/pnas.1716137115>.

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
