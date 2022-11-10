%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  idopNetwork
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Cartographic Tool to Chart Spatial Microbial Interaction Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-orthopolynom 
Requires:         R-parallel 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-patchwork 

%description
Most existing approaches for network reconstruction can only infer an
overall network and, also, fail to capture a complete set of network
properties. To address these issues, a new model has been developed, which
converts static data into their 'dynamic' form. 'idopNetwork' is an 'R'
interface to this model, it can inferring informative, dynamic,
omnidirectional and personalized networks. For more information on
functional clustering part, see Kim et al. (2008)
<doi:10.1534/genetics.108.093690>, Wang et al. (2011)
<doi:10.1093/bib/bbr032>. For more information on our model, see Chen et
al. (2019) <doi:10.1038/s41540-019-0116-1>, and Cao et al. (2022)
<doi:10.1080/19490976.2022.2106103>.

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
