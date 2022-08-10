%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  abcrf
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Approximate Bayesian Computation via Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-readr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 

%description
Performs Approximate Bayesian Computation (ABC) model choice and parameter
inference via random forests. Pudlo P., Marin J.-M., Estoup A., Cornuet
J.-M., Gautier M. and Robert C. P. (2016)
<doi:10.1093/bioinformatics/btv684>. Estoup A., Raynal L., Verdu P. and
Marin J.-M. <http://journal-sfds.fr/article/view/709>. Raynal L., Marin
J.-M., Pudlo P., Ribatet M., Robert C. P. and Estoup A. (2019)
<doi:10.1093/bioinformatics/bty867>.

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
