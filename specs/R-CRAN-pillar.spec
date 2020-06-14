%global packname  pillar
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          2%{?dist}
Summary:          Coloured Formatting for Columns

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-utf8 >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-vctrs >= 0.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fansi 
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-utf8 >= 1.1.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-vctrs >= 0.2.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fansi 

%description
Provides 'pillar' and 'colonnade' generics designed for formatting columns
of data using the full range of colours provided by modern terminals.

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
%{rlibdir}/%{packname}/INDEX
