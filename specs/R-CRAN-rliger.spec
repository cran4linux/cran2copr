%global __brp_check_rpaths %{nil}
%global packname  rliger
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linked Inference of Genomic Experimental Relationships

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-riverplot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-riverplot 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-mclust 
Requires:         R-stats 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-hdf5r 

%description
Uses an extension of nonnegative matrix factorization to identify shared
and dataset-specific factors. See Welch J, Kozareva V, et al (2019)
<doi:10.1016/j.cell.2019.05.006>, and Liu J, Gao C, Sodicoff J, et al
(2020) <doi:10.1038/s41596-020-0391-8> for more details.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
