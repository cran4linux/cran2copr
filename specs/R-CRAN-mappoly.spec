%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mappoly
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Linkage Maps in Autopolyploids

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-princurve 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-vcfR 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggsci 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-princurve 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-vcfR 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-plotly 

%description
Construction of genetic maps in autopolyploid full-sib populations. Uses
pairwise recombination fraction estimation as the first source of
information to sequentially position allelic variants in specific
homologous chromosomes. For situations where pairwise analysis has limited
power, the algorithm relies on the multilocus likelihood obtained through
a hidden Markov model (HMM). For more detail, please see Mollinari and
Garcia (2019) <doi:10.1534/g3.119.400378> and Mollinari et al. (2020)
<doi:10.1534/g3.119.400620>.

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
