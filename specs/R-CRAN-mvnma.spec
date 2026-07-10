%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvnma
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Network Meta-Analysis using Bayesian Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 8.3.0
BuildRequires:    R-CRAN-netmeta >= 3.4.0
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-meta >= 8.3.0
Requires:         R-CRAN-netmeta >= 3.4.0
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forcats 

%description
Tools to conduct Bayesian multivariate network meta-analysis providing -
the single correlation coefficient model by Efthimiou et al. (2015)
<doi:10.1093/biostatistics/kxu030>; - per-outcome treatment hierarchies
using the surface under the cumulative ranking curve (SUCRA), the
probability of best value, or median (or mean) ranks (Salanti et al.,
2011) <doi:10.1016/j.jclinepi.2010.03.016>; - across-outcomes benefit-risk
assessment using the VišeKriterijumska Optimizacija I Kompromisno Rešenje
(VIKOR) method (Opricovic & Tzeng, 2004)
<doi:10.1016/S0377-2217(03)00020-1>; - convergence checks using trace
plots, density plots, or the R-hat statistic; - forest plots of treatment
estimates, scatter plots of per-outcome rankings, Hasse diagrams (Carlsen
& Bruggemann, 2014) <doi:10.1002/cem.2569> to visualize the partial order
of the treatments across all outcomes.

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
