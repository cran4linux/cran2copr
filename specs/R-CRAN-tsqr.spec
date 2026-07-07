%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsqr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Threshold-Spatial-Quantile Panel Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.90
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-plm >= 2.6.0
BuildRequires:    R-CRAN-spdep >= 1.2.0
BuildRequires:    R-CRAN-spatialreg >= 1.2.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-quantreg >= 5.90
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-plm >= 2.6.0
Requires:         R-CRAN-spdep >= 1.2.0
Requires:         R-CRAN-spatialreg >= 1.2.0
Requires:         R-stats 
Requires:         R-utils 

%description
Implements a sequential panel estimation protocol for regional economic
panels that combines three estimation layers in a fixed order. The first
layer applies a two-way fixed effects baseline. The second layer applies
the panel threshold regression method of Hansen (1999)
<doi:10.1016/S0304-4076(99)00025-1> to identify structural breaks at an
unknown threshold of a moderating variable, with bootstrap inference
following Hansen (2000) <doi:10.1111/1468-0262.00124>. The third layer
applies a spatial Durbin model with an impact decomposition following
LeSage and Pace (2009, ISBN:978-1-4200-6424-7) to quantify direct and
indirect spillover effects. The fourth layer applies the two-step panel
quantile estimator of Canay (2011) <doi:10.1111/j.1368-423X.2011.00349.x>
to document distributional heterogeneity in the outcome. The threshold
identified in the second layer defines a subsample used as structured
input to the fourth layer, and a consistency check evaluates whether the
three sets of results are jointly compatible with a common underlying
structural relationship. An illustrative panel of 33 districts of the
state of Maharashtra, India, observed over 10 agricultural years, is
included with the package.

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
