%global __brp_check_rpaths %{nil}
%global packname  IRSF
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interaction Random Survival Forest

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-randomForestSRC 
BuildRequires:    R-CRAN-abind 
Requires:         R-parallel 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-randomForestSRC 
Requires:         R-CRAN-abind 

%description
Builds ensemble survival tree models to reveal variable interactions when
the response is a time-to-events outcome. Codes contain randomization,
interaction modeling, and prediction subroutines to be used in addition to
the following R packages: 'survival' for Kaplan-Meier and Cox regression
modeling, 'randomForestSRC' for RSF modeling, and optionally
'ggRandomForests' for Random Forest exploration/visualization. The current
version contains additional R codes in folder "/inst/doc" for the analysis
and generation of results shown in the corresponding article (Dazard et
al. (2018) <doi:10.1515/sagmb-2017-0038>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
