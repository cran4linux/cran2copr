%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsMAMS
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sequential Designs of Multi-Arm Multi-Stage Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
It provides functions to generate operating characteristics and to
calculate Sequential Conditional Probability Ratio Tests(SCPRT) efficacy
and futility boundary values along with sample/event size of Multi-Arm
Multi-Stage(MAMS) trials for different outcomes. The package is based on
Jianrong Wu, Yimei Li, Liang Zhu (2023) <doi:10.1002/sim.9682>, Jianrong
Wu, Yimei Li (2023) "Group Sequential Multi-Arm Multi-Stage Survival Trial
Design with Treatment Selection"(Manuscript accepted for publication) and
Jianrong Wu, Yimei Li, Shengping Yang (2023) "Group Sequential Multi-Arm
Multi-Stage Trial Design with Ordinal Endpoints"(In preparation).

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
