%global __brp_check_rpaths %{nil}
%global packname  FDboost
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Boosting Functional Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost >= 2.9.0
BuildRequires:    R-CRAN-gamboostLSS >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stabs 
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-mboost >= 2.9.0
Requires:         R-CRAN-gamboostLSS >= 2.0.0
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-stabs 
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-CRAN-zoo 

%description
Regression models for functional data, i.e., scalar-on-function,
function-on-scalar and function-on-function regression models, are fitted
by a component-wise gradient boosting algorithm. For a manual on how to
use 'FDboost', see Brockhaus, Ruegamer, Greven (2017)
<doi:10.18637/jss.v094.i10>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
