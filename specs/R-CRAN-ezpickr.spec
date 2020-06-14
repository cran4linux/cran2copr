%global packname  ezpickr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}
Summary:          Easy Data Import Using GUI File Picker and SeamlessCommunication Between an Excel and R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-textreadr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-mboxr 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-textreadr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-mboxr 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 

%description
Choosing any rectangular data file using interactive GUI dialog box, and
seamlessly manipulating tidy data between an 'Excel' window and R session.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
