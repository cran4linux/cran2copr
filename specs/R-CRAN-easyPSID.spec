%global packname  easyPSID
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Reading, Formatting, and Organizing the Panel Study of IncomeDynamics (PSID)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-foreign >= 0.8.67
BuildRequires:    R-CRAN-LaF >= 0.6.0
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-foreign >= 0.8.67
Requires:         R-CRAN-LaF >= 0.6.0

%description
Provides various functions for reading and preparing the Panel Study of
Income Dynamics (PSID) for longitudinal analysis, including functions that
read the PSID's fixed width format files directly into R, rename all of
the PSID's longitudinal variables so that recurring variables have
consistent names across years, simplify assembling longitudinal datasets
from cross sections of the PSID Family Files, and export the resulting
PSID files into file formats common among other statistical programming
languages ('SAS', 'STATA', and 'SPSS').

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
