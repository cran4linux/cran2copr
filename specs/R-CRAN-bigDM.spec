%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigDM
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Scalable Bayesian Disease Mapping Models for High-Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-geos 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlist 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-geos 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spatialreg 
Requires:         R-CRAN-spdep 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlist 

%description
Implements several spatial and spatio-temporal scalable disease mapping
models for high-dimensional count data using the INLA technique for
approximate Bayesian inference in latent Gaussian models (Orozco-Acosta et
al., 2021 <doi:10.1016/j.spasta.2021.100496>; Orozco-Acosta et al., 2023
<doi:10.1016/j.cmpb.2023.107403> and Vicente et al., 2023
<doi:10.1007/s11222-023-10263-x>). The creation and develpment of this
package has been supported by Project MTM2017-82553-R (AEI/FEDER, UE) and
Project PID2020-113125RB-I00/MCIN/AEI/10.13039/501100011033. It has also
been partially funded by the Public University of Navarra (project
PJUPNA2001).

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
