%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PSor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Principal Stratification Analysis Beyond Monotonicity

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geex 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geex 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-numDeriv 

%description
Estimates principal causal effects under principal stratification using a
margin-free, conditional odds ratio sensitivity parameter. This framework
unifies the monotonicity assumption and the counterfactual intermediate
independence assumption, allowing for robust analysis when monotonicity
may not hold. Computes point estimates, standard errors, and confidence
intervals for conditionally doubly robust and debiased machine learning
estimators. The methodological details are described in Tong, Kahan,
Harhay, and Li (2025) <doi:10.48550/arXiv.2501.17514>.

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
