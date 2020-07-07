%global packname  getTBinR
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}
Summary:          Access and Summarise World Health Organization Tuberculosis Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.2.1
BuildRequires:    R-CRAN-ggthemes >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.1
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-viridis >= 0.5.1
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-grDevices 
Requires:         R-CRAN-plotly >= 4.9.2.1
Requires:         R-CRAN-ggthemes >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.3.1
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-viridis >= 0.5.1
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-grDevices 

%description
Quickly and easily import analysis ready Tuberculosis (TB) burden data,
from the World Health Organization (WHO), into R. The aim of getTBinR is
to allow researchers, and other interested individuals, to quickly and
easily gain access to a detailed TB data set and to start using it to
derive key insights. It provides a consistent set of tools that can be
used to rapidly evaluate hypotheses on a widely used data set before they
are explored further using more complex methods or more detailed data.
These tools include: generic plotting and mapping functions; a data
dictionary search tool; an interactive shiny dashboard; and an automated,
country level, TB report. For newer R users, this package reduces the
barrier to entry by handling data import, munging, and visualisation. All
plotting and mapping functions are built with ggplot2 so can be readily
extended.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
