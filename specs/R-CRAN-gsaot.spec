%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsaot
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Global Sensitivity Analysis Indices Using Optimal Transport

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-patchwork >= 1.2.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.4.0.0
BuildRequires:    R-CRAN-transport >= 0.15.0
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-patchwork >= 1.2.0
Requires:         R-CRAN-RcppEigen >= 0.3.4.0.0
Requires:         R-CRAN-transport >= 0.15.0
Requires:         R-CRAN-boot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Computing Global Sensitivity Indices from given data using Optimal
Transport, as defined in Borgonovo et al (2024)
<doi:10.1287/mnsc.2023.01796>. You provide an input sample, an output
sample, decide the algorithm, and compute the indices.

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
