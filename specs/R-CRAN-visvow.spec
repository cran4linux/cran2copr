%global packname  visvow
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}
Summary:          Visible Vowels: Visualization of Vowel Variation

License:          GNU General Public License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-WriteXLS 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-splitstackshape 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 
Requires:         R-MASS 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-WriteXLS 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-plyr 
Requires:         R-grid 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-Rdpack 

%description
Visualizes vowel variation in f0, F1, F2, F3 and duration.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/email.png
%doc %{rlibdir}/%{packname}/example.xlsx
%doc %{rlibdir}/%{packname}/FA.jpg
%doc %{rlibdir}/%{packname}/format.png
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/visvow.pdf
%{rlibdir}/%{packname}/INDEX
