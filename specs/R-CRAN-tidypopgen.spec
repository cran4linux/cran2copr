%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidypopgen
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Population Genetics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-bigparallelr 
BuildRequires:    R-CRAN-bigsnpr 
BuildRequires:    R-CRAN-bigstatsr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-runner 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-rmio 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-bigparallelr 
Requires:         R-CRAN-bigsnpr 
Requires:         R-CRAN-bigstatsr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-runner 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-UpSetR 
Requires:         R-CRAN-vctrs 

%description
We provide a tidy grammar of population genetics, facilitating the
manipulation and analysis of data on biallelic single nucleotide
polymorphisms (SNPs). 'tidypopgen' scales to very large genetic datasets
by storing genotypes on disk, and performing operations on them in chunks,
without ever loading all data in memory. The full functionalities of the
package are described in Carter et al. (2025)
<doi:10.1111/2041-210x.70204>.

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
