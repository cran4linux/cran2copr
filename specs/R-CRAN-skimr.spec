%global packname  skimr
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Compact and Flexible Summaries of Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.2
BuildRequires:    R-CRAN-stringr >= 1.1
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-tidyr >= 0.7
BuildRequires:    R-CRAN-tibble >= 0.6
BuildRequires:    R-CRAN-tidyselect >= 0.2.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-knitr >= 1.2
Requires:         R-CRAN-stringr >= 1.1
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-tidyr >= 0.7
Requires:         R-CRAN-tibble >= 0.6
Requires:         R-CRAN-tidyselect >= 0.2.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
A simple to use summary function that can be used with pipes and displays
nicely in the console. The default summary statistics may be modified by
the user as can the default formatting. Support for data frames and
vectors is included, and users can implement their own skim methods for
specific object types as described in a vignette. Default summaries
include support for inline spark graphs. Instructions for managing these
on specific operating systems are given in the "Using skimr" vignette and
the README.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/other_docs
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
