%global packname  psborrow
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Dynamic Borrowing with Propensity Score

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-futile.logger 
Requires:         R-methods 
Requires:         R-utils 

%description
A tool which aims to help evaluate the effect of external borrowing using
an integrated approach described in Lewis et al., (2019)
<doi:10.1080/19466315.2018.1497533> that combines propensity score and
Bayesian dynamic borrowing methods.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
