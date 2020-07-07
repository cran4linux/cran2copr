%global packname  ASMap
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}
Summary:          Linkage Map Construction using the MSTmap Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-lattice 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-lattice 

%description
Functions for Accurate and Speedy linkage map construction, manipulation
and diagnosis of Doubled Haploid, Backcross and Recombinant Inbred 'R/qtl'
objects. This includes extremely fast linkage map clustering and optimal
marker ordering using 'MSTmap' (see Wu et al.,2008).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
