%global packname  hillR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Diversity Through Hill Numbers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-tibble 

%description
Calculate taxonomic, functional and phylogenetic diversity measures
through Hill Numbers proposed by Chao, Chiu and Jost (2014)
<doi:10.1146/annurev-ecolsys-120213-091540>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
