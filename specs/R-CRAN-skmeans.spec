%global packname  skmeans
%global packver   0.2-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          3%{?dist}
Summary:          Spherical k-Means Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-clue >= 0.3.39
BuildRequires:    R-CRAN-slam >= 0.1.31
BuildRequires:    R-cluster 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-clue >= 0.3.39
Requires:         R-CRAN-slam >= 0.1.31
Requires:         R-cluster 
Requires:         R-stats 
Requires:         R-utils 

%description
Algorithms to compute spherical k-means partitions. Features several
methods, including a genetic and a fixed-point algorithm and an interface
to the CLUTO vcluster program.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/cluto
%{rlibdir}/%{packname}/INDEX
