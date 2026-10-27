%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MOFAT
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum One-Factor-at-a-Time Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-SFDesign 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-SLHD 
BuildRequires:    R-CRAN-spacefillr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MaxPro 
BuildRequires:    R-CRAN-RcppHungarian 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-SFDesign 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-SLHD 
Requires:         R-CRAN-spacefillr 
Requires:         R-stats 
Requires:         R-CRAN-MaxPro 
Requires:         R-CRAN-RcppHungarian 
Requires:         R-CRAN-withr 

%description
Identifying important factors from a large number of potentially important
factors in a highly nonlinear and computationally expensive black-box
model is a difficult problem. Xiao, Joseph, and Ray (2022)
<doi:10.1080/00401706.2022.2141897> proposed Maximum One-Factor-at-a-Time
(MOFAT) designs for this purpose. A MOFAT design is a collection of
one-factor-at-a-time (OFAT) designs constructed to achieve maximal
screening capability. Song and Joseph (2026)
<doi:10.48550/arXiv.2609.02087> extended the MOFAT framework to
incorporate nominal and discrete numeric factors. The resulting designs
are implemented in the mofatQQ function. Yu and Joseph (2026)
<doi:10.48550/arXiv.2606.02533> proposed Space-Filling
One-Factor-at-a-Time (SOFT) designs, which achieve optimal space-filling
properties while retaining the screening capability. Therefore, SOFT
designs are useful for both factor screening and surrogate modeling. The
work on MOFAT is supported by a U.S. National Science Foundation (NSF)
grant CMMI-1921646
<https://www.nsf.gov/awardsearch/show-award/?AWD_ID=1921646>, and the work
on MOFATQQ and SOFT is supported by a U.S. NSF grant DMS-2310637.

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
