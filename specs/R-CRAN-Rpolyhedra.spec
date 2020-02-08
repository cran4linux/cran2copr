%global packname  Rpolyhedra
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Polyhedra Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-git2r 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-git2r 

%description
A polyhedra database scraped from various sources as R6 objects and 'rgl'
visualizing capabilities.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/genchangelog.sh
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
