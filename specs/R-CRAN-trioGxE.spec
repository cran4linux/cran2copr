%global packname  trioGxE
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          A data smoothing approach to explore and test gene-environmentinteraction in case-parent trio data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-msm 
Requires:         R-mgcv 
Requires:         R-CRAN-gtools 

%description
The package contains functions that 1) estimates gene-environment
interaction between a SNP and a continuous non-genetic attribute by
fitting a generalized additive model to case-parent trio data, 2) produces
graphical displays of estimated interaction, 3) performs permutation test
of gene-environment interaction; 4) simulates informative case-parent
trios.

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
