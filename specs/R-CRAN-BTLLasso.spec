%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BTLLasso
%global packver   0.1-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Heterogeneity in Paired Comparison Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-psychotools 

%description
Performs 'BTLLasso' as described by Schauberger and Tutz (2019)
<doi:10.18637/jss.v088.i09> and Schauberger and Tutz (2017)
<doi:10.1177/1471082X17693086>. BTLLasso is a method to include different
types of variables in paired comparison models and, therefore, to allow
for heterogeneity between subjects. Variables can be subject-specific,
object-specific and subject-object-specific and can have an influence on
the attractiveness/strength of the objects. Suitable L1 penalty terms are
used to cluster certain effects and to reduce the complexity of the
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
