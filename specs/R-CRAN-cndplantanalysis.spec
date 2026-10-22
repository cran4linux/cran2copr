%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cndplantanalysis
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Nutrient Diagnosis for Plant Tissue Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides an implementation of Compositional Nutrient Diagnosis (CND) for
plant tissue tests. Computes scale invariant simplex filling values(Rd),
row-centered log-ratios (CLR), iterative database partitioning via
Cate-Nelson procedures, cubic polynomial regression of cumulative variance
ratio functions to determine inflection point yield cutoffs, critical CND
nutrient imbalance thresholds (r^2) using the chi-square distribution,
diagnostic standardized indices (Ix) and automated Cate Nelson scatter
partitioning. Includes linear, non-linear, cumulative variance, chi-square
and quadrant plotting functions.Methodology and theoretical frameworks are
grounded in Parent and Dafir (1992) <doi:10.21273/JASHS.117.2.239> and
Khiari et al. (2001) <doi:10.2134/agronj2001.934802x>.

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
