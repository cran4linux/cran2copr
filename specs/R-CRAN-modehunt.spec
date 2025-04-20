%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modehunt
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Multiscale Analysis for Density Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Given independent and identically distributed observations X(1), ..., X(n)
from a density f, provides five methods to perform a multiscale analysis
about f as well as the necessary critical values. The first method,
introduced in Duembgen and Walther (2008), provides simultaneous
confidence statements for the existence and location of local increases
(or decreases) of f, based on all intervals I(all) spanned by any two
observations X(j), X(k). The second method approximates the latter
approach by using only a subset of I(all) and is therefore computationally
much more efficient, but asymptotically equivalent. Omitting the additive
correction term Gamma in either method offers another two approaches which
are more powerful on small scales and less powerful on large scales,
however, not asymptotically minimax optimal anymore. Finally, the block
procedure is a compromise between adding Gamma or not, having intermediate
power properties. The latter is again asymptotically equivalent to the
first and was introduced in Rufibach and Walther (2010).

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
