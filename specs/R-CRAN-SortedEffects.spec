%global packname  SortedEffects
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Inference Methods for Sorted Causal Effects and Classification Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dummies 
Requires:         R-CRAN-boot 
Requires:         R-graphics 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-SparseM 
Requires:         R-stats 
Requires:         R-CRAN-dummies 

%description
Implements the estimation and inference methods for sorted causal effects
and classification analysis as in Chernozhukov, Fernandez-Val and Luo
(2018) <doi:10.3982/ECTA14415>.

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
