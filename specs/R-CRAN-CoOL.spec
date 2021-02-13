%global packname  CoOL
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causes of Outcome Learning

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mltools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ClustGeo 
BuildRequires:    R-CRAN-wesanderson 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pROC 
Requires:         R-graphics 
Requires:         R-CRAN-mltools 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ClustGeo 
Requires:         R-CRAN-wesanderson 

%description
Implementing the computational phase of the Causes of Outcome Learning
approach as described in Rieckmann, Dworzynski, Arras, Lapuschkin, Samek,
Arah, Rod, Ekstrom. Causes of outcome learning: A causal
inference-inspired machine learning approach to disentangling common
combinations of potential causes of a health outcome. medRxiv (2020)
<doi:10.1101/2020.12.10.20225243>. The optional 'ggtree' package can be
obtained through Bioconductor.

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
