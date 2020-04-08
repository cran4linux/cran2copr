%global packname  metapower
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Power Analysis for Meta-Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-testthat >= 2.3.2
BuildRequires:    R-CRAN-rmarkdown >= 2.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-knitr >= 1.28
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-testthat >= 2.3.2
Requires:         R-CRAN-rmarkdown >= 2.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-knitr >= 1.28
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.5

%description
A simple and effective tool for computing meta-analytic statistical power
for main effects, tests of homogeneity, and categorical moderator models.
All equations are described in Pigott (2012)
<doi:10.1007/978-1-4614-2278-5>, Hedges & Pigott (2004)
<doi:10.1037/1082-989X.9.4.426>, and Borenstein, Hedges, Higgins, &
Rothstein (2009) <doi:10.1002/9780470743386>.

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
%doc %{rlibdir}/%{packname}/apa.csl
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/metapower.bib
%{rlibdir}/%{packname}/INDEX
