%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  itdr
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Integral Transformation Methods for SDR in Regression

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-tidyr 

%description
The itdr() routine allows for the estimation of sufficient dimension
reduction subspaces in univariate regression such as the central mean
subspace or central subspace in regression. This is achieved using Fourier
transformation methods proposed by Zhu and Zeng (2006)
<doi:10.1198/016214506000000140>, convolution transformation methods
proposed by Zeng and Zhu (2010) <doi:10.1016/j.jmva.2009.08.004>, and
iterative Hessian transformation methods proposed by Cook and Li (2002)
<doi:10.1214/aos/1021379861>. Additionally, mitdr() function provides
optimal estimators for sufficient dimension reduction subspaces in
multivariate regression by optimizing a discrepancy function using a
Fourier transform approach proposed by Weng and Yin (2022)
<doi:10.5705/ss.202020.0312>, and selects the sufficient variables using
Fourier transform sparse inverse regression estimators proposed by Weng
(2022) <doi:10.1016/j.csda.2021.107380>.

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
