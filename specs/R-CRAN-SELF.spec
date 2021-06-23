%global __brp_check_rpaths %{nil}
%global packname  SELF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Structural Equation Embedded Likelihood Framework for CausalDiscovery

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-bnlearn >= 4.1
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-xgboost >= 0.6.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-CRAN-CompareCausalNetworks >= 0.1.0
Requires:         R-CRAN-bnlearn >= 4.1
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-xgboost >= 0.6.4
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-CompareCausalNetworks >= 0.1.0

%description
Provides the SELF criteria to learn causal structure. Please cite "Ruichu
Cai, Jie Qiao, Zhenjie Zhang, Zhifeng Hao. SELF: Structural Equational
Embedded Likelihood Framework for Causal Discovery. AAAI. 2018."

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
