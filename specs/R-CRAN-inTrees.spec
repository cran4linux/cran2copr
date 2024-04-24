%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  inTrees
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interpret Tree Ensembles

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RRF 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
Requires:         R-CRAN-RRF 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-data.table 
Requires:         R-methods 

%description
For tree ensembles such as random forests, regularized random forests and
gradient boosted trees, this package provides functions for: extracting,
measuring and pruning rules; selecting a compact rule set; summarizing
rules into a learner; calculating frequent variable interactions;
formatting rules in latex code.  Reference: Interpreting tree ensembles
with inTrees (Houtao Deng, 2019, <doi:10.1007/s41060-018-0144-8>).

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
