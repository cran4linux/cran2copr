%global packname  hrbrthemes
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          Additional Themes, Theme Components and Utilities for 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-gdtools 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-htmltools 
Requires:         R-tools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-gdtools 

%description
A compilation of extra 'ggplot2' themes, scales and utilities, including a
spell check function for plot label fields and an overall emphasis on
typography. A copy of the 'Google' font 'Roboto Condensed'
<https://github.com/google/roboto/> is also included along with a copy of
the 'IBM' 'Plex Sans' <https://github.com/IBM/type>, 'Titillium Web'
<https://fonts.google.com/specimen/Titillium+Web>, and 'Public Sans'
<https://github.com/uswds/public-sans/> fonts are also included to support
their respective typography-oriented themes.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fonts
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
