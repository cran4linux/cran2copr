%global packname  ShiftConvolvePoibin
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Exactly Computing the Tail of the Poisson-Binomial Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
An exact method for computing the Poisson-Binomial Distribution (PBD). The
package provides a function for generating a random sample from the PBD,
as well as two distinct approaches for computing the density,
distribution, and quantile functions of the PBD. The first method uses
direct-convolution, or a dynamic-programming approach which is numerically
stable but can be slow for a large input due to its quadratic complexity.
The second method is much faster on large inputs thanks to its use of Fast
Fourier Transform (FFT) based convolutions. Notably in this case the
package uses an exponential shift to practically guarantee the relative
accuracy of the computation of an arbitrarily small tail of the PBD --
something that FFT-based methods often struggle with. This
ShiftConvolvePoiBin method is described in Peres, Lee and Keich (2020)
<arXiv:2004.07429> where it is also shown to be competitive with the
fastest implementations for exactly computing the entire Poisson-Binomial
distribution.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
