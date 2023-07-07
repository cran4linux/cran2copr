%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vstdct
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Estimation of Toeplitz Covariance Matrices

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dtt 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-dtt 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 

%description
A nonparametric method to estimate Toeplitz covariance matrices from a
sample of n independently and identically distributed p-dimensional
vectors with mean zero. The data is preprocessed with the discrete cosine
matrix and a variance stabilization transformation to obtain an
approximate Gaussian regression setting for the log-spectral density
function. Estimates of the spectral density function and the inverse of
the covariance matrix are provided as well. Functions for simulating data
and a protein data example are included. For details see (Klockmann,
Krivobokova; 2023), <arXiv:2303.10018>.

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
