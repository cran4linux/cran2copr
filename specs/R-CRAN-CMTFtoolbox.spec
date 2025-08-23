%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMTFtoolbox
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create (Advanced) Coupled Matrix and Tensor Factorization Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mize 
BuildRequires:    R-CRAN-multiway 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mize 
Requires:         R-CRAN-multiway 
Requires:         R-parallel 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rTensor 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Creation and selection of (Advanced) Coupled Matrix and Tensor
Factorization (ACMTF) and ACMTF-Regression (ACMTF-R) models. Selection of
the optimal number of components can be done using
'ACMTF_modelSelection()' and 'ACMTFR_modelSelection()'. The CMTF and ACMTF
methods were originally described by Acar et al., 2011
<doi:10.48550/arXiv.1105.3422> and Acar et al., 2014
<doi:10.1186/1471-2105-15-239>, respectively.

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
