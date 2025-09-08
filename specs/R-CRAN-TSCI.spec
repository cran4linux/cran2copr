%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSCI
%global packver   3.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Causal Inference with Possibly Invalid Instrumental Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fastDummies 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-CRAN-ranger 
Requires:         R-parallel 
Requires:         R-CRAN-fastDummies 

%description
Two stage curvature identification with machine learning for causal
inference in settings when instrumental variable regression is not
suitable because of potentially invalid instrumental variables. Based on
Guo and Buehlmann (2022) "Two Stage Curvature Identification with Machine
Learning: Causal Inference with Possibly Invalid Instrumental Variables"
<doi:10.48550/arXiv.2203.12808>. The vignette is available in Carl,
Emmenegger, Bühlmann and Guo (2025) "TSCI: Two Stage Curvature
Identification for Causal Inference with Invalid Instruments in R"
<doi:10.18637/jss.v114.i07>.

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
