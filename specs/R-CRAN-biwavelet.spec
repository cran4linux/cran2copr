%global __brp_check_rpaths %{nil}
%global packname  biwavelet
%global packver   0.20.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.20.21
Release:          1%{?dist}%{?buildtag}
Summary:          Conduct Univariate and Bivariate Wavelet Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 

%description
This is a port of the WTC MATLAB package written by Aslak Grinsted and the
wavelet program written by Christopher Torrence and Gibert P. Compo. This
package can be used to perform univariate and bivariate (cross-wavelet,
wavelet coherence, wavelet clustering) analyses.

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
