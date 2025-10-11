%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surrosurv
%global packver   1.1.27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.27
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation of Failure Time Surrogate Endpoints in Individual Patient Data Meta-Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parfm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-eha 
Requires:         R-grDevices 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvmeta 
Requires:         R-CRAN-optimx 
Requires:         R-parallel 
Requires:         R-CRAN-parfm 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Provides functions for the evaluation of surrogate endpoints when both the
surrogate and the true endpoint are failure time variables. The approaches
implemented are: (1) the two-step approach (Burzykowski et al, 2001)
<DOI:10.1111/1467-9876.00244> with a copula model (Clayton, Plackett,
Hougaard) at the first step and either a linear regression of log-hazard
ratios at the second step (either adjusted or not for measurement error);
(2) mixed proportional hazard models estimated via mixed Poisson GLM
(Rotolo et al, 2017 <DOI:10.1177/0962280217718582>).

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
