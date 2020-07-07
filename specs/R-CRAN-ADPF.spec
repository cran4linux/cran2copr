%global packname  ADPF
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Use Least Squares Polynomial Regression and Statistical Testingto Improve Savitzky-Golay

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
This function takes a vector or matrix of data and smooths the data with
an improved Savitzky Golay transform. The Savitzky-Golay method for data
smoothing and differentiation calculates convolution weights using Gram
polynomials that exactly reproduce the results of least-squares polynomial
regression. Use of the Savitzky-Golay method requires specification of
both filter length and polynomial degree to calculate convolution weights.
For maximum smoothing of statistical noise in data, polynomials with low
degrees are desirable, while a high polynomial degree is necessary for
accurate reproduction of peaks in the data. Extension of the least-squares
regression formalism with statistical testing of additional terms of
polynomial degree to a heuristically chosen minimum for each data window
leads to an adaptive-degree polynomial filter (ADPF). Based on noise
reduction for data that consist of pure noise and on signal reproduction
for data that is purely signal, ADPF performed nearly as well as the
optimally chosen fixed-degree Savitzky-Golay filter and outperformed
sub-optimally chosen Savitzky-Golay filters. For synthetic data consisting
of noise and signal, ADPF outperformed both optimally chosen and
sub-optimally chosen fixed-degree Savitzky-Golay filters. See Barak, P.
(1995) <doi:10.1021/ac00113a006> for more information.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
