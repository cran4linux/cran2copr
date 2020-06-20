%global packname  IATscores
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}
Summary:          Implicit Association Test Scores Using Robust Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.4.1
BuildRequires:    R-CRAN-qgraph >= 1.6.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
Requires:         R-methods >= 3.4.1
Requires:         R-CRAN-qgraph >= 1.6.5
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 0.8.5

%description
Compute several variations of the Implicit Association Test (IAT) scores,
including the D scores (Greenwald, Nosek, Banaji, 2003,
<doi:10.1037/0022-3514.85.2.197>) and the new scores that were developed
using robust statistics (Richetin, Costantini, Perugini, and Schonbrodt,
2015, <doi:10.1371/journal.pone.0129601>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
