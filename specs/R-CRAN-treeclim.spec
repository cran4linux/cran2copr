%global __brp_check_rpaths %{nil}
%global packname  treeclim
%global packver   2.0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Numerical Calibration of Proxy-Climate Relationships

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.4.000.2
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-lmodel2 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-boot 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-base 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-lmodel2 
Requires:         R-CRAN-np 
Requires:         R-CRAN-boot 

%description
Bootstrapped response and correlation functions, seasonal correlations and
evaluation of reconstruction skills for use in dendroclimatology and
dendroecology, see Zang and Biondi (2015) <doi:10.1111/ecog.01335>.

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
