%global packname  emdbook
%global packver   1.3.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.12
Release:          3%{?dist}%{?buildtag}
Summary:          Support Functions and Data for "Ecological Models and Data"

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-bbmle 
Requires:         R-MASS 
Requires:         R-lattice 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-bbmle 

%description
Auxiliary functions and data sets for "Ecological Models and Data", a book
presenting maximum likelihood estimation and related topics for ecologists
(ISBN 978-0-691-12522-0).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/BUGS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/misc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
