%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ONAM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Interpretable Neural Additive Models Using Orthogonalization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-keras3 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-keras3 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 

%description
An algorithm for fitting interpretable additive neural networks for
identifiable and visualizable feature effects using post hoc
orthogonalization. Fit custom neural networks intuitively using
established 'R' 'formula' notation, including interaction effects of
arbitrary order while preserving identifiability to enable a functional
decomposition of the prediction function. For more details see Koehler et
al. (2025) <doi:10.1038/s44387-025-00033-7>.

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
