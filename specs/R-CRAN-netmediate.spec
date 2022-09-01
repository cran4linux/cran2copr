%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  netmediate
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Micro-Macro Analysis for Social Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-btergm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-RSiena 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ergMargins 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-intergraph 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-btergm 
Requires:         R-stats 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-RSiena 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ergMargins 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-intergraph 

%description
Estimates micro effects on macro structures (MEMS) and average micro
mediated effects (AMME) when using statistical models for network
structure. URL: <https://github.com/sduxbury/netmediate>. BugReports:
<https://github.com/sduxbury/netmediate/issues>. Long, J. Scott, and Sarah
Mustillo (2018) <doi:10.1177/0049124118799374>. Mize, Trenton D. (2019)
<doi:10.15195/v6.a4>. Imai, Kosuke (2010) <doi:10.1037/a0020761>. Imai,
Kosuke (2010) <doi:10.1214/10-STS321>.

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
