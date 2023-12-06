%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dexterMST
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          CML and Bayesian Calibration of Multistage Tests

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-dexter >= 1.2.2
BuildRequires:    R-CRAN-igraph >= 1.2.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.12.6.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dexter >= 1.2.2
Requires:         R-CRAN-igraph >= 1.2.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo >= 0.12.6.6.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-crayon 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Conditional Maximum Likelihood Calibration and data management of
multistage tests. Supports polytomous items and incomplete designs with
linear as well as multistage tests. Extended Nominal Response and
Interaction models, DIF and profile analysis. See Robert J. Zwitser and
Gunter Maris (2015)<doi:10.1007/s11336-013-9369-6>.

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
