%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nnspat
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nearest Neighbor Methods for Spatial Patterns

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pcds 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-pcds 

%description
Contains the functions for testing the spatial patterns (of segregation,
spatial symmetry, association, disease clustering, species correspondence,
and reflexivity) based on nearest neighbor relations, especially using
contingency tables such as nearest neighbor contingency tables (Ceyhan
(2010) <doi:10.1007/s10651-008-0104-x> and Ceyhan (2017)
<doi:10.1016/j.jkss.2016.10.002> and references therein), nearest neighbor
symmetry contingency tables (Ceyhan (2014) <doi:10.1155/2014/698296>),
species correspondence contingency tables and reflexivity contingency
tables (Ceyhan (2018) <doi:10.2436/20.8080.02.72> for two (or higher)
dimensional data. The package also contains functions for generating
patterns of segregation, association, uniformity in a multi-class setting
(Ceyhan (2014) <doi:10.1007/s00477-013-0824-9>), and various non-random
labeling patterns for disease clustering in two dimensional cases (Ceyhan
(2014) <doi:10.1002/sim.6053>), and for visualization of all these
patterns for the two dimensional data. The tests are usually (asymptotic)
normal z-tests or chi-square tests.

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
