%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SEQTaRget
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Sequential Trial Emulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-fastglm 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-parallelly 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-fastglm 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-parallelly 

%description
Implementation of sequential trial emulation for the analysis of
observational databases. The 'SEQTaRget' software accommodates
time-varying treatments and confounders, as well as binary and failure
time outcomes. 'SEQTaRget' allows to compare both static and dynamic
strategies, can be used to estimate observational analogs of
intention-to-treat and per-protocol effects, and can adjust for potential
selection bias induced by losses-to-follow-up. (Paper to come).

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
