%global packname  datastepr
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          2%{?dist}
Summary:          An Implementation of a SAS-Style Data Step

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.0.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
Requires:         R-CRAN-R6 >= 2.0.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-lazyeval >= 0.1.10

%description
Based on a SAS data step. This allows for row-wise dynamic building of
data, iteratively importing slices of existing dataframes, conducting
analyses, and exporting to a results frame. This is particularly useful
for differential or time-series analyses, which are often not well suited
to vector- based operations.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
