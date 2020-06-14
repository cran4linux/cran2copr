%global packname  BiBitR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          R Wrapper for Java Implementation of BiBit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-foreign 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-lattice 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-biclust 
Requires:         R-stats 
Requires:         R-foreign 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-viridis 
Requires:         R-cluster 
Requires:         R-CRAN-dendextend 
Requires:         R-lattice 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-biclust 

%description
A simple R wrapper for the Java BiBit algorithm from "A biclustering
algorithm for extracting bit-patterns from binary datasets" from Domingo
et al. (2011) <DOI:10.1093/bioinformatics/btr464>. An simple adaption for
the BiBit algorithm which allows noise in the biclusters is also
introduced as well as a function to guide the algorithm towards given
(sub)patterns. Further, a workflow to derive noisy biclusters from
discoverd larger column patterns is included as well.

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
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
