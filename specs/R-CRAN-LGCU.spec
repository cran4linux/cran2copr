%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LGCU
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of Learning Gamma CUSUM (Cumulative Sum) Control Charts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tictoc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tictoc 

%description
Implements Cumulative Sum (CUSUM) control charts specifically designed for
monitoring processes following a Gamma distribution. Provides functions to
estimate distribution parameters, simulate control limits, and apply
cautious learning schemes for adaptive thresholding. It supports upward
and downward monitoring with guaranteed performance evaluated via Monte
Carlo simulations. It is useful for quality control applications in
industries where data follows a Gamma distribution. Methods are based on
Madrid-Alvarez et al. (2024) <doi:10.1002/qre.3464> and Madrid-Alvarez et
al. (2024) <doi:10.1080/08982112.2024.2440368>.

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
