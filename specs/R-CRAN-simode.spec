%global packname  simode
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          Statistical Inference for Systems of Ordinary DifferentialEquations using Separable Integral-Matching

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-pracma 

%description
Implements statistical inference for systems of ordinary differential
equations, that uses the integral-matching criterion and takes advantage
of the separability of parameters, in order to obtain initial parameter
estimates for nonlinear least squares optimization. Dattner & Yaari (2018)
<arXiv:1807.04202>. Dattner et al. (2017) <doi:10.1098/rsif.2016.0525>.
Dattner & Klaassen (2015) <doi:10.1214/15-EJS1053>.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/joss
%doc %{rlibdir}/%{packname}/R_package_simode.Rnw
%doc %{rlibdir}/%{packname}/simode-manual.pdf
%{rlibdir}/%{packname}/INDEX
