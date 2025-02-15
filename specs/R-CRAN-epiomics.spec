%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiomics
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Omics Data in Observational Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-qgcomp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-qgcomp 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
A collection of fast and flexible functions for analyzing omics data in
observational studies. Multiple different approaches for integrating
multiple environmental/genetic factors, omics data, and/or phenotype data
are implemented. This includes functions for performing omics wide
association studies with one or more variables of interest as the exposure
or outcome; a function for performing a meet in the middle analysis for
linking exposures, omics, and outcomes (as described by Chadeau-Hyam et
al., (2010) <doi:10.3109/1354750X.2010.533285>); and a function for
performing a mixtures analysis across all omics features using
quantile-based g-Computation (as described by Keil et al., (2019)
<doi:10.1289/EHP5838>).

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
