%global packname  IndexConstruction
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Index Construction for Time Series Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-RcppBDT 
BuildRequires:    R-CRAN-zoo 
Requires:         R-KernSmooth 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-RcppBDT 
Requires:         R-CRAN-zoo 

%description
Derivation of indexes for benchmarking purposes. A methodology with
flexible number of constituents is implemented. Also functions for market
capitalization and volume weighted indexes with fixed number of
constituents are available. The main function of the package, indexComp(),
provides the derived index, suitable for analysis purposes. The functions
indexUpdate(), indexMemberSelection() and indexMembersUpdate() are
components of indexComp() and enable one to construct and continuously
update an index, e.g. for display on a website. The methodology behind the
functions provided gets introduced in Trimborn and Haerdle (2018)
<doi:10.1016/j.jempfin.2018.08.004>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
