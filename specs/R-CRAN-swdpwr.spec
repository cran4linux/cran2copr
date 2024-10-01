%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  swdpwr
%global packver   1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Power Calculation for Stepped Wedge Cluster Randomized Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat.random 

%description
To meet the needs of statistical power calculation for stepped wedge
cluster randomized trials, we developed this software. Different
parameters can be specified by users for different scenarios, including:
cross-sectional and cohort designs, binary and continuous outcomes,
marginal (GEE) and conditional models (mixed effects model), three link
functions (identity, log, logit links), with and without time effects (the
default specification assumes no-time-effect) under exchangeable, nested
exchangeable and block exchangeable correlation structures. Unequal
numbers of clusters per sequence are also allowed. The methods included in
this package: Zhou et al. (2020) <doi:10.1093/biostatistics/kxy031>, Li et
al. (2018) <doi:10.1111/biom.12918>. Supplementary documents can be found
at:
<https://ysph.yale.edu/cmips/research/software/study-design-power-calculation/swdpwr/>.
The Shiny app for swdpwr can be accessed at:
<https://jiachenchen322.shinyapps.io/swdpwr_shinyapp/>. The package also
includes functions that perform calculations for the intra-cluster
correlation coefficients based on the random effects variances as input
variables for continuous and binary outcomes, respectively.

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
