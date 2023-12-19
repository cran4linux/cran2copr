%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesfMRI
%global packver   0.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Bayesian Methods for Task Functional MRI Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ciftiTools >= 0.8.0
BuildRequires:    R-CRAN-excursions 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-fMRItools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ciftiTools >= 0.8.0
Requires:         R-CRAN-excursions 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-fMRItools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-utils 

%description
Performs a spatial Bayesian general linear model (GLM) for task functional
magnetic resonance imaging (fMRI) data on the cortical surface. Additional
models include group analysis and inference to detect thresholded areas of
activation. Includes direct support for the 'CIFTI' neuroimaging file
format. For more information see A. F. Mejia, Y. R. Yue, D. Bolin, F.
Lindgren, M. A. Lindquist (2020) <doi:10.1080/01621459.2019.1611582> and
D. Spencer, Y. R. Yue, D. Bolin, S. Ryan, A. F. Mejia (2022)
<doi:10.1016/j.neuroimage.2022.118908>.

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
