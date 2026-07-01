%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OptSurvCutR
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Survival Cut-Point Discovery for Time-to-Event Analysis with 'OptSurvCutR'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-tidyr 

%description
Provides a robust workflow for optimal cut-point analysis in time-to-event
('survival') data. Functions determine the optimal number of cut-points
via find_cutpoint_number(), find their precise locations via
find_cutpoint() using systematic or genetic algorithms (via the 'rgenoud'
package), and validate stability via bootstrapping using
validate_cutpoint(). Features include covariate adjustment, parallel
processing, and an extensible S3 plotting engine for clinical dashboards
and diagnostics.

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
