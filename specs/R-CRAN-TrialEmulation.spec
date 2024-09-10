%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TrialEmulation
%global packver   0.0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Analysis of Observational Time-to-Event Data

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-broom >= 0.7.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-parglm 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-broom >= 0.7.10
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-parglm 
Requires:         R-CRAN-sandwich 

%description
Implements target trial emulation methods to apply randomized clinical
trial design and analysis in an observational setting. Using marginal
structural models, it can estimate intention-to-treat and per-protocol
effects in emulated trials using electronic health records. A description
and application of the method can be found in Danaei et al (2013)
<doi:10.1177/0962280211403603>.

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
