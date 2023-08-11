%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stR
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          STR Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Methods for decomposing seasonal data: STR (a Seasonal-Trend decomposition
procedure based on Regression) and Robust STR. In some ways, STR is
similar to Ridge Regression and Robust STR can be related to LASSO. They
allow for multiple seasonal components, multiple linear covariates with
constant, flexible and seasonal influence. Seasonal patterns (for both
seasonal components and seasonal covariates) can be fractional and
flexible over time; moreover they can be either strictly periodic or have
a more complex topology. The methods provide confidence intervals for the
estimated components. The methods can be used for forecasting.

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
