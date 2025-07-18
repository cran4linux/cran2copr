%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icmstate
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interval Censored Multi-State Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph >= 1.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-mstate 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-JOPS 
Requires:         R-CRAN-igraph >= 1.3.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-mstate 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-JOPS 

%description
Allows for the non-parametric estimation of transition intensities in
interval-censored multi-state models using the approach of Gomon and
Putter (2024) <doi:10.48550/arXiv.2409.07176> or Gu et al. (2023)
<doi:10.1093/biomet/asad073>.

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
