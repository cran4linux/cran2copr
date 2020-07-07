%global packname  ctv
%global packver   0.8-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          3%{?dist}
Summary:          CRAN Task Views

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Infrastructure for task views to CRAN-style repositories: Querying task
views and installing the associated packages (client-side tools),
generating HTML pages and storing task view information in the repository
(server-side tools).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/ctv
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
