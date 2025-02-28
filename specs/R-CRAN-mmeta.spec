%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmeta
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Multiple 2 by 2 tables often arise in meta-analysis which combines
statistical evidence from multiple studies. Two risks within the same
study are possibly correlated because they share some common factors such
as environment and population structure. This package implements a set of
novel Bayesian approaches for multivariate meta analysis when the risks
within the same study are independent or correlated. The exact posterior
inference of odds ratio, relative risk, and risk difference given either a
single 2 by 2 table or multiple 2 by 2 tables is provided. Luo, Chen, Su,
Chu, (2014) <doi:10.18637/jss.v056.i11>, Chen, Luo, (2011)
<doi:10.1002/sim.4248>, Chen, Chu, Luo, Nie, Chen, (2015)
<doi:10.1177/0962280211430889>, Chen, Luo, Chu, Su, Nie, (2014)
<doi:10.1080/03610926.2012.700379>, Chen, Luo, Chu, Wei, (2013)
<doi:10.1080/19466315.2013.791483>.

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
