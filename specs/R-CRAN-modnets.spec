%global __brp_check_rpaths %{nil}
%global packname  modnets
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Moderated Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glinternet 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-interactionTest 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-systemfit 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glinternet 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-interactionTest 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-systemfit 

%description
Methods for modeling moderator variables in cross-sectional, temporal, and
multi-level networks. Includes model selection techniques and a variety of
plotting functions. Implements the methods described by Swanson (2020)
<https://www.proquest.com/openview/d151ab6b93ad47e3f0d5e59d7b6fd3d3>.

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
