%global packname  Lahman
%global packver   8.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Sean 'Lahman' Baseball Database

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-dplyr 

%description
Provides the tables from the 'Sean Lahman Baseball Database' as a set of R
data.frames. It uses the data on pitching, hitting and fielding
performance and other tables from 1871 through 2018, as recorded in the
2019 version of the database. Documentation examples show how many
baseball questions can be investigated.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/DESC-temp-change-maintainer.txt
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
