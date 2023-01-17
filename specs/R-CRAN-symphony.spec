%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  symphony
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient and Precise Single-Cell Reference Atlas Mapping

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-harmony 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-harmony 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-class 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RANN 

%description
Implements the Symphony single-cell reference building and query mapping
algorithms and additional functions described in Kang et al
<https://www.nature.com/articles/s41467-021-25957-x>.

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
