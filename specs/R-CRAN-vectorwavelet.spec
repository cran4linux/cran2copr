%global __brp_check_rpaths %{nil}
%global packname  vectorwavelet
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vector Wavelet Coherence for Multiple Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-biwavelet >= 0.20.19
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-biwavelet >= 0.20.19
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rcpp 

%description
New wavelet methodology (vector wavelet coherence) (Oygur, T., Unal, G,
2020 <doi:10.1007/s40435-020-00706-y>) to handle dynamic co-movements of
multivariate time series via extending multiple and quadruple wavelet
coherence methodologies. This package can be used to perform multiple
wavelet coherence, quadruple wavelet coherence, and n-dimensional vector
wavelet coherence analyses.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
