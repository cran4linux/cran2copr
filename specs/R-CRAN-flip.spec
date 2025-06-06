%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flip
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Permutation Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cherry 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-someMTP 
Requires:         R-methods 
Requires:         R-CRAN-cherry 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-someMTP 

%description
It implements many univariate and multivariate permutation (and rotation)
tests. Allowed tests: the t one and two samples, ANOVA, linear models, Chi
Squared test, rank tests (i.e. Wilcoxon, Mann-Whitney, Kruskal-Wallis),
Sign test and Mc Nemar. Test on Linear Models are performed also in
presence of covariates (i.e. nuisance parameters). The permutation and the
rotation methods to get the null distribution of the test statistics are
available. It also implements methods for multiplicity control such as
Westfall & Young minP procedure and Closed Testing (Marcus, 1976) and
k-FWER. Moreover, it allows to test for fixed effects in mixed effects
models.

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
