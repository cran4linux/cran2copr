%global packname  styler
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Non-Invasive Pretty Printing of R Code

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rematch2 >= 2.0.1
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-backports >= 1.1.0
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-rprojroot >= 1.1
BuildRequires:    R-CRAN-magrittr >= 1.0.1
BuildRequires:    R-CRAN-withr >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-rlang >= 0.1.1
BuildRequires:    R-CRAN-xfun >= 0.1
BuildRequires:    R-tools 
Requires:         R-CRAN-rematch2 >= 2.0.1
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-backports >= 1.1.0
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-rprojroot >= 1.1
Requires:         R-CRAN-magrittr >= 1.0.1
Requires:         R-CRAN-withr >= 1.0.0
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-rlang >= 0.1.1
Requires:         R-CRAN-xfun >= 0.1
Requires:         R-tools 

%description
Pretty-prints R code without changing the user's formatting intent.

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
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
