%global packname  pedigreeTools
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Versatile Functions for Working with Pedigrees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-Matrix >= 1.0
BuildRequires:    R-methods 
Requires:         R-Matrix >= 1.0
Requires:         R-methods 

%description
Tools to sort, edit and prune pedigrees and to extract the inbreeding
coefficients and the relationship matrix (includes code for pedigrees from
self-pollinated species). The use of pedigree data is central to genetics
research within the animal and plant breeding communities to predict
breeding values. The relationship matrix between the individuals can be
derived from pedigree structure following the algorithms described for
example in Vazquez et al., 2010 <doi:10.2527/jas.2009-1952>.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
