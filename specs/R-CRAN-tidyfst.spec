%global packname  tidyfst
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          3%{?dist}
Summary:          Tidy Verbs for Fast Data Manipulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-fst >= 0.9.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-fst >= 0.9.0

%description
A toolkit of tidy data manipulation verbs with 'data.table' as the
backend. Combining the merits of syntax elegance from 'dplyr' and
computing performance from 'data.table', 'tidyfst' intends to provide
users with state-of-the-art data manipulation tools with least pain. This
package is an extension of 'data.table'. While enjoying a tidy syntax, it
also wraps combinations of efficient functions to facilitate
frequently-used data operations.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
