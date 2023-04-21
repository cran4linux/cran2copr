%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cellWise
%global packver   2.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Data with Cellwise Outliers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.600.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10.14
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-svd 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-shape 
Requires:         R-CRAN-Rcpp >= 0.12.10.14
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-svd 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-shape 

%description
Tools for detecting cellwise outliers and robust methods to analyze data
which may contain them. Contains the implementation of the algorithms
described in Rousseeuw and Van den Bossche (2018)
<doi:10.1080/00401706.2017.1340909> (open access) Hubert et al. (2019)
<doi:10.1080/00401706.2018.1562989> (open access), Raymaekers and
Rousseeuw (2021) <doi:10.1080/00401706.2019.1677270> (open access),
Raymaekers and Rousseeuw (2021) <doi:10.1007/s10994-021-05960-5> (open
access), Raymaekers and Rousseeuw (2021) <doi:10.52933/jdssv.v1i3.18>
(open access), Raymaekers and Rousseeuw (2022) <arXiv:2207.13493> (open
access) Rousseeuw (2022) <arXiv:2209.12697> (open access). Examples can be
found in the vignettes: "DDC_examples", "MacroPCA_examples",
"wrap_examples", "transfo_examples", "DI_examples", "cellMCD_examples" ,
"Correspondence_analysis_examples", and "cellwise_weights_examples".

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
