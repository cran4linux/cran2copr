%global __brp_check_rpaths %{nil}
%global packname  landsepi
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Landscape Epidemiology and Evolution

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    gdal-devel >= 1.11.0
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats >= 3.0.2
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-CRAN-sp >= 1.0.17
BuildRequires:    R-CRAN-Rcpp >= 0.9.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-testthat 
Requires:         R-stats >= 3.0.2
Requires:         R-grDevices >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-CRAN-sp >= 1.0.17
Requires:         R-CRAN-Rcpp >= 0.9.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
A stochastic, spatially-explicit, demo-genetic model simulating the spread
and evolution of a plant pathogen in a heterogeneous landscape to assess
resistance deployment strategies. It is based on a spatial geometry for
describing the landscape and allocation of different cultivars, a
dispersal kernel for the dissemination of the pathogen, and a SEIR
('Susceptible-Exposed-Infectious-Removed’) structure with a discrete time
step. It provides a useful tool to assess the performance of a wide range
of deployment options with respect to their epidemiological, evolutionary
and economic outcomes. Loup Rimbaud, Julien Papaïx, Jean-François Rey,
Luke G Barrett, Peter H Thrall (2018) <doi:10.1371/journal.pcbi.1006067>.

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
