%global packname  corrr
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Correlations in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.4.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-tibble >= 2.0
BuildRequires:    R-CRAN-seriation >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-ggrepel >= 0.6.5
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.2.2
Requires:         R-methods >= 3.4.3
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-tibble >= 2.0
Requires:         R-CRAN-seriation >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-ggrepel >= 0.6.5
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.2.2

%description
A tool for exploring correlations. It makes it possible to easily perform
routine tasks when exploring correlation matrices such as ignoring the
diagonal, focusing on the correlations of certain variables against
others, or rearranging and visualizing the matrix in terms of the strength
of the correlations.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
