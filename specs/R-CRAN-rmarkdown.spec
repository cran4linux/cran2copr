%global packname  rmarkdown
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Dynamic Documents for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-knitr >= 1.22
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-htmltools >= 0.3.5
BuildRequires:    R-CRAN-evaluate >= 0.13
BuildRequires:    R-CRAN-tinytex >= 0.11
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-methods 
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-knitr >= 1.22
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-evaluate >= 0.13
Requires:         R-CRAN-tinytex >= 0.11
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-xfun 
Requires:         R-methods 

%description
Convert R Markdown documents into a variety of formats.

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
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/rmd
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
