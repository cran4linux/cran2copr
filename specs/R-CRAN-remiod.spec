%global __brp_check_rpaths %{nil}
%global packname  remiod
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reference-Based Multiple Imputation for Ordinal/Binary Response

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-JointAI 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-JointAI 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-reshape2 

%description
Reference-based multiple imputation of ordinal and binary responses under
Bayesian framework, as described in Wang and Liu (2022)
<arXiv:2203.02771>. Methods for missing-not-at-random include
Jump-to-Reference (J2R), Copy Reference (CR), and Delta Adjustment which
can generate tipping point analysis.

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
