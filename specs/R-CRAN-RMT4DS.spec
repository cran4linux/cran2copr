%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMT4DS
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Random Matrix Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RMTstat 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-mpoly 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RMTstat 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-mpoly 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-quadprog 

%description
We generate random variables following general Marchenko-Pastur
distribution and Tracy-Widom distribution. We compute limits and
distributions of eigenvalues and generalized components of spiked
covariance matrices. We give estimation of all population eigenvalues of
spiked covariance matrix model. We give tests of population covariance
matrix. We also perform matrix denoising for signal-plus-noise model.

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
