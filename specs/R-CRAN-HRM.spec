%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HRM
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Repeated Measures

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-pseudorank >= 0.3.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-pseudorank >= 0.3.7
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-mvtnorm 

%description
Methods for testing main and interaction effects in possibly
high-dimensional parametric or nonparametric repeated measures in
factorial designs. The observations of the subjects are assumed to be
multivariate normal if using the parametric test. The nonparametric
version tests with regard to nonparametric relative effects (based on
pseudo-ranks). It is possible to use up to 2 whole- and 3 subplot factors.
See Happ et al. (2017, <doi:10.1080/15598608.2017.1307792>) for details.

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
