%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastGLCM
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          'GLCM' Texture Features

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-OpenImageR 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-OpenImageR 
Requires:         R-utils 

%description
Two 'Gray Level Co-occurrence Matrix' ('GLCM') implementations are
included: The first is a fast 'GLCM' feature texture computation based on
'Python' 'Numpy' arrays ('Github' Repository,
<https://github.com/tzm030329/GLCM>). The second is a fast 'GLCM'
'RcppArmadillo' implementation which is parallelized (using 'OpenMP') with
the option to return all 'GLCM' features at once. For more information,
see "Artifact-Free Thin Cloud Removal Using Gans" by Toizumi Takahiro,
Zini Simone, Sagi Kazutoshi, Kaneko Eiji, Tsukada Masato, Schettini
Raimondo (2019), IEEE International Conference on Image Processing (ICIP),
pp. 3596-3600, <doi:10.1109/ICIP.2019.8803652>.

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
