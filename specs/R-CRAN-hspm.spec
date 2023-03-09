%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hspm
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Heterogeneous Spatial Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-sphet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-sphet 
Requires:         R-stats 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-Matrix 

%description
Spatial heterogeneity can be specified in various ways. 'hspm' is an
ambitious project that aims at implementing various methodologies to
control for heterogeneity in spatial models. The current version of 'hspm'
deals with spatial and (non-spatial) regimes models. In particular, the
package allows to estimate a general spatial regimes model with additional
endogenous variables, specified in terms of a spatial lag of the dependent
variable, the spatially lagged regressors, and, potentially, a spatially
autocorrelated error term. Spatial regime models are estimated by
instrumental variables and generalized methods of moments (see Arraiz et
al., (2010) <doi:10.1111/j.1467-9787.2009.00618.x>, Bivand and Piras,
(2015) <doi:10.18637/jss.v063.i18>, Drukker et al., (2013)
<doi:10.1080/07474938.2013.741020>, Kelejian and Prucha, (2010)
<doi:10.1016/j.jeconom.2009.10.025>).

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
