%global packname  BrailleR
%global packver   0.30.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.30.2
Release:          1%{?dist}
Summary:          Improved Access for Blind Users

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python3dist(wxpython) >= 4
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-gridSVG 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-roloc 
BuildRequires:    R-CRAN-rolocISCCNBS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-gridSVG 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-roloc 
Requires:         R-CRAN-rolocISCCNBS 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xtable 

%description
Blind users do not have access to the graphical output from R without
printing the content of graphics windows to an embosser of some kind. This
is not as immediate as is required for efficient access to statistical
output. The functions here are created so that blind people can make even
better use of R. This includes the text descriptions of graphs,
convenience functions to replace the functionality offered in many GUI
front ends, and experimental functionality for optimising graphical
content to prepare it for embossing as tactile images.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fonts
%doc %{rlibdir}/%{packname}/MyBrailleR
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/Python
%doc %{rlibdir}/%{packname}/Sound
%doc %{rlibdir}/%{packname}/Templates
%doc %{rlibdir}/%{packname}/Web
%doc %{rlibdir}/%{packname}/whisker
%{rlibdir}/%{packname}/INDEX
