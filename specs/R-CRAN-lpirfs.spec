%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lpirfs
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Local Projections Impulse Response Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-sandwich >= 2.5.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-plm >= 2.2.3
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-lmtest >= 0.9.36
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-sandwich >= 2.5.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-plm >= 2.2.3
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-lmtest >= 0.9.36

%description
Provides functions to estimate and visualize linear as well as nonlinear
impulse responses based on local projections by Jordà (2005)
<doi:10.1257/0002828053828518>. The methods and the package are explained
in detail in Adämmer (2019) <doi:10.32614/RJ-2019-052>.

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
