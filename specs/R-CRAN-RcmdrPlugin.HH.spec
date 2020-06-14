%global packname  RcmdrPlugin.HH
%global packver   1.1-47
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.47
Release:          2%{?dist}
Summary:          Rcmdr Support for the HH Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.0.0
BuildRequires:    R-CRAN-HH 
BuildRequires:    R-lattice 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-Rcmdr >= 2.0.0
Requires:         R-CRAN-HH 
Requires:         R-lattice 
Requires:         R-mgcv 

%description
Rcmdr menu support for many of the functions in the HH package. The focus
is on menu items for functions we use in our introductory courses.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
