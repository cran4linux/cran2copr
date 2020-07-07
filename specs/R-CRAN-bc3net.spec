%global packname  bc3net
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}
Summary:          Gene Regulatory Network Inference with Bc3net

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-c3net 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-lattice 
Requires:         R-CRAN-c3net 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-lattice 

%description
Implementation of the BC3NET algorithm for gene regulatory network
inference (de Matos Simoes and Frank Emmert-Streib, Bagging Statistical
Network Inference from Large-Scale Gene Expression Data, PLoS ONE 7(3):
e33624, <doi:10.1371/journal.pone.0033624>).

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
%{rlibdir}/%{packname}/INDEX
