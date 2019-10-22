%global packname  RVenn
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Set Operations for Many Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods >= 3.5.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-vegan >= 2.5.2
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-pheatmap >= 1.0.10
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-ggforce >= 0.2.1
Requires:         R-methods >= 3.5.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-vegan >= 2.5.2
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-pheatmap >= 1.0.10
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-ggforce >= 0.2.1

%description
Set operations for many sets. The base functions for set operations in R
can be used for only two sets. This package uses 'purr' to find the union,
intersection and difference of three or more sets. This package also
provides functions for pairwise set operations among several sets.
Further, based on 'ggplot2' and 'ggforce', a Venn diagram can be drawn for
two or three sets. For bigger data sets, a clustered heatmap showing
presence/absence of the elements of the sets can be drawn based on the
'pheatmap' package. Finally, enrichment test can be applied to two sets
whether an overlap is statistically significant or not.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
