%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  copulaSFM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Copula-Based Simultaneous Stochastic Frontier Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-VineCopula 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-VineCopula 

%description
Provides estimation procedures for copula-based stochastic frontier models
for cross-sectional data. The package implements maximum likelihood
estimation of stochastic frontier models allowing flexible dependence
structures between inefficiency and noise terms through various copula
families (e.g., Gaussian and Student-t). It enables estimation of
technical efficiency scores, log-likelihood values, and information
criteria (AIC and BIC). The implemented framework builds upon stochastic
frontier analysis introduced by Aigner, Lovell and Schmidt (1977)
<doi:10.1016/0304-4076(77)90052-5> and the copula theory described in Joe
(2014, ISBN:9781466583221). Empirical applications of copula-based
stochastic frontier models can be found in Wiboonpongse et al. (2015)
<doi:10.1016/j.ijar.2015.06.001> and Maneejuk et al. (2017,
ISBN:9783319562176).

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
