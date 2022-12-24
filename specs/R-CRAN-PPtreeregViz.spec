%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PPtreeregViz
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Projection Pursuit Regression Tree Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-shapr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-PPtreeViz 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-shapr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-PPtreeViz 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
It was developed as a tool for exploring 'PPTreereg' (Projection Pursuit
TREE of REGression). It uses various projection pursuit indexes and 'XAI'
(eXplainable Artificial Intelligence) methods to help understand the model
by finding connections between the input variables and prediction values
of the model. The 'KernelSHAP' (Aas, Jullum and Løland (2019)
<arXiv:1903.10464>) algorithm was modified to fit ‘PPTreereg’, and some
codes were modified from the 'shapr' package (Sellereite, Nikolai, and
Martin Jullum (2020) <doi:10.21105/joss.02027>). The implemented methods
help to explore the model at the single instance level as well as at the
whole dataset level. Users can compare with other machine learning models
by applying it to the 'DALEX' package of 'R'.

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
