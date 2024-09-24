%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NPCDTools
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Nonparametric Classification Methods for Cognitive Diagnosis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GDINA 
BuildRequires:    R-CRAN-NPCD 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-SimDesign 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-GDINA 
Requires:         R-CRAN-NPCD 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-SimDesign 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-gtools 

%description
Statistical tools for analyzing cognitive diagnosis (CD) data collected
from small settings using the nonparametric classification (NPCD)
framework. The core methods of the NPCD framework includes the
nonparametric classification (NPC) method developed by Chiu and Douglas
(2013) <DOI:10.1007/s00357-013-9132-9> and the general NPC (GNPC) method
developed by Chiu, Sun, and Bian (2018) <DOI:10.1007/s11336-017-9595-4>
and Chiu and Köhn (2019) <DOI:10.1007/s11336-019-09660-x>. An extension of
the NPCD framework included in the package is the nonparametric method for
multiple-choice items (MC-NPC) developed by Wang, Chiu, and Koehn (2023)
<DOI:10.3102/10769986221133088>.  Functions associated with various
extensions concerning the evaluation, validation, and feasibility of the
CD analysis are also provided. These topics include the completeness of
Q-matrix, Q-matrix refinement method, as well as Q-matrix estimation.

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
