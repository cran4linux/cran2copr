%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DIDHAD
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Difference-in-Differences in Heterogeneous Adoption Designs with Quasi Untreated Groups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-YatchewTest >= 1.1.0
BuildRequires:    R-CRAN-nprobust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-rnames 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-YatchewTest >= 1.1.0
Requires:         R-CRAN-nprobust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-rnames 
Requires:         R-stats 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 

%description
Estimation of Difference-in-Differences (DiD) estimators from de
Chaisemartin et al. (2025) <doi:10.48550/arXiv.2405.04465> in
Heterogeneous Adoption Designs with Quasi Untreated Groups.

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
