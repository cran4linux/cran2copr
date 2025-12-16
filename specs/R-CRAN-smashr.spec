%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smashr
%global packver   1.3-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.12
Release:          1%{?dist}%{?buildtag}
Summary:          Smoothing by Adaptive Shrinkage

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-CRAN-ashr 
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-wavethresh 
Requires:         R-CRAN-ashr 

%description
Fast, wavelet-based Empirical Bayes shrinkage methods for signal
denoising, including smoothing Poisson-distributed data and
Gaussian-distributed data with possibly heteroskedastic error. The
algorithms implement the methods described Z. Xing, P. Carbonetto & M.
Stephens (2021) <https://jmlr.org/papers/v22/19-042.html>.

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
