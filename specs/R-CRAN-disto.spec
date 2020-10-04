%global packname  disto
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Unified Interface to Distance, Dissimilarity, SimilarityMatrices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-pbapply >= 1.3.4
BuildRequires:    R-CRAN-fastcluster >= 1.1.25
BuildRequires:    R-CRAN-fastmatch >= 1.1.0
BuildRequires:    R-CRAN-factoextra >= 1.0.5
BuildRequires:    R-CRAN-tidyr >= 0.8.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-broom >= 0.4.4
BuildRequires:    R-CRAN-proxy >= 0.4.19
BuildRequires:    R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-pbapply >= 1.3.4
Requires:         R-CRAN-fastcluster >= 1.1.25
Requires:         R-CRAN-fastmatch >= 1.1.0
Requires:         R-CRAN-factoextra >= 1.0.5
Requires:         R-CRAN-tidyr >= 0.8.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-broom >= 0.4.4
Requires:         R-CRAN-proxy >= 0.4.19
Requires:         R-CRAN-assertthat >= 0.2.0

%description
Provides a high level API to interface over sources storing distance,
dissimilarity, similarity matrices with matrix style extraction,
replacement and other utilities. Currently, in-memory dist object backend
is supported.

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
%{rlibdir}/%{packname}/INDEX
