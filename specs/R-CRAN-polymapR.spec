%global packname  polymapR
%global packver   1.0.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.20
Release:          3%{?dist}
Summary:          Linkage Analysis in Outcrossing Polyploids

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-MDSMap 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-MDSMap 

%description
Creation of linkage maps in polyploid species from marker dosage scores of
an F1 cross from two heterozygous parents. Currently works for outcrossing
diploid, autotriploid, autotetraploid and autohexaploid species, as well
as segmental allotetraploids. Methods are described in a manuscript of
Bourke et al. (2018) <doi:10.1093/bioinformatics/bty371>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
