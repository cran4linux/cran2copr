%global packname  decompr
%global packver   4.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.0
Release:          3%{?dist}
Summary:          Global-Value-Chain Decomposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Two global-value-chain decompositions are implemented. Firstly, the
Wang-Wei-Zhu (Wang, Wei, and Zhu, 2013) algorithm splits bilateral gross
exports into 16 value-added components. Secondly, the Leontief
decomposition (default) derives the value added origin of exports by
country and industry, which is also based on Wang, Wei, and Zhu (Wang, Z.,
S.-J. Wei, and K. Zhu. 2013. "Quantifying International Production Sharing
at the Bilateral and Sector Levels.").

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
