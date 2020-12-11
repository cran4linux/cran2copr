%global packname  logmult
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
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
Goldthorpe), a.k.a. log-multiplicative layer effect model (Xie), and
several association models: Goodman's row-column association models of the
RC(M) and RC(M)-L families with one or several dimensions; two
skew-symmetric association models proposed by Yamaguchi and by van der
Heijden & Mooijaart. Functions allow computing the intrinsic association
coefficient (and therefore the Altham index), including via the Bayes
shrinkage estimator proposed by Zhou; and the RAS/IPF/Deming-Stephan
algorithm.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
