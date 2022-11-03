%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adaptIVPT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Bioequivalence Design for In-Vitro Permeation Tests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rgl 

%description
Contains functions carrying out adaptive procedures using mixed scaling
approach to establish bioequivalence for in-vitro permeation test (IVPT)
data. Currently, the package provides procedures based on parallel
replicate design and balanced data, according to the U.S. Food and Drug
Administration's "Draft Guidance on Acyclovir"
<https:www.accessdata.fda.gov/drugsatfda_docs/psg/Acyclovir_topical
cream_RLD 21478_RV12-16.pdf>. Potvin et al. (2008) <doi:10.1002/pst.294>
provides the basis for our adaptive design (see Method B). This package
reflects the views of the authors and should not be construed to represent
the views or policies of the U.S. Food and Drug Administration.

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
