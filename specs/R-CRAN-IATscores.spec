%global packname  IATscores
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Implicit Association Test Scores Using Robust Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.4.1
BuildRequires:    R-CRAN-qgraph >= 1.4.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.2
Requires:         R-methods >= 3.4.1
Requires:         R-CRAN-qgraph >= 1.4.4
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.7.2

%description
Compute several variations of the Implicit Association Test (IAT) scores,
including the D scores (Greenwald, Nosek, Banaji, 2003,
<doi:10.1037/0022-3514.85.2.197>) and the new scores that were developed
using robust statistics (Richetin, Costantini, Perugini, and Schonbrodt,
2015, <doi:10.1371/journal.pone.0129601>).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
