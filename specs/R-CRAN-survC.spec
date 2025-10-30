%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Model Validation Utilities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-rvg 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-timeROC 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-rvg 

%description
Provides helper functions to compute linear predictors, time-dependent ROC
curves, and Harrell's concordance index for Cox proportional hazards
models as described in Therneau (2024)
<https://CRAN.R-project.org/package=survival>, Therneau and Grambsch
(2000, ISBN:0-387-98784-3), Hung and Chiang (2010)
<doi:10.1002/cjs.10046>, Uno et al. (2007)
<doi:10.1198/016214507000000149>, Blanche, Dartigues, and Jacqmin-Gadda
(2013) <doi:10.1002/sim.5958>, Blanche, Latouche, and Viallon (2013)
<doi:10.1007/978-1-4614-8981-8_11>, Harrell et al. (1982)
<doi:10.1001/jama.1982.03320430047030>, Peto and Peto (1972)
<doi:10.2307/2344317>, Schemper (1992) <doi:10.2307/2349009>, and Uno et
al. (2011) <doi:10.1002/sim.4154>.

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
