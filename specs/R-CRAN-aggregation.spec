%global packname  aggregation
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          p-Value Aggregation Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Contains functionality for performing the following methods of p-value
aggregation: Fisher's method [Fisher, RA (1932, ISBN: 9780028447308)], the
Lancaster method (weighted Fisher's method) [Lancaster, HO (1961,
<doi:10.1111/j.1467-842X.1961.tb00058.x>)], and Sidak correction [Sidak, Z
(1967, <doi:10.1080/01621459.1967.10482935>)].  Please cite Yi et al., the
manuscript corresponding to this package [Yi, L et al., (2017),
<doi:10.1101/190199>].

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
