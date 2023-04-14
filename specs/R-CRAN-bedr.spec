%global __brp_check_rpaths %{nil}
%global packname  bedr
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Genomic Region Processing using Tools Such as 'BEDTools','BEDOPS' and 'Tabix'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.10
BuildRequires:    R-CRAN-R.utils >= 2.0.2
BuildRequires:    R-CRAN-data.table >= 1.8.11
BuildRequires:    R-CRAN-VennDiagram >= 1.6.4
BuildRequires:    R-CRAN-testthat >= 0.7.1
BuildRequires:    R-parallel 
BuildRequires:    R-grid 
Requires:         R-CRAN-yaml >= 2.1.10
Requires:         R-CRAN-R.utils >= 2.0.2
Requires:         R-CRAN-data.table >= 1.8.11
Requires:         R-CRAN-VennDiagram >= 1.6.4
Requires:         R-CRAN-testthat >= 0.7.1
Requires:         R-parallel 
Requires:         R-grid 

%description
Genomic regions processing using open-source command line tools such as
'BEDTools', 'BEDOPS' and 'Tabix'. These tools offer scalable and efficient
utilities to perform genome arithmetic e.g indexing, formatting and
merging. bedr API enhances access to these tools as well as offers
additional utilities for genomic regions processing.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
