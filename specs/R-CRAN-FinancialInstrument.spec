%global __brp_check_rpaths %{nil}
%global packname  FinancialInstrument
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Financial Instrument Model Infrastructure and Meta-Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.5
BuildRequires:    R-CRAN-quantmod >= 0.4.3
BuildRequires:    R-CRAN-xts >= 0.10.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-TTR 
Requires:         R-CRAN-zoo >= 1.7.5
Requires:         R-CRAN-quantmod >= 0.4.3
Requires:         R-CRAN-xts >= 0.10.0
Requires:         R-methods 
Requires:         R-CRAN-TTR 

%description
Infrastructure for defining meta-data and relationships for financial
instruments.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/parser
%doc %{rlibdir}/%{packname}/tests
%doc %{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/INDEX
