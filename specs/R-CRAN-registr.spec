%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  registr
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Curve Registration for Exponential Family Functional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pbs 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pbs 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Matrix 

%description
A method for performing joint registration and functional principal
component analysis for curves (functional data) that are generated from
exponential family distributions. This mainly implements the algorithms
described in 'Wrobel et al. (2019)' <doi:10.1111/biom.12963> and further
adapts them to potentially incomplete curves where (some) curves are not
observed from the beginning and/or until the end of the common domain.
Curve registration can be used to better understand patterns in functional
data by separating curves into phase and amplitude variability. This
software handles both binary and continuous functional data, and is
especially applicable in accelerometry and wearable technology.

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
