%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  enetLTS
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust and Sparse Methods for High Dimensional Linear, Binary and Multinomial Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-robustHD 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-glmnet 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-robustHD 
Requires:         R-grDevices 

%description
Fully robust versions of the elastic net estimator for linear, binary and
multinomial regression, in particular for high dimensional data. The
algorithm searches for outlier-free subsets on which the classical elastic
net estimator can be applied. A reweighting step is added to improve the
statistical efficiency of the estimators. The tuning parameters of the
elastic net penalty are selected by cross-validation. The methods are
described in Kurnaz, Hoffmann and Filzmoser (2018)
<doi:10.1016/j.chemolab.2017.11.017> and in Kurnaz and Filzmoser (2023)
<doi:10.1007/s10618-023-00936-6>.

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
