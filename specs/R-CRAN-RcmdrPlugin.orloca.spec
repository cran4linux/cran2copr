%global packname  RcmdrPlugin.orloca
%global packver   4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7
Release:          2%{?dist}
Summary:          A GUI for Planar Location Problems

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-orloca >= 4.6
BuildRequires:    R-CRAN-orloca.es >= 4.6
BuildRequires:    R-CRAN-Rcmdr 
Requires:         R-CRAN-orloca >= 4.6
Requires:         R-CRAN-orloca.es >= 4.6
Requires:         R-CRAN-Rcmdr 

%description
A GUI for the orloca package is provided as a Rcmdr plug-in. The package
deals with planar location problems.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
