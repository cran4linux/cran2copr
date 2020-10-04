%global packname  parsemsf
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Parse ThermoFisher MSF Files and Estimate Protein Abundances

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-RSQLite >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-stats 
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-RSQLite >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-lazyeval 
Requires:         R-stats 

%description
Provides functions for parsing ThermoFisher MSF files produced by Proteome
Discoverer 1.4.x (see <https://thermofisher.com> for more information).
This package makes it easy to view individual peptide information,
including peak areas, and to map peptides to locations within the parent
protein sequence. This package also estimates protein abundances from peak
areas and across multiple technical replicates. The author of this package
is not affiliated with ThermoFisher Scientific in any way.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
