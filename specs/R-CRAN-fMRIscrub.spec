%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fMRIscrub
%global packver   0.14.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.5
Release:          1%{?dist}%{?buildtag}
Summary:          Scrubbing and Other Data Cleaning Routines for fMRI

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fMRItools >= 0.2.2
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-pesel 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gamlss 
Requires:         R-CRAN-fMRItools >= 0.2.2
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-pesel 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-CRAN-expm 
Requires:         R-utils 
Requires:         R-CRAN-gamlss 

%description
Data-driven fMRI denoising with projection scrubbing (Pham et al (2022)
<doi:10.1016/j.neuroimage.2023.119972>). Also includes routines for DVARS
(Derivatives VARianceS) (Afyouni and Nichols (2018)
<doi:10.1016/j.neuroimage.2017.12.098>), motion scrubbing (Power et al
(2012) <doi:10.1016/j.neuroimage.2011.10.018>), aCompCor (anatomical
Components Correction) (Muschelli et al (2014)
<doi:10.1016/j.neuroimage.2014.03.028>), detrending, and nuisance
regression. Projection scrubbing is also applicable to other outlier
detection tasks involving high-dimensional data.

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
