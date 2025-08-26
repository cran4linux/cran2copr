%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logmult
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Log-Multiplicative Models, Including Association Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gnm >= 1.0.5
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-qvcalc 
Requires:         R-CRAN-gnm >= 1.0.5
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-qvcalc 

%description
Functions to fit log-multiplicative models using 'gnm', with support for
convenient printing, plots, and jackknife/bootstrap standard errors. For
complex survey data, models can be fitted from design objects from the
'survey' package. Currently supported models include UNIDIFF (Erikson &
Goldthorpe, 1992), a.k.a. log-multiplicative layer effect model (Xie,
1992) <doi:10.2307/2096242>, and several association models: Goodman
(1979) <doi:10.2307/2286971> row-column association models of the RC(M)
and RC(M)-L families with one or several dimensions; two skew-symmetric
association models proposed by Yamaguchi (1990) <doi:10.2307/271086> and
by van der Heijden & Mooijaart (1995) <doi:10.1177/0049124195024001002>
Functions allow computing the intrinsic association coefficient (see
Bouchet-Valat (2022) <doi:10.1177/0049124119852389>) and the Altham (1970)
index <doi:10.1111/j.2517-6161.1970.tb00816.x>, including via the Bayes
shrinkage estimator proposed by Zhou (2015)
<doi:10.1177/0081175015570097>; and the RAS/IPF/Deming-Stephan algorithm.

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
