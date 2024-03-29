%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultNonParam
%global packver   1.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Nonparametric Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ICSNP 
Requires:         R-CRAN-ICSNP 

%description
A collection of multivariate nonparametric methods, selected in part to
support an MS level course in nonparametric statistical methods. Methods
include adjustments for multiple comparisons, implementation of
multivariate Mann-Whitney-Wilcoxon testing, inversion of these tests to
produce a confidence region, some permutation tests for linear models, and
some algorithms for calculating exact probabilities associated with one-
and two- stage testing involving Mann-Whitney-Wilcoxon statistics.
Supported by grant NSF DMS 1712839.  See Kolassa and Seifu (2013)
<doi:10.1016/j.acra.2013.03.006>.

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
