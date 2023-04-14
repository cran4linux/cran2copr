%global __brp_check_rpaths %{nil}
%global packname  kimisc
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Kirill's Miscellaneous Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-pryr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-pryr 

%description
A collection of useful functions not found anywhere else, mainly for
programming: Pretty intervals, generalized lagged differences, checking
containment in an interval, and an alternative interface to assign().

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
