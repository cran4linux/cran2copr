%global __brp_check_rpaths %{nil}
%global packname  SEMID
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Identifiability of Linear Structural Equation Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils >= 2.3.0
BuildRequires:    R-CRAN-R.oo >= 1.20.0
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-R.methodsS3 
Requires:         R-CRAN-R.utils >= 2.3.0
Requires:         R-CRAN-R.oo >= 1.20.0
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-R.methodsS3 

%description
Provides routines to check identifiability or non-identifiability of
linear structural equation models as described in Drton, Foygel, and
Sullivant (2011) <DOI:10.1214/10-AOS859>, Foygel, Draisma, and Drton
(2012) <DOI:10.1214/12-AOS1012>, and other works. The routines are based
on the graphical representation of structural equation models by a path
diagram/mixed graph.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
