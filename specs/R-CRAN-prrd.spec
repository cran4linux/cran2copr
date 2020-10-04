%global packname  prrd
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Parallel Runs of Reverse Depends

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-liteq 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-config 
Requires:         R-CRAN-liteq 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 

%description
Reverse depends for a given package are queued such that multiple workers
can run the tests in parallel.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
