%global packname  fftwtools
%global packver   0.9-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          3%{?dist}
Summary:          Wrapper for 'FFTW3' Includes: One-Dimensional Univariate,One-Dimensional Multivariate, and Two-Dimensional Transform

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.1.2
Requires:         fftw
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


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
