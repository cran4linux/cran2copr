%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rxode2parse
%global packver   2.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Parsing and Code Generation Functions for 'rxode2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0.7
BuildRequires:    R-CRAN-BH >= 1.78.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.2
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dparser 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dparser 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-qs 
Requires:         R-utils 

%description
Provides the parsing needed for 'rxode2' (Wang, Hallow and James (2016)
<doi:10.1002/psp4.12052>). It also provides the 'stan' based advan linear
compartment model solutions with gradients (Carpenter et al (2015),
<arXiv:1509.07164>) needed in 'nlmixr2' (Fidler et al (2019)
<doi:10.1002/psp4.12445>) needed in 'nlmixr2'. This split will reduce
computational burden of recompiling 'rxode2'.

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
