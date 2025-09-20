%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RLumCarlo
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Monte-Carlo Methods for Simulating Luminescence Phenomena

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildRequires:    R-CRAN-RcppArmadillo >= 14.6.0
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-abind >= 1.4.8
BuildRequires:    R-CRAN-khroma >= 1.16.0
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-scatterplot3d >= 0.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-abind >= 1.4.8
Requires:         R-CRAN-khroma >= 1.16.0
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-scatterplot3d >= 0.3
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 

%description
A collection of functions to simulate luminescence production in
dosimetric materials using Monte Carlo methods. Implemented are models for
delocalised transitions (e.g., Chen and McKeever (1997)
<doi:10.1142/2781>), localised transitions (e.g., Pagonis et al. (2019)
<doi:10.1016/j.jlumin.2018.11.024>) and tunnelling transitions (Jain et
al. (2012) <doi:10.1088/0953-8984/24/38/385402> and Pagonis et al. (2019)
<doi:10.1016/j.jlumin.2018.11.024>). Supported stimulation methods are
thermal luminescence (TL), continuous-wave optically stimulated
luminescence (CW-OSL), linearly-modulated optically stimulated
luminescence (LM-OSL), linearly-modulated infrared stimulated luminescence
(LM-IRSL), and isothermal luminescence (ITL or ISO-TL).

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
