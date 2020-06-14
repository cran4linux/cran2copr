%global packname  SynchWave
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Synchrosqueezed Wavelet Transform

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13
Requires:         R-core >= 2.13
BuildRequires:    R-CRAN-fields >= 6.7
Requires:         R-CRAN-fields >= 6.7

%description
This package carries out synchrosqueezed wavelet transform. The package is
a translation of MATLAB Synchrosqueezing Toolbox, version 1.1 originally
developed by Eugene Brevdo (2012). The C code for curve_ext was authored
by Jianfeng Lu, and translated to Fortran by Dongik Jang. Synchrosqueezing
is based on the papers: [1] Daubechies, I., Lu, J. and Wu, H. T. (2011)
Synchrosqueezed wavelet transforms: An empirical mode decomposition-like
tool. Applied and Computational Harmonic Analysis, 30. 243-261. [2]
Thakur, G., Brevdo, E., Fukar, N. S. and Wu, H-T. (2013) The
Synchrosqueezing algorithm for time-varying spectral analysis: Robustness
properties and new paleoclimate applications. Signal Processing, 93,
1079-1094.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
