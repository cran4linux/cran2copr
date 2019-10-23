%global packname  zipfextR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Zipf Extended Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.1
Requires:         R-core >= 2.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tolerance >= 1.2.0
BuildRequires:    R-CRAN-copula >= 0.999.18
BuildRequires:    R-CRAN-VGAM >= 0.9.8
Requires:         R-CRAN-tolerance >= 1.2.0
Requires:         R-CRAN-copula >= 0.999.18
Requires:         R-CRAN-VGAM >= 0.9.8

%description
Implementation of four extensions of the Zipf distribution: the
Marshall-Olkin Extended Zipf (MOEZipf) Pérez-Casany, M., & Casellas, A.
(2013) <arXiv:1304.4540>, the Zipf-Poisson Extreme (Zipf-PE), the
Zipf-Poisson Stopped Sum (Zipf-PSS) and the Zipf-Polylog distributions. In
log-log scale, the two first extensions allow for top-concavity and
top-convexity while the third one only allows for top-concavity. All the
extensions maintain the linearity associated with the Zipf model in the
tail.

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
