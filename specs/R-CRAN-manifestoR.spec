%global packname  manifestoR
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Access and Process Data and Documents of the Manifesto Project

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.11
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.12
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-CRAN-functional >= 0.6
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-dplyr >= 0.5
BuildRequires:    R-CRAN-DT >= 0.2
BuildRequires:    R-CRAN-NLP >= 0.1.3
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-zoo >= 1.7.11
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.12
Requires:         R-CRAN-tm >= 0.6
Requires:         R-CRAN-functional >= 0.6
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-dplyr >= 0.5
Requires:         R-CRAN-DT >= 0.2
Requires:         R-CRAN-NLP >= 0.1.3
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmltools 

%description
Provides access to coded election programmes from the Manifesto Corpus and
to the Manifesto Project's Main Dataset and routines to analyse this data.
The Manifesto Project <https://manifesto-project.wzb.eu> collects and
analyses election programmes across time and space to measure the
political preferences of parties. The Manifesto Corpus contains the
collected and annotated election programmes in the Corpus format of the
package 'tm' to enable easy use of text processing and text mining
functionality. Specific functions for scaling of coded political texts are
included.

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
