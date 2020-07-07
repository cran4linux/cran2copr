%global packname  scrubr
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          Clean Biological Occurrence Records

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-qlcMatrix 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-curl 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-qlcMatrix 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-curl 

%description
Clean biological occurrence records. Includes functionality for cleaning
based on various aspects of spatial coordinates, unlikely values due to
political 'centroids', coordinates based on where collections of specimens
are held, and more.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/ignore
%{rlibdir}/%{packname}/INDEX
