%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  arulesCBA
%global packver   1.2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Classification Based on Association Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       R-java
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-glmnet >= 3.0.0
BuildRequires:    R-CRAN-arules >= 1.7.4
BuildRequires:    R-CRAN-Matrix >= 1.4.0
BuildRequires:    R-CRAN-discretization >= 1.0.1
BuildRequires:    R-methods 
Requires:         R-CRAN-glmnet >= 3.0.0
Requires:         R-CRAN-arules >= 1.7.4
Requires:         R-CRAN-Matrix >= 1.4.0
Requires:         R-CRAN-discretization >= 1.0.1
Requires:         R-methods 

%description
Provides the infrastructure for association rule-based classification
including the algorithms CBA, CMAR, CPAR, C4.5, FOIL, PART, PRM, RCAR, and
RIPPER to build associative classifiers. Hahsler et al (2019)
<doi:10.32614/RJ-2019-048>.

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
