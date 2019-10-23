%global packname  PIGE
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Self Contained Gene Set Analysis for Gene- AndPathway-Environment Interaction Analysis

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-ARTP 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-survival 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-ARTP 
Requires:         R-CRAN-xtable 
Requires:         R-survival 

%description
Extension of the 'ARTP' package (Yu, K., et al. (2009)
<doi:10.1002/gepi.20422>) for gene- and pathway-environment interaction. A
permutation and a parametric bootstrap approaches have been implemented
for investigating gene- and pathway-environment interaction analysis
(Truong, T., et al. (2014) <doi:10.1530/ERC-14-0121>).

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
%doc %{rlibdir}/%{packname}/sampleData
%{rlibdir}/%{packname}/INDEX
