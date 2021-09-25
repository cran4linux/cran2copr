%global __brp_check_rpaths %{nil}
%global packname  ccdf
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Distribution-Free Single-Cell Differential Expression Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-RcppNumerical 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-cowplot 

%description
Complex hypothesis testing through conditional cumulative distribution
function estimation. Method is detailed in: Gauthier M, Agniel D, Thiebaut
R & Hejblum BP (2020). "Distribution-free complex hypothesis testing for
single-cell RNA-seq differential expression analysis", BioRxiv
<doi:10.1101/2021.05.21.445165>.

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
