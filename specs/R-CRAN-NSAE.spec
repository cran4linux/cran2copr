%global __brp_check_rpaths %{nil}
%global packname  NSAE
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonstationary Small Area Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-spgwr 
BuildRequires:    R-CRAN-SemiPar 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-spgwr 
Requires:         R-CRAN-SemiPar 

%description
Executes nonstationary Fay-Herriot model and nonstationary generalized
linear mixed model for small area estimation.The empirical best linear
unbiased predictor (EBLUP) under stationary and nonstationary Fay-Herriot
models and empirical best predictor (EBP) under nonstationary generalized
linear mixed model along with the mean squared error estimation are
included. EBLUP for prediction of non-sample area is also included under
both stationary and nonstationary Fay-Herriot models. This extension to
the Fay-Herriot model that accounts for the presence of spatial
nonstationarity was developed by Hukum Chandra, Nicola Salvati and Ray
Chambers (2015) <doi:10.1093/jssam/smu026> and nonstationary generalized
linear mixed model was developed by Hukum Chandra, Nicola Salvati and Ray
Chambers (2017) <doi:10.1016/j.spasta.2017.01.004>. This package is
dedicated to the memory of Dr. Hukum Chandra who passed away while the
package creation was in progress.

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
