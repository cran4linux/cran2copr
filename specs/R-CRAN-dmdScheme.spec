%global packname  dmdScheme
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Domain Specific MetaData Scheme

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-readxl >= 1.2.0
BuildRequires:    R-CRAN-digest >= 0.6
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-tools 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-EML 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-readxl >= 1.2.0
Requires:         R-CRAN-digest >= 0.6
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-tools 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-EML 
Requires:         R-CRAN-stringr 

%description
Forms the core for developing own domain specific metadata schemes. It
contains the basic functionality needed for all metadata schemes based on
the 'dmdScheme'. See R.M. Krug and O.L. Petchey (2019)
<DOI:10.5281/zenodo.3581970>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/aaa.R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/index.md
%doc %{rlibdir}/%{packname}/reports
%doc %{rlibdir}/%{packname}/shiny_apps
%{rlibdir}/%{packname}/INDEX
