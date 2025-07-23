%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rlme
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Rank-Based Estimation and Prediction in Random Effects Nested Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Estimates robust rank-based fixed effects and predicts robust random
effects in two- and three- level random effects nested models. The
methodology is described in Bilgic & Susmann (2013)
<https://journal.r-project.org/archive/2013/RJ-2013-027/>.

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
