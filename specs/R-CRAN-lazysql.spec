%global __brp_check_rpaths %{nil}
%global packname  lazysql
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Lazy SQL Programming

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.7.2
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-checkmate >= 1.7.2
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 

%description
Helper functions to build SQL statements for dbGetQuery or dbSendQuery
under program control. They are intended to increase speed of coding and
to reduce coding errors. Arguments are carefully checked, in particular
SQL identifiers such as names of tables or columns. More patterns will be
added as required.

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
