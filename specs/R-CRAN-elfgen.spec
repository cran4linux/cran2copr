%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  elfgen
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Limit Function Model Generation and Analysis Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-sbtools 
BuildRequires:    R-CRAN-nhdplusTools 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-quantreg 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-testit 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-sbtools 
Requires:         R-CRAN-nhdplusTools 

%description
A toolset for generating Ecological Limit Function (ELF) models and
evaluating potential species loss resulting from flow change, based on the
'elfgen' framework. ELFs describe the relation between aquatic species
richness (fish or benthic macroinvertebrates) and stream size
characteristics (streamflow or drainage area). Journal publications are
available outlining framework methodology (Kleiner et al. (2020)
<doi:10.1111/1752-1688.12876>) and application (Rapp et al. (2020)
<doi:10.1111/1752-1688.12877>).

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
