%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robustbetareg
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Beta Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-betareg 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-zoo 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-Matrix 

%description
Robust estimators for the beta regression, useful for modeling bounded
continuous data. Currently, four types of robust estimators are supported.
They depend on a tuning constant which may be fixed or selected by a
data-driven algorithm also implemented in the package. Diagnostic tools
associated with the fitted model, such as the residuals and
goodness-of-fit statistics, are implemented. Robust Wald-type tests are
available. More details about robust beta regression are described in
Maluf et al. (2025) <doi:10.1007/s00184-024-00949-1>.

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
