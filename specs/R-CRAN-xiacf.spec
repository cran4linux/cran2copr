%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xiacf
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantifying Nonlinear Dependence and Lead-Lag Dynamics via Chatterjee's Xi

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-progressr 
Requires:         R-stats 

%description
Computes Chatterjee's non-parametric correlation coefficient for time
series data. It extends the original metric to time series analysis by
providing the Xi-Autocorrelation Function (Xi-ACF) and
Xi-Cross-Correlation Function (Xi-CCF). The package allows users to test
for non-linear dependence using Iterative Amplitude Adjusted Fourier
Transform (IAAFT) surrogate data. Main functions include xi_acf() and
xi_ccf() for computation, along with matrix extraction tools.
Methodologies are based on Chatterjee (2021)
<doi:10.1080/01621459.2020.1758115> and surrogate data testing methods by
Schreiber and Schmitz (1996) <doi:10.1103/PhysRevLett.77.635>.

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
