%global __brp_check_rpaths %{nil}
%global packname  multifamm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Functional Additive Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MFPCA >= 1.3.2
BuildRequires:    R-CRAN-sparseFLMM > 0.3.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-funData 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-MFPCA >= 1.3.2
Requires:         R-CRAN-sparseFLMM > 0.3.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-funData 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-zoo 

%description
An implementation for multivariate functional additive mixed models
(multiFAMM), see Volkmann et al. (2021, <arXiv:2103.06606>). It builds on
developed methods for univariate sparse functional regression models and
multivariate functional principal component analysis. This package
contains the function to run a multiFAMM and some convenience functions
useful when working with large models. An additional package on GitHub
contains more convenience functions to reproduce the analyses of the
corresponding paper (<https://github.com/alexvolkmann/multifammPaper>).

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
