%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lax
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Loglikelihood Adjustment for Extreme Value Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chandwich 
BuildRequires:    R-CRAN-exdex 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-revdbayes 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-chandwich 
Requires:         R-CRAN-exdex 
Requires:         R-graphics 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-revdbayes 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-utils 

%description
Performs adjusted inferences based on model objects fitted, using maximum
likelihood estimation, by the extreme value analysis packages 'eva'
<https://cran.r-project.org/package=eva>, 'evd'
<https://cran.r-project.org/package=evd>, 'evir'
<https://cran.r-project.org/package=evir>, 'extRemes'
<https://cran.r-project.org/package=extRemes>, 'fExtremes'
<https://cran.r-project.org/package=fExtremes>, 'ismev'
<https://cran.r-project.org/package=ismev>, 'mev'
<https://cran.r-project.org/package=mev>, 'POT'
<https://cran.r-project.org/package=POT> and 'texmex'
<https://cran.r-project.org/package=texmex>. Adjusted standard errors and
an adjusted loglikelihood are provided, using the 'chandwich' package
<https://cran.r-project.org/package=chandwich> and the object-oriented
features of the 'sandwich' package
<https://cran.r-project.org/package=sandwich>. The adjustment is based on
a robust sandwich estimator of the parameter covariance matrix, based on
the methodology in Chandler and Bate (2007) <doi:10.1093/biomet/asm015>.
This can be used for cluster correlated data when interest lies in the
parameters of the marginal distributions, or for performing inferences
that are robust to certain types of model misspecification.  Univariate
extreme value models, including regression models, are supported.

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
