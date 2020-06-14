%global packname  CMatching
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          2%{?dist}
Summary:          Matching Algorithms for Causal Inference with Clustered Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-multiwayvcov 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-Matching 
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-multiwayvcov 
Requires:         R-CRAN-lme4 

%description
Provides functions to perform matching algorithms for causal inference
with clustered data, as described in B. Arpino and M. Cannas (2016)
<doi:10.1002/sim.6880>. Pure within-cluster and preferential
within-cluster matching are implemented. Both algorithms provide causal
estimates with cluster-adjusted estimates of standard errors.

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
