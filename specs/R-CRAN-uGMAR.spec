%global packname  uGMAR
%global packver   3.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.5
Release:          2%{?dist}
Summary:          Estimate Univariate Gaussian or Student's t MixtureAutoregressive Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-pbapply >= 1.3.2
BuildRequires:    R-CRAN-Brobdingnag >= 1.2.4
BuildRequires:    R-parallel 
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-pbapply >= 1.3.2
Requires:         R-CRAN-Brobdingnag >= 1.2.4
Requires:         R-parallel 

%description
Maximum likelihood estimation of univariate Gaussian Mixture
Autoregressive (GMAR), Student's t Mixture Autoregressive (StMAR), and
Gaussian and Student's t Mixture Autoregressive (G-StMAR) models, quantile
residual tests, graphical diagnostics, forecast and simulate from GMAR,
StMAR and G-StMAR processes. Leena Kalliovirta, Mika Meitz, Pentti
Saikkonen (2015) <doi:10.1111/jtsa.12108>, Mika Meitz, Daniel Preve,
Pentti Saikkonen (2018) <arXiv:1805.04010>, Savi Virolainen (2020)
<arXiv:2003.05221>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
