%global __brp_check_rpaths %{nil}
%global packname  SIMMS
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Subnetwork Integration for Multi-Modal Signatures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.12
BuildRequires:    R-CRAN-randomForestSRC >= 2.9.1
BuildRequires:    R-CRAN-survival >= 2.36.2
BuildRequires:    R-CRAN-glmnet >= 1.9.8
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-MASS >= 7.3.12
Requires:         R-CRAN-randomForestSRC >= 2.9.1
Requires:         R-CRAN-survival >= 2.36.2
Requires:         R-CRAN-glmnet >= 1.9.8
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-doParallel >= 1.0.10

%description
Algorithms to create prognostic biomarkers using biological genesets or
networks.

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
