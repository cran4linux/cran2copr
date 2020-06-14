%global packname  goeveg
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          2%{?dist}
Summary:          Functions for Community Data and Ordinations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-cluster 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-fields 
Requires:         R-mgcv 
Requires:         R-CRAN-Hmisc 
Requires:         R-cluster 

%description
A collection of functions useful in (vegetation) community analyses and
ordinations. Includes automatic species selection for ordination diagrams,
species response curves and rank-abundance curves as well as calculation
and sorting of synoptic tables.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
