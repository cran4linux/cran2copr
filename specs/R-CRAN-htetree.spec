%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  htetree
%global packver   0.1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.20
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference with Tree-Based Machine Learning Algorithms

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-Matching 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringr 

%description
Estimating heterogeneous treatment effects with tree-based machine
learning algorithms and visualizing estimated results in flexible and
presentation-ready ways. For more information, see Brand, Xu, Koch, and
Geraldo (2021) <doi:10.1177/0081175021993503>. Our current package first
started as a fork of the 'causalTree' package on 'GitHub' and we greatly
appreciate the authors for their extremely useful and free package.

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
