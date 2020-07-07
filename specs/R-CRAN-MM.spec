%global packname  MM
%global packver   1.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          3%{?dist}
Summary:          The Multiplicative Multinomial Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions >= 1.9.14
BuildRequires:    R-CRAN-magic >= 1.5.6
BuildRequires:    R-CRAN-Oarray >= 1.4.6
BuildRequires:    R-CRAN-emulator >= 1.2.13
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
Requires:         R-CRAN-partitions >= 1.9.14
Requires:         R-CRAN-magic >= 1.5.6
Requires:         R-CRAN-Oarray >= 1.4.6
Requires:         R-CRAN-emulator >= 1.2.13
Requires:         R-CRAN-abind 
Requires:         R-methods 

%description
Various utilities for the Multiplicative Multinomial distribution.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
