%global __brp_check_rpaths %{nil}
%global packname  ipsecr
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Explicit Capture-Recapture by Inverse Prediction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-secr >= 4.5.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-secr >= 4.5.4
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-nlme 

%description
Estimates the density of a spatially distributed animal population sampled
with an array of passive detectors, such as traps. Models incorporating
distance-dependent detection are fitted by simulation and inverse
prediction as proposed by Efford (2004)
<doi:10.1111/j.0030-1299.2004.13043.x>.

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
