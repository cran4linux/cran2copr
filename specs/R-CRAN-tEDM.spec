%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tEDM
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Empirical Dynamic Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Inferring causation from time series data through empirical dynamic
modeling (EDM), with methods such as convergent cross mapping from
Sugihara et al. (2012) <doi:10.1126/science.1227079>, partial cross
mapping as outlined in Leng et al. (2020)
<doi:10.1038/s41467-020-16238-0>, and cross mapping cardinality as
described in Tao et al. (2023) <doi:10.1016/j.fmre.2023.01.007>.

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
