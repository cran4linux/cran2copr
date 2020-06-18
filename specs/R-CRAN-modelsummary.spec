%global packname  modelsummary
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Summary Tables for Statistical Models: Beautiful, Customizable,and Publication-Ready

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.6
BuildRequires:    R-CRAN-knitr >= 1.16
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-gt >= 0.2.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rmarkdown >= 1.6
Requires:         R-CRAN-knitr >= 1.16
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-gt >= 0.2.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
Create beautiful and customizable tables to summarize several statistical
models side-by-side. This package supports dozens of model types and can
produce tables in HTML, LaTeX, Markdown, Word, PowerPoint, Excel, RTF,
JPG, or PNG. Tables can easily be embedded in 'Rmarkdown' or 'knitr'
dynamic documents.

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
%{rlibdir}/%{packname}/INDEX
