%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  corsym
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Correlation Estimation for Exchangeable/Symmetrical Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
We implement a new correlation estimator, CorSym, designed for
exchangeable variables, where the ordering of the two values in the pair
is arbitrary.  This kind of data arises frequently in the study of
assortative pairing (for example, income in a couple).  The standard
Pearson estimator is sensitive to such ordering and can be highly biased
when the order is biased (when the first value tends to have lower or
higher values than the second value).  CorSym gives the same estimate
deterministically for all orders within each pair, and estimates the
desired correlation without bias (variables must be exchangeable).  The
package also includes utilities to simulate biased orders and test for
order bias.  Described in Kennedy and Ochoa (2026)
<doi:10.64898/2026.08.22.746446>.

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
