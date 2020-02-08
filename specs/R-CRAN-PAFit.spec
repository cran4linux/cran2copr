%global packname  PAFit
%global packver   1.0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.7
Release:          1%{?dist}
Summary:          Generative Mechanism Estimation in Temporal Complex Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-magicaxis 
BuildRequires:    R-CRAN-networkDynamic 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-VGAM 
Requires:         R-MASS 
Requires:         R-CRAN-magicaxis 
Requires:         R-CRAN-networkDynamic 
Requires:         R-CRAN-network 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-knitr 
Requires:         R-methods 

%description
Statistical methods for estimating preferential attachment and node
fitness generative mechanisms in temporal complex networks are provided.
Thong Pham et al. (2015) <doi:10.1371/journal.pone.0137796>. Thong Pham et
al. (2016) <doi:10.1038/srep32558>.

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
