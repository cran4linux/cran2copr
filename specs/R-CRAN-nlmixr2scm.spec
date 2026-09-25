%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmixr2scm
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Stepwise Covariate Modeling for 'nlmixr2' Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-nlmixr2est >= 7.0.0
BuildRequires:    R-CRAN-rxode2 >= 5.0.0
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-nlmixr2utils >= 0.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lotri 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-nlmixr2est >= 7.0.0
Requires:         R-CRAN-rxode2 >= 5.0.0
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-nlmixr2utils >= 0.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lotri 
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Stepwise covariate modeling (SCM) for nonlinear mixed-effects models
fitted with 'nlmixr2'. Forward inclusion and backward elimination are
driven by likelihood-ratio tests, and the covariate terms are generated
inside the model body, so continuous covariates are centered and
categorical covariates expanded into indicator columns without editing the
model by hand. Candidate fits can be cached and resumed, fitted in
parallel, and reviewed through per-step and all-candidate summary tables.
The approach follows Jonsson and Karlsson (1998)
<doi:10.1023/A:1011970125687>, and the implementation in
'Perl-speaks-NONMEM' described by Lindbom, Ribbing and Jonsson (2004)
<doi:10.1016/j.cmpb.2003.11.003>.

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
