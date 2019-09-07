%global packname  netchain
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Inferring Causal Effects on Collective Outcomes underInterference

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-Matrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-igraph 

%description
In networks, treatments may spill over from the treated individual to his
or her social contacts and outcomes may be contagious over time. Under
this setting, causal inference on the collective outcome observed over all
network is often of interest. We use chain graph models approximating the
projection of the full longitudinal data onto the observed data to
identify the causal effect of the intervention on the whole outcome.
Justification of such approximation is demonstrated in Ogburn et al.
(2018) <arXiv:1812.04990>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
