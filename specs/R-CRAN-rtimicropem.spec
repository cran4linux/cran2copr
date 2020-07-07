%global packname  rtimicropem
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}
Summary:          Supports the Analysis of RTI MicroPEM Output Files

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rbokeh 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rbokeh 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Supports the input and reproducible analysis of RTI MicroPEM output files.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/batchtestfiles
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
