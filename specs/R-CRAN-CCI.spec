%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CCI
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computational Test for Conditional Independence

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dagitty 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-ranger 
Requires:         R-stats 
Requires:         R-CRAN-dagitty 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-progress 

%description
Tool for performing computational testing for conditional independence
between variables in a dataset. 'CCI' implements permutation in
combination with Monte Carlo Cross-Validation in generating null
distributions and test statistics. For more details see Computational Test
for Conditional Independence (2024) <doi:10.3390/a17080323>.

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
