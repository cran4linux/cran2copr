%global __brp_check_rpaths %{nil}
%global packname  concstats
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Market Structure, Concentration and Inequality Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-readr 

%description
Based on individual market shares of all participants in a market or space
or their respective sales figures, the package offers a set of different
structural and concentration measures frequently - and not so frequently -
used in research and in practice. Measures can be calculated in groups or
individually. The calculated measure or the resulting vector in table
format should help practitioners make more informed decisions. Methods
used in this package are from: 1.  Chang, E. J., Guerra, S. M., de Souza
Penaloza, R. A. & Tabak, B. M. (2005) "Banking concentration: the
Brazilian case". 2.  Cobham, A. and A. Summer (2013). "Is It All About the
Tails? The Palma Measure of Income Inequality". 3.  Garcia Alba Idunate,
P. (1994). "Un Indice de dominancia para el analisis de la estructura de
los mercados". 4.  Ginevicius, R. and S. Cirba (2009). "Additive
measurement of market concentration"
<doi:10.3846/1611-1699.2009.10.191-198>. 5.  Herfindahl, O. C. (1950),
"Concentration in the steel industry (PhD thesis)". 6.  Hirschmann, A. O.
(1945), "National power and structure of foreign trade". 7.  Melnik, A.,
O. Shy, and R. Stenbacka (2008), "Assessing market dominance"
<doi:10.1016/j.jebo.2008.03.010>. 8.  Palma, J. G. (2006). "Globalizing
Inequality: 'Centrifugal' and 'Centripetal' Forces at Work". 9.  Shannon,
C. E. (1948). "A Mathematical Theory of Communication".

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
