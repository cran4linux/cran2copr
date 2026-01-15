%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  grmtree
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Recursive Partitioning for Graded Response Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt >= 1.36.1
BuildRequires:    R-CRAN-partykit >= 1.2.9
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-strucchange 
Requires:         R-CRAN-mirt >= 1.36.1
Requires:         R-CRAN-partykit >= 1.2.9
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-strucchange 

%description
Provides methods for recursive partitioning based on the 'Graded Response
Model' ('GRM'), extending the 'MOB' algorithm from the 'partykit' package.
The package allows for fitting 'GRM' trees that partition the population
into homogeneous subgroups based on item response patterns and covariates.
Includes specialized plotting functions for visualizing 'GRM' trees with
different terminal node displays (threshold regions, parameter profiles,
and factor score distributions). For more details on the methods, see
Samejima (1969) <doi:10.1002/J.2333-8504.1968.TB00153.X>, Komboz et al.
(2018) <doi:10.1177/0013164416664394> and Arimoro et al. (2025)
<doi:10.1007/s11136-025-04018-6>.

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
