%global __brp_check_rpaths %{nil}
%global packname  chantrics
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Loglikelihood Adjustments for Econometric Models

License:          EUPL (>= 1.2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-chandwich 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-chandwich 
Requires:         R-graphics 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 

%description
Adjusts the loglikelihood of common econometric models for clustered data
based on the estimation process suggested in Chandler and Bate (2007)
<doi:10.1093/biomet/asm015>, using the 'chandwich' package
<https://cran.r-project.org/package=chandwich>, and provides convenience
functions for inference on the adjusted models.

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
