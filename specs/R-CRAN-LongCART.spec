%global __brp_check_rpaths %{nil}
%global packname  LongCART
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Recursive Partitioning for Longitudinal Data and Right Censored Data Using Baseline Covariates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-Formula 

%description
Constructs tree for continuous longitudinal data and survival data using
baseline covariates as partitioning variables according to the 'LongCART'
and 'SurvCART' algorithm, respectively. Later also included functions to
calculate conditional power and predictive power of success based on
interim results and probability of success for a prospective trial.

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
