%global packname  QuantumOps
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          3%{?dist}
Summary:          Performs Common Linear Algebra Operations Used in QuantumComputing and Implements Quantum Algorithms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
Contains basic structures and operations used frequently in quantum
computing. Intended to be a convenient tool to help learn quantum
mechanics and algorithms. Can create arbitrarily sized kets and bras and
implements quantum gates, inner products, and tensor products. Creates
arbitrarily controlled versions of all gates and can simulate complete or
partial measurements of kets. Has functionality to convert functions into
equivalent quantum gates and model quantum noise. Includes larger
applications, such as Steane error correction
<DOI:10.1103/physrevlett.77.793>, Quantum Fourier Transform and Shor's
algorithm (Shor 1999), Grover's algorithm (1996), Quantum Approximation
Optimization Algorithm (QAOA) (Farhi, Goldstone, and Gutmann 2014)
<arXiv:1411.4028>, and a variational quantum classifier (Schuld 2018)
<arXiv:1804.00633>. Can be used with the gridsynth algorithm
<arXiv:1212.6253> to perform decomposition into the Clifford+T set.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
