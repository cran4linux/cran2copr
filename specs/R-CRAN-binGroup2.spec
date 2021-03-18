%global packname  binGroup2
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Identification and Estimation using Group Testing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-rBeta2009 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-rBeta2009 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Methods for the group testing identification problem: 1) Operating
characteristics (e.g., expected number of tests) for commonly used
hierarchical and array-based algorithms, and 2) Optimal testing
configurations for these same algorithms. Calculations for algorithms with
single-disease assays are described in Hitt et al. (2019)
<doi:10.1002/sim.8341> and with multiplex assays are described in Bilder
et al. (2019) <doi:10.1111/biom.12988> and Hou et al. (2020)
<doi:10.1093/biostatistics/kxy058>. Methods for the group testing
estimation problem: 1) Estimation and inference procedures for an overall
prevalence, and 2) Regression modeling for commonly used hierarchical and
array-based algorithms. Estimation and confidence interval methods are
described in Biggerstaff (2008) <doi:10.1198/108571108X379055> and
Hepworth & Biggerstaff (2017) <doi:10.1007/s13253-017-0297-2>. Regression
modeling is described in Xie (2001) <doi:10.1002/sim.817>.

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
