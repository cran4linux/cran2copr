%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  comets
%global packver   0.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Covariance Measure Tests for Conditional Independence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-coin 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-coin 

%description
Covariance measure tests for conditional independence testing against
conditional covariance and nonlinear conditional mean alternatives.
Contains versions of the generalised covariance measure test (Shah and
Peters, 2020, <doi:10.1214/19-aos1857>) and projected covariance measure
test (Lundborg et al., 2023, <doi:10.48550/arXiv.2211.02039>).
Applications can be found in Kook and Lundborg (2024,
<doi:10.1093/bib/bbae475>).

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
