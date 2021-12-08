%global __brp_check_rpaths %{nil}
%global packname  lefko3
%global packver   4.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Historical and Ahistorical Population Projection Matrix Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-SparseM 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-VGAM 

%description
Creates matrix population models for use in population ecological
analyses. Specializes on the construction of historical matrices, which
are 2d matrices comprising 3 consecutive times of demographic information.
Estimates both raw and function-based forms of historical and standard
ahistorical matrices. It also estimates function-based age-by-stage
matrices. Methodology based on Ehrlen (2000)
<doi:10.1890/0012-9658(2000)081[1675:TDOPPD]2.0.CO;2> and deVries and
Caswell (2018) <doi:10.1007/s12080-017-0353-0>.

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
