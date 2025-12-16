%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pvEBayes
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Bayes Methods for Pharmacovigilance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-ggfittext 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SobolSequence 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wacolors 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-ggfittext 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-graphics 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-SobolSequence 
Requires:         R-stats 
Requires:         R-CRAN-wacolors 
Requires:         R-CRAN-Rcpp 
Requires:         R-splines 
Requires:         R-CRAN-CVXR 

%description
A suite of empirical Bayes methods to use in pharmacovigilance. Contains
various model fitting and post-processing functions. For more details see
Tan et al. (2025) <doi:10.48550/arXiv.2502.09816>,
<doi:10.48550/arXiv.2512.01057>; Koenker and Mizera (2014)
<doi:10.1080/01621459.2013.869224>; Efron (2016)
<doi:10.1093/biomet/asv068>.

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
