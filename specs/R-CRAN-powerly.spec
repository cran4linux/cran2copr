%global __brp_check_rpaths %{nil}
%global packname  powerly
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Analysis for Psychological Networks and More

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-osqp 
BuildRequires:    R-CRAN-bootnet 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-progress 
Requires:         R-parallel 
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-osqp 
Requires:         R-CRAN-bootnet 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 

%description
An implementation of the sample size computation method for network models
proposed by Constantin et al. (2021) <doi:10.31234/osf.io/j5v7u> The
implementation takes the form of a three-step recursive algorithm designed
to find an optimal sample size given a model specification and a
performance measure of interest. It starts with a Monte Carlo simulation
step for computing the performance measure and a statistic at various
sample sizes selected from an initial sample size range. It continues with
a monotone curve-fitting step for interpolating the statistic across the
entire sample size range. The final step employs stratified bootstrapping
to quantify the uncertainty around the fitted curve.

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
