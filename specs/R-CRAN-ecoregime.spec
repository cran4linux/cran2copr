%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecoregime
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Ecological Dynamic Regimes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ecotraj >= 1.1.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ecotraj >= 1.1.1
Requires:         R-CRAN-ape 
Requires:         R-CRAN-data.table 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-smacof 
Requires:         R-stats 
Requires:         R-CRAN-stringr 

%description
A toolbox for implementing the Ecological Dynamic Regime framework
(Sánchez-Pinillos et al., 2023 <doi:10.1002/ecm.1589>) to characterize and
compare groups of ecological trajectories in multidimensional spaces
defined by state variables. The package includes the RETRA-EDR algorithm
to identify representative trajectories, functions to generate, summarize,
and visualize representative trajectories, and several metrics to quantify
the distribution and heterogeneity of trajectories in an ecological
dynamic regime and quantify the dissimilarity between two or more
ecological dynamic regimes. The package also includes a set of functions
to assess ecological resilience based on ecological dynamic regimes
(Sánchez-Pinillos et al., 2024 <doi:10.1016/j.biocon.2023.110409>).

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
