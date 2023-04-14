%global __brp_check_rpaths %{nil}
%global packname  pacman
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Package Management Tool

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-remotes 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools to more conveniently perform tasks associated with add-on packages.
pacman conveniently wraps library and package related functions and names
them in an intuitive and consistent fashion.  It seeks to combine
functionality from lower level functions which can speed up workflow.

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
