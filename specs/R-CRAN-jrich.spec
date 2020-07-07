%global packname  jrich
%global packver   0.60-35
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.60.35
Release:          3%{?dist}
Summary:          Jack-Knife Support for Evolutionary Distinctiveness Indices Iand W

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-ape 

%description
These functions calculate the taxonomic measures presented in
Miranda-Esquivel (2016). The package introduces Jack-knife resampling in
evolutionary distinctiveness prioritization analysis, as a way to evaluate
the support of the ranking in area prioritization, and the persistence of
a given area in a conservation analysis. The algorithm is described in:
Miranda-Esquivel, D (2016) <DOI:10.1007/978-3-319-22461-9_11>.

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
%{rlibdir}/%{packname}/exdata
%{rlibdir}/%{packname}/INDEX
