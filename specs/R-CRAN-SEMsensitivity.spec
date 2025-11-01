%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SEMsensitivity
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          SEM Sensitivity Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-semfindr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-semfindr 
Requires:         R-stats 
Requires:         R-methods 

%description
Performs sensitivity analysis for Structural Equation Modeling (SEM). It
determines which sample points need to be removed for the sign of a
specific path in the SEM model to change, thus assessing the robustness of
the model. Methodological manuscript in preparation.

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
