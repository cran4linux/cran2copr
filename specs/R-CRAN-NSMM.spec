%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NSMM
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Stationary Multivariate (Copula-Based) Framework, Hydrological Applications

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-openxlsx 

%description
To account for non-stationary multivariate data, this package implements
the framework including copula and marginal distributions. In addition to
modeling and parameter estimations, it allows the computation and
visualization of multivariate quantile curves for given events. This
package is useful for a variety of disciplines such as finance,
climatology and particularly for hydrological applications, where
dependence structures and marginal parameters may vary over time. This
framework, based on Chebana & Ouarda (2021)
<doi:10.1016/j.jhydrol.2020.125907>, integrates both multivariate and
non-stationary aspects to be more accurate (e.g. for risk assessment) and
more realistic (e.g. considering climate changes).

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
