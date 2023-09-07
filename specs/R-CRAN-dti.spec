%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dti
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Diffusion Weighted Imaging (DWI) Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-aws >= 2.4.1
BuildRequires:    R-CRAN-awsMethods >= 1.1.1
BuildRequires:    R-CRAN-adimpro >= 0.9
BuildRequires:    R-CRAN-oro.nifti >= 0.3.9
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-oro.dicom 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-aws >= 2.4.1
Requires:         R-CRAN-awsMethods >= 1.1.1
Requires:         R-CRAN-adimpro >= 0.9
Requires:         R-CRAN-oro.nifti >= 0.3.9
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-oro.dicom 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-quadprog 

%description
Diffusion Weighted Imaging (DWI) is a Magnetic Resonance Imaging modality,
that measures diffusion of water in tissues like the human brain. The
package contains R-functions to process diffusion-weighted data. The
functionality includes diffusion tensor imaging (DTI), diffusion kurtosis
imaging (DKI), modeling for high angular resolution diffusion weighted
imaging (HARDI) using Q-ball-reconstruction and tensor mixture models,
several methods for structural adaptive smoothing including POAS and
msPOAS, and a streamline fiber tracking for tensor and tensor mixture
models. The package provides functionality to manipulate and visualize
results in 2D and 3D.

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
