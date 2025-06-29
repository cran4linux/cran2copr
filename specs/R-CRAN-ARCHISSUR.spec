%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ARCHISSUR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Active Recovery of a Constrained and Hidden Set by Stepwise Uncertainty Reduction Strategy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GPCsign 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-KrigInv 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TruncatedNormal 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-graphics 
Requires:         R-CRAN-GPCsign 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-KrigInv 
Requires:         R-CRAN-future.apply 
Requires:         R-stats 
Requires:         R-CRAN-TruncatedNormal 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-rgenoud 
Requires:         R-graphics 

%description
Stepwise Uncertainty Reduction criterion and algorithm for sequentially
learning a Gaussian Process Classifier as described in Menz et al. (2025).

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
