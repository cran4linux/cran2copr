%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hierNest
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized Regression with Hierarchical Nested Parameterization Structure

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dotCall64 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dotCall64 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-plotly 

%description
Efficient implementation of penalized regression with hierarchical nested
parametrization for grouped data. The package provides penalized
regression methods that decompose subgroup specific effects into shared
global effects, Major subgroup specific effects, and Minor subgroup
specific effects, enabling structured borrowing of information across
related clinical subgroups. Both lasso and hierarchical overlapping group
lasso penalties are supported to encourage sparsity while respecting the
nested subgroup structure. Efficient computation is achieved through a
modified design matrix representation and a custom algorithm for
overlapping group penalties.

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
