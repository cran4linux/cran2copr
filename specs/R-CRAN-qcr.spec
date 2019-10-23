%global packname  qcr
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Quality Control Review

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-qcc 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-qualityTools 
BuildRequires:    R-MASS 
Requires:         R-CRAN-qcc 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-qualityTools 
Requires:         R-MASS 

%description
Allows to generate Shewhart-type charts and to obtain numerical results of
interest for a process quality control (involving continuous, attribute or
count data). This package provides basic functionality for univariable and
multivariable quality control analysis, including: xbar, xbar-one, S, R,
ewna, cusum, mewna, mcusum and T2 charts. Additionally have nonparametric
control charts multivariate. Parametric and nonparametric Process
Capability Indices.

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
%doc %{rlibdir}/%{packname}/CHANGES
%{rlibdir}/%{packname}/INDEX
