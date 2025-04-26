%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psd
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive, Sine-Multitaper Power Spectral Density and Cross Spectrum Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-RColorBrewer 

%description
Produces power spectral density estimates through iterative refinement of
the optimal number of sine-tapers at each frequency. This optimization
procedure is based on the method of Riedel and Sidorenko (1995), which
minimizes the Mean Square Error (sum of variance and bias) at each
frequency, but modified for computational stability. The same procedure
can now be used to calculate the cross spectrum (multivariate analyses).

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
