%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExactMed
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exact Mediation Analysis for Binary Outcomes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brglm2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-pkgcond 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-brglm2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-pkgcond 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-nnet 

%description
A tool for conducting exact parametric regression-based causal mediation
analysis of binary outcomes as described in Samoilenko, Blais and Lefebvre
(2018) <doi:10.1353/obs.2018.0013>; Samoilenko, Lefebvre (2021)
<doi:10.1093/aje/kwab055>; and Samoilenko, Lefebvre (2023)
<doi:10.1002/sim.9621>.

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
