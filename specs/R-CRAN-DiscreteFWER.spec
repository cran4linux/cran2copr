%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiscreteFWER
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          FWER-Based Multiple Testing Procedures with Adaptation for Discrete Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-DiscreteFDR >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-DiscreteFDR >= 2.0.0
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-checkmate 

%description
Implementations of several multiple testing procedures that control the
family-wise error rate (FWER) designed specifically for discrete tests.
Included are discrete adaptations of the Bonferroni, Holm, Hochberg and
Šidák procedures as described in the papers Döhler (2010) "Validation of
credit default probabilities using multiple-testing procedures"
<doi:10.21314/JRMV.2010.062> and Zhu & Guo (2019) "Family-Wise Error Rate
Controlling Procedures for Discrete Data"
<doi:10.1080/19466315.2019.1654912>. The main procedures of this package
take as input the results of a test procedure from package 'DiscreteTests'
or a set of observed p-values and their discrete support under their
nulls. A shortcut function to apply discrete procedures directly to data
is also provided.

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
