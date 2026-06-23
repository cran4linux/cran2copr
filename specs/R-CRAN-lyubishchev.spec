%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lyubishchev
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Taxonomy Methods of A.A. Lyubishchev (1943)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Implements the multivariate classification methods of Alexander
Alexandrovich Lyubishchev (1890-1972), as described in his 1943 manuscript
'Programma obshchey sistematiki' Lyubishchev (1943)
<https://www.zin.ru/animalia/coleoptera/rus/lyubis05.htm> and published in
Lubischew (1962) <https://www.jstor.org/stable/2527894>. Provides
divergence_coefficient() for measuring separation between groups on
continuous features, scatter_ellipse() for fitting covariance ellipses per
class, transgression() for detecting ellipse overlap, and classify() for
Bayesian posterior classification. These methods predate and are more
general than the binary-character similarity coefficients of Sokal and
Sneath (1963) that appear in other R packages.

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
