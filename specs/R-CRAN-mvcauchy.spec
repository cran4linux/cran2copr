%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvcauchy
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Cauchy Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 

%description
The Cauchy distribution is a special case of the t distribution when the
degrees of freedom are equal to 1. The functions are related to the
multivariate Cauchy distribution and include simulation, computation of
the density, maximum likelihood estimation, contour plot of the bivariate
Cauchy distribution, and discriminant analysis. References include:
Nadarajah S. and Kotz S. (2008). "Estimation methods for the multivariate
t distribution". Acta Applicandae Mathematicae, 102(1): 99--118.
<doi:10.1007/s10440-008-9212-8>, and Kanti V. Mardia, John T. Kent and
John M. Bibby (1979). "Multivariate analysis", ISBN:978-0124712522.
Academic Press, London.

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
