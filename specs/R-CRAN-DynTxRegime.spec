%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DynTxRegime
%global packver   4.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.15
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Estimating Optimal Dynamic Treatment Regimes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modelObj 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-dfoptim 
Requires:         R-methods 
Requires:         R-CRAN-modelObj 
Requires:         R-stats 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-dfoptim 

%description
Methods to estimate dynamic treatment regimes using Interactive
Q-Learning, Q-Learning, weighted learning, and value-search methods based
on Augmented Inverse Probability Weighted Estimators and Inverse
Probability Weighted Estimators. Dynamic Treatment Regimes: Statistical
Methods for Precision Medicine, Tsiatis, A. A., Davidian, M. D., Holloway,
S. T., and Laber, E. B., Chapman & Hall/CRC Press, 2020,
ISBN:978-1-4987-6977-8.

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
