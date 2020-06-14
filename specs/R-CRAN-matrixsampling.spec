%global packname  matrixsampling
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}
Summary:          Simulations of Matrix Variate Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-keep 
Requires:         R-stats 
Requires:         R-CRAN-keep 

%description
Provides samplers for various matrix variate distributions: Wishart,
inverse-Wishart, normal, t, inverted-t, Beta type I, Beta type II, Gamma,
confluent hypergeometric. Allows to simulate the noncentral Wishart
distribution without the integer restriction on the degrees of freedom.

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
%doc %{rlibdir}/%{packname}/BetaMatrix2.html
%doc %{rlibdir}/%{packname}/BetaMatrix2.Rmd
%doc %{rlibdir}/%{packname}/BetaMatrix3.html
%doc %{rlibdir}/%{packname}/BetaMatrix3.Rmd
%doc %{rlibdir}/%{packname}/BetaMatrix4.html
%doc %{rlibdir}/%{packname}/BetaMatrix4.Rmd
%{rlibdir}/%{packname}/INDEX
