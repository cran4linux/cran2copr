%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NO.PING.PONG
%global packver   0.1.8.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8.7
Release:          1%{?dist}%{?buildtag}
Summary:          Incorporating Previous Findings When Evaluating New Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-MASS 
Requires:         R-utils 

%description
Functions for revealing what happens when effect size estimates from
previous studies are taken into account when evaluating each new dataset
in a study sequence. The analyses can be conducted for cumulative
meta-analyses and for Bayesian data analyses. The package contains sample
data for a wide selection of research topics. Jointly considering previous
findings along with new data is more likely to result in correct
conclusions than does the traditional practice of not incorporating
previous findings, which often results in a back and forth ping-pong of
conclusions when evaluating a sequence of studies. O'Connor & Ermacora
(2021, <doi:10.1037/cbs0000259>).

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
