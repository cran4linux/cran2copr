%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dacc
%global packver   0.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Detection and Attribution Analysis of Climate Change

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-CFtime 
BuildRequires:    R-CRAN-ncdf4 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-CFtime 
Requires:         R-CRAN-ncdf4 

%description
Conduct detection and attribution of climate change using methods
including optimal fingerprinting via generalized total least squares or
estimating equation approach from Ma et al. (2023)
<doi:10.1175/JCLI-D-22-0681.1>. Provide shrinkage estimators for
covariance matrix from Ledoit and Wolf (2004)
<doi:10.1016/S0047-259X(03)00096-4>, and Ledoit and Wolf (2017)
<doi:10.2139/ssrn.2383361>.

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
