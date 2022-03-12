%global __brp_check_rpaths %{nil}
%global packname  saeHB.gpois
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SAE using HB Method under Generalized Poisson Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rjags 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
We designed this package to provide function for area level of Small Area
Estimation using Hierarchical Bayesian (HB) method under Generalized
Poisson Distribution. This package provides model using Univariate
Generalized Poisson Distribution for variable of interest. Some datasets
simulated by a data generation are also provided. The 'rjags' package is
employed to obtain parameter estimates. Model-based estimators involves
the HB estimators which include the mean and the variation of mean. For
the reference, see Rao and Molina (2015) <doi:10.1002/9781118735855>, Wang
(2021) <doi:10.1016/j.ecoinf.2021.101301> and Ntzoufras (2009)
<doi:10.1002/9780470434567>.

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
