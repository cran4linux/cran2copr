%global packname  mixpoissonreg
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Poisson Regression for Overdispersed Count Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gamlss 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gamlss 

%description
Fits mixed Poisson regression models (Poisson-Inverse Gaussian or
Negative-Binomial) on data sets with response variables being count data.
The models can have varying precision parameter, where a linear regression
structure (through a link function) is assumed to hold on the precision
parameter. The Expectation-Maximization algorithm for both these models
(Poisson Inverse Gaussian and Negative Binomial) is an important
contribution of this package. Another important feature of this package is
the set of functions to perform global and local influence analysis. See
Barreto-Souza and Simas (2016) <doi:10.1007/s11222-015-9601-6> for further
details.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
