%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reconf
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Intervals for Random Effect Parameters in Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.5.0
BuildRequires:    R-CRAN-lme4 >= 1.1.8
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix >= 1.5.0
Requires:         R-CRAN-lme4 >= 1.1.8
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-trust 
Requires:         R-methods 
Requires:         R-CRAN-generics 

%description
Computes score-based confidence intervals and hypothesis tests for
variance and covariance parameters of random effects in linear mixed
models fitted with 'lme4'. The intervals invert a profile score statistic
on the variance-covariance scale, with nuisance parameters estimated on an
extended parameter set. The intervals have near-nominal coverage uniformly
in the parameter, including near the boundary of the parameter space,
where Wald and likelihood ratio intervals can be unreliable. The methods
are described in Shedden and Ekvall (2026)
<doi:10.48550/arXiv.2610.04181>, building on Ekvall and Bottai (2026)
<doi:10.1093/biomet/asaf079>, Zhang, Ekvall, and Molstad (2025)
<doi:10.1093/biomet/asaf010>, and Ekvall and Bottai (2022)
<doi:10.1214/22-AOS2177>.

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
