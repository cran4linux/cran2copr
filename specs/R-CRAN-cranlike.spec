%global __brp_check_rpaths %{nil}
%global packname  cranlike
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for 'CRAN'-Like Repositories

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-desc >= 1.1.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-debugme 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-desc >= 1.1.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-debugme 
Requires:         R-CRAN-RSQLite 
Requires:         R-tools 
Requires:         R-utils 

%description
A set of functions to manage 'CRAN'-like repositories efficiently.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
