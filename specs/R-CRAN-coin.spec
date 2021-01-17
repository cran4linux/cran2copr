%global packname  coin
%global packver   1.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Inference Procedures in a Permutation Test Framework

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-libcoin >= 1.0.5
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
BuildRequires:    R-CRAN-matrixStats >= 0.54.0
BuildRequires:    R-CRAN-modeltools >= 0.2.9
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-libcoin >= 1.0.5
Requires:         R-CRAN-mvtnorm >= 1.0.5
Requires:         R-CRAN-matrixStats >= 0.54.0
Requires:         R-CRAN-modeltools >= 0.2.9
Requires:         R-CRAN-survival 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-utils 
Requires:         R-CRAN-multcomp 

%description
Conditional inference procedures for the general independence problem
including two-sample, K-sample (non-parametric ANOVA), correlation,
censored, ordered and multivariate problems described in
doi{10.18637/jss.v028.i08}.

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
