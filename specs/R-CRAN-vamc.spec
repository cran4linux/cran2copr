%global packname  vamc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          A Monte Carlo Valuation Framework for Variable Annuities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.0
BuildRequires:    R-utils >= 3.3.0
BuildRequires:    R-CRAN-Rdpack >= 0.4
Requires:         R-stats >= 3.3.0
Requires:         R-utils >= 3.3.0
Requires:         R-CRAN-Rdpack >= 0.4

%description
Implementation of a Monte Carlo simulation engine for valuing synthetic
portfolios of variable annuities, which reflect realistic features of
common annuity contracts in practice. It aims to facilitate the
development and dissemination of research related to the efficient
valuation of a portfolio of large variable annuities. The main valuation
methodology was proposed by Gan (2017) <doi:10.1515/demo-2017-0021>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
