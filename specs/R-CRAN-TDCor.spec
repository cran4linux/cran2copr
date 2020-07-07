%global packname  TDCor
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Gene Network Inference from Time-Series Transcriptomic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-parallel 
Requires:         R-CRAN-deSolve 
Requires:         R-parallel 

%description
The Time-Delay Correlation algorithm (TDCor) reconstructs the topology of
a gene regulatory network (GRN) from time-series transcriptomic data.  The
algorithm is described in details in Lavenus et al., Plant Cell, 2015.  It
was initially developed to infer the topology of the GRN controlling
lateral root formation in Arabidopsis thaliana.  The time-series
transcriptomic dataset which was used in this study is included in the
package to illustrate how to use it.

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
