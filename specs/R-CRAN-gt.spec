%global packname  gt
%global packver   0.2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.5
Release:          1%{?dist}
Summary:          Easily Create Presentation-Ready Display Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-commonmark >= 1.7
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-fs >= 1.3.2
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-htmltools >= 0.4.0
BuildRequires:    R-CRAN-sass >= 0.1.1
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-commonmark >= 1.7
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-fs >= 1.3.2
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-htmltools >= 0.4.0
Requires:         R-CRAN-sass >= 0.1.1

%description
Build display tables from tabular data using with an easy-to-use API. With
its progressive approach, we can construct display tables with a clear
separation of concerns: you don't have to decide how the tabular data gets
transformed and structured whilst also worrying about aesthetics.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/css
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/graphics
%{rlibdir}/%{packname}/INDEX
