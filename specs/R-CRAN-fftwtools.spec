%global packname  fftwtools
%global packver   0.9-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper for 'FFTW3' Includes: One-Dimensional Univariate, One-Dimensional Multivariate, and Two-Dimensional Transform

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.1.2
BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2

%description
Provides a wrapper for several 'FFTW' functions. This package provides
access to the two-dimensional 'FFT', the multivariate 'FFT', and the
one-dimensional real to complex 'FFT' using the 'FFTW3' library. The
package includes the functions fftw() and mvfftw() which are designed to
mimic the functionality of the R functions fft() and mvfft(). The 'FFT'
functions have a parameter that allows them to not return the redundant
complex conjugate when the input is real data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
