%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multvardiv
%global packver   1.0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.14
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Probability Distributions, Statistical Divergence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-data.table 

%description
Multivariate generalized Gaussian distribution, Multivariate Cauchy
distribution, Multivariate t distribution. Distance between two
distributions (see N. Bouhlel and A. Dziri (2019):
<doi:10.1109/LSP.2019.2915000>, N. Bouhlel and D. Rousseau (2022):
<doi:10.3390/e24060838>, N. Bouhlel and D. Rousseau (2023):
<doi:10.1109/LSP.2023.3324594>). Manipulation of these multivariate
probability distributions. This package replaces 'mggd', 'mcauchyd' and
'mstudentd'.

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
