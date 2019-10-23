%global packname  msaenet
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}
Summary:          Multi-Step Adaptive Estimation Methods for Sparse Regressions

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ncvreg >= 3.8.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-survival 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-ncvreg >= 3.8.0
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mvtnorm 
Requires:         R-survival 
Requires:         R-Matrix 

%description
Multi-step adaptive elastic-net (MSAENet) algorithm for feature selection
in high-dimensional regressions proposed in Xiao and Xu (2015)
<DOI:10.1080/00949655.2015.1016944>, with support for multi-step adaptive
MCP-net (MSAMNet) and multi-step adaptive SCAD-net (MSASNet) methods.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
