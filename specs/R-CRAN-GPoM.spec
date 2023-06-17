%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPoM
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Polynomial Modelling

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-float 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-float 

%description
Platform dedicated to the Global Modelling technique. Its aim is to obtain
ordinary differential equations of polynomial form directly from time
series. It can be applied to single or multiple time series under various
conditions of noise, time series lengths, sampling, etc. This platform is
developped at the Centre d'Etudes Spatiales de la Biosphere (CESBIO), UMR
5126 UPS/CNRS/CNES/IRD, 18 av. Edouard Belin, 31401 TOULOUSE, FRANCE. The
developments were funded by the French program Les Enveloppes Fluides et
l'Environnement (LEFE, MANU, projets GloMo, SpatioGloMo and MoMu). The
French program Defi InFiNiTi (CNRS) and PNTS are also acknowledged
(projects Crops'IChaos and Musc & SlowFast). The method is described in
the article : Mangiarotti S. and Huc M. (2019) <doi:10.1063/1.5081448>.

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
