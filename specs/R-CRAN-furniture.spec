%global packname  furniture
%global packver   1.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.7
Release:          3%{?dist}%{?buildtag}
Summary:          Furniture for Quantitative Scientists

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 

%description
Contains four main functions (i.e., four pieces of furniture): table1()
which produces a well-formatted table of descriptive statistics common as
Table 1 in research articles, tableC() which produces a well-formatted
table of correlations, tableF() which provides frequency counts, and
washer() which is helpful in cleaning up the data. These furniture-themed
functions are designed to simplify common tasks in quantitative analysis.
Other data summary and cleaning tools are also available.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
