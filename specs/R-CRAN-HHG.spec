%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HHG
%global packver   2.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Heller-Heller-Gorfine Tests of Independence and Equality of Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-methods 

%description
Heller-Heller-Gorfine tests are a set of powerful statistical tests of
multivariate k-sample homogeneity and independence (Heller et. al., 2013,
<doi:10.1093/biomet/ass070>). For the univariate case, the package also
offers implementations of the 'MinP DDP' and 'MinP ADP' tests by Heller
et. al. (2016), which are consistent against all continuous alternatives
but are distribution-free, and are thus much faster to apply.

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
