%global packname  tidymodels
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Easily Install and Load the 'Tidymodels' Packages

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-pillar >= 1.4.2
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-broom >= 0.5.2
BuildRequires:    R-CRAN-infer >= 0.5.0
BuildRequires:    R-CRAN-tidypredict >= 0.4.3
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-tidytext >= 0.2.2
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-CRAN-recipes >= 0.1.7
BuildRequires:    R-CRAN-rsample >= 0.0.5
BuildRequires:    R-CRAN-yardstick >= 0.0.4
BuildRequires:    R-CRAN-parsnip >= 0.0.3.1
BuildRequires:    R-CRAN-dials >= 0.0.3
BuildRequires:    R-CRAN-tidyposterior >= 0.0.2
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-pillar >= 1.4.2
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-broom >= 0.5.2
Requires:         R-CRAN-infer >= 0.5.0
Requires:         R-CRAN-tidypredict >= 0.4.3
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-tidytext >= 0.2.2
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-recipes >= 0.1.7
Requires:         R-CRAN-rsample >= 0.0.5
Requires:         R-CRAN-yardstick >= 0.0.4
Requires:         R-CRAN-parsnip >= 0.0.3.1
Requires:         R-CRAN-dials >= 0.0.3
Requires:         R-CRAN-tidyposterior >= 0.0.2

%description
The tidy modeling "verse" is a collection of packages for modeling and
statistical analysis that share the underlying design philosophy, grammar,
and data structures of the tidyverse.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
