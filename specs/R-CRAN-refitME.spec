%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refitME
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Measurement Error Modelling using MCEM

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-VGAMdata 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-VGAMdata 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 

%description
Fits measurement error models using Monte Carlo Expectation Maximization
(MCEM). For specific details on the methodology, see: Greg C. G. Wei &
Martin A. Tanner (1990) A Monte Carlo Implementation of the EM Algorithm
and the Poor Man's Data Augmentation Algorithms, Journal of the American
Statistical Association, 85:411, 699-704
<doi:10.1080/01621459.1990.10474930> For more examples on measurement
error modelling using MCEM, see the 'RMarkdown' vignette: "'refitME'
R-package tutorial".

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
