%global __brp_check_rpaths %{nil}
%global packname  CondCopulas
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Inference for Conditional Copula Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ordinalNet 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-wdm 
Requires:         R-CRAN-VineCopula 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ordinalNet 
Requires:         R-CRAN-tree 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-wdm 

%description
Provides functions for the estimation of conditional copulas models,
various estimators of conditional Kendall's tau (proposed in Derumigny and
Fermanian (2019a, 2019b, 2020) <doi:10.1515/demo-2019-0016>,
<doi:10.1016/j.csda.2019.01.013>, <doi:10.1016/j.jmva.2020.104610>), and
test procedures for the simplifying assumption (proposed in Derumigny and
Fermanian (2017) <doi:10.1515/demo-2017-0011> and Derumigny, Fermanian and
Min (2020) <arXiv:2008.09498>).

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
