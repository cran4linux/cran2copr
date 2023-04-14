%global __brp_check_rpaths %{nil}
%global packname  elliptic
%global packver   1.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Weierstrass and Jacobi Elliptic Functions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pari
BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
A suite of elliptic and related functions including Weierstrass and Jacobi
forms.  Also includes various tools for manipulating and visualizing
complex functions.

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
