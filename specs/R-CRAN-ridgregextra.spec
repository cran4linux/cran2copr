%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ridgregextra
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ridge Regression Parameter Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-CRAN-isdals >= 3.0.0
BuildRequires:    R-CRAN-mctest >= 1.3.0
Requires:         R-CRAN-plotly >= 4.9.0
Requires:         R-stats >= 4.0.0
Requires:         R-graphics >= 4.0.0
Requires:         R-CRAN-isdals >= 3.0.0
Requires:         R-CRAN-mctest >= 1.3.0

%description
It is a package that provides alternative approach for finding optimum
parameters of ridge regression. This package focuses on finding the ridge
parameter value k which makes the variance inflation factors closest to 1,
while keeping them above 1 as addressed by Michael Kutner, Christopher
Nachtsheim, John Neter, William Li (2004, ISBN:978-0073108742). Moreover,
the package offers end-to-end functionality to find optimum k value and
presents the detailed ridge regression results. Finally it shows three
sets of graphs consisting k versus variance inflation factors, regression
coefficients and standard errors of them.

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
