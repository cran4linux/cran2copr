%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDRFA
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Robust Factor Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-pracma 

%description
Factor models have been widely applied in areas such as economics and
finance, and the well-known heavy-tailedness of macroeconomic/financial
data should be taken into account when conducting factor analysis. We
propose two algorithms to do robust factor analysis by considering the
Huber loss. One is based on minimizing the Huber loss of the idiosyncratic
error's L2 norm, which turns out to do Principal Component Analysis (PCA)
on the weighted sample covariance matrix and thereby named as Huber PCA.
The other one is based on minimizing the element-wise Huber loss, which
can be solved by an iterative Huber regression algorithm. In this package
we also provide the code for traditional PCA, the Robust Two Step (RTS)
method by He et al. (2022) and the Quantile Factor Analysis (QFA) method
by Chen et al. (2021) and He et al. (2023).

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
