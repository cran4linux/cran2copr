%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TempStable
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Methods to Estimate Parameters of Different Tempered Stable Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-gsl >= 2.1.8
BuildRequires:    R-CRAN-StableEstim >= 2.1
BuildRequires:    R-CRAN-rootSolve >= 1.8
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-hypergeo >= 1.2.13
BuildRequires:    R-CRAN-VGAM >= 1.1.7
BuildRequires:    R-CRAN-copula >= 1.1.2
BuildRequires:    R-CRAN-doParallel >= 1.0.12
BuildRequires:    R-CRAN-stabledist >= 0.7.1
BuildRequires:    R-CRAN-moments >= 0.14
BuildRequires:    R-methods 
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-gsl >= 2.1.8
Requires:         R-CRAN-StableEstim >= 2.1
Requires:         R-CRAN-rootSolve >= 1.8
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-hypergeo >= 1.2.13
Requires:         R-CRAN-VGAM >= 1.1.7
Requires:         R-CRAN-copula >= 1.1.2
Requires:         R-CRAN-doParallel >= 1.0.12
Requires:         R-CRAN-stabledist >= 0.7.1
Requires:         R-CRAN-moments >= 0.14
Requires:         R-methods 

%description
A collection of methods to estimate parameters of different tempered
stable distributions (TSD). Currently, there are seven different tempered
stable distributions to choose from: Tempered stable subordinator
distribution, classical TSD, generalized classical TSD, normal TSD,
modified TSD, rapid decreasing TSD, and Kim-Rachev TSD. The package also
provides functions to compute density and probability functions and tools
to run Monte Carlo simulations. This package has already been used for the
estimation of tempered stable distributions (Massing (2023)
<arXiv:2303.07060>). The following references form the theoretical
background for various functions in this package. References for each
function are explicitly listed in its documentation: Bianchi et al. (2010)
<doi:10.1007/978-88-470-1481-7_4> Bianchi et al. (2011)
<doi:10.1137/S0040585X97984632> Carrasco (2017)
<doi:10.1017/S0266466616000025> Feuerverger (1981)
<doi:10.1111/j.2517-6161.1981.tb01143.x> Hansen et al. (1996)
<doi:10.1080/07350015.1996.10524656> Hansen (1982) <doi:10.2307/1912775>
Hofert (2011) <doi:10.1145/2043635.2043638> Kawai & Masuda (2011)
<doi:10.1016/j.cam.2010.12.014> Kim et al. (2008)
<doi:10.1016/j.jbankfin.2007.11.004> Kim et al. (2009)
<doi:10.1007/978-3-7908-2050-8_5> Kim et al. (2010)
<doi:10.1016/j.jbankfin.2010.01.015> Kuechler & Tappe (2013)
<doi:10.1016/j.spa.2013.06.012> Rachev et al. (2011)
<doi:10.1002/9781118268070>.

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
