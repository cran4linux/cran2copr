%global __brp_check_rpaths %{nil}
%global packname  OpVaR
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Statistical Methods for Modelling Operational Risk

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-CRAN-tea 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-ReIns 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-evmix 
Requires:         R-CRAN-VineCopula 
Requires:         R-CRAN-tea 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-ReIns 
Requires:         R-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-evmix 

%description
Functions for computing the value-at-risk in compound Poisson models. The
implementation comprises functions for modeling loss frequencies and loss
severities with plain, mixed (Frigessi et al. (2012)
<doi:10.1023/A:1024072610684>) or spliced distributions using Maximum
Likelihood estimation and Bayesian approaches (Ergashev et al. (2013)
<doi:10.21314/JOP.2013.131>). In particular, the parametrization of tail
distributions includes the fitting of Tukey-type distributions (Kuo and
Headrick (2014) <doi:10.1155/2014/645823>). Furthermore, the package
contains the modeling of bivariate dependencies between loss severities
and frequencies, Monte Carlo simulation for total loss estimation as well
as a closed-form approximation based on Degen (2010)
<doi:10.21314/JOP.2010.084> to determine the value-at-risk.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
