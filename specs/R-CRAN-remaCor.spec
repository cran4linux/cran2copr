%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remaCor
%global packver   0.0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.16
Release:          1%{?dist}%{?buildtag}
Summary:          Random Effects Meta-Analysis for Correlated Test Statistics

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-grid 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Meta-analysis is widely used to summarize estimated effects sizes across
multiple statistical tests. Standard fixed and random effect meta-analysis
methods assume that the estimated of the effect sizes are statistically
independent.  Here we relax this assumption and enable meta-analysis when
the correlation matrix between effect size estimates is known.  Fixed
effect meta-analysis uses the method of Lin and Sullivan (2009)
<doi:10.1016/j.ajhg.2009.11.001>, and random effects meta-analysis uses
the method of Han, et al. <doi:10.1093/hmg/ddw049>.

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
