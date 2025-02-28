%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StratifiedSampling
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Different Methods for Stratified Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-transport 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-transport 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sampling 
Requires:         R-CRAN-Rglpk 

%description
Integrating a stratified structure in the population in a sampling design
can considerably reduce the variance of the Horvitz-Thompson estimator. We
propose in this package different methods to handle the selection of a
balanced sample in stratified population. For more details see Raphaël
Jauslin, Esther Eustache and Yves Tillé (2021)
<doi:10.1007/s42081-021-00134-y>. The package propose also a method based
on optimal transport and balanced sampling, see Raphaël Jauslin and Yves
Tillé <doi:10.1016/j.jspi.2022.12.003>.

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
