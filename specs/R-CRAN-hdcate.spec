%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdcate
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Conditional Average Treatment Effects with High-Dimensional Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-hdm 
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-hdm 
Requires:         R-CRAN-locpol 
Requires:         R-CRAN-caret 

%description
A two-step double-robust method to estimate the conditional average
treatment effects (CATE) with potentially high-dimensional covariate(s).
In the first stage, the nuisance functions necessary for identifying CATE
are estimated by machine learning methods, allowing the number of
covariates to be comparable to or larger than the sample size. The second
stage consists of a low-dimensional local linear regression, reducing CATE
to a function of the covariate(s) of interest. The CATE estimator
implemented in this package not only allows for high-dimensional data, but
also has the “double robustness” property: either the model for the
propensity score or the models for the conditional means of the potential
outcomes are allowed to be misspecified (but not both). This package is
based on the paper by Fan et al., "Estimation of Conditional Average
Treatment Effects With High-Dimensional Data" (2022), Journal of Business
& Economic Statistics <doi:10.1080/07350015.2020.1811102>.

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
