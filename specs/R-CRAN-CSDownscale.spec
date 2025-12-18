%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CSDownscale
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Downscaling of Climate Predictions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CSTools 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-multiApply 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-s2dv 
BuildRequires:    R-CRAN-ClimProjDiags 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-easyVerification 
Requires:         R-CRAN-CSTools 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-multiApply 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-s2dv 
Requires:         R-CRAN-ClimProjDiags 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-easyVerification 

%description
Statistical downscaling and bias correction of climate predictions. It
includes implementations of commonly used methods such as Analogs, Linear
Regression, Logistic Regression, and Bias Correction techniques, as well
as interpolation functions for regridding and point-based applications. It
facilitates the production of high-resolution and local-scale climate
information from coarse-scale predictions, which is essential for impact
analyses. The package can be applied in a wide range of sectors and
studies, including agriculture, water management, energy, heatwaves, and
other climate-sensitive applications. The package was developed within the
framework of the European Union Horizon Europe projects Impetus4Change
(101081555) and ASPECT (101081460), the Wellcome Trust supported HARMONIZE
project (224694/Z/21/Z), and the Spanish national project BOREAS
(PID2022-140673OA-I00). Implements the methods described in Duzenli et al.
(2024) <doi:10.5194/egusphere-egu24-19420>.

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
