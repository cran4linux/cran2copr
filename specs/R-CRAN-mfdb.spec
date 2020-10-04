%global packname  mfdb
%global packver   6.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          MareFrame DB Querying Library

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-logging >= 0.7.103
BuildRequires:    R-CRAN-RPostgreSQL >= 0.4
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-CRAN-getPass >= 0.1.1
Requires:         R-CRAN-logging >= 0.7.103
Requires:         R-CRAN-RPostgreSQL >= 0.4
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-CRAN-getPass >= 0.1.1

%description
Creates and manages a PostgreSQL database suitable for storing fisheries
data and aggregating ready for use within a Gadget
<https://hafro.github.io/gadget> model. See
<https://mareframe.github.io/mfdb> for more information.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo-data
%{rlibdir}/%{packname}/INDEX
