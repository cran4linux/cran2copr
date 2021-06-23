%global __brp_check_rpaths %{nil}
%global packname  INLAMSM
%global packver   0.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Spatial Models with 'INLA'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 

%description
Implementation of several multivariate areal latent effects for 'INLA'
using the 'rgeneric' latent effect (Palmí-Perales et al., 2019,
<doi:10.18637/jss.v098.i02>). The 'INLA' package can be downloaded from
<https://www.r-inla.org>. In particular, the package includes latent
effects ready to use for several multivariate spatial models: intrinsic
CAR, proper CAR and the M-model (Botella-Rocamora et al., 2015,
<doi:10.1002/sim.6423>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
