%global packname  quantoptr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Algorithms for Quantile- And Mean-Optimal Treatment Regimes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rgenoud >= 5.7
BuildRequires:    R-CRAN-quantreg >= 5.18
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-rgenoud >= 5.7
Requires:         R-CRAN-quantreg >= 5.18
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 

%description
Estimation methods for optimal treatment regimes under three different
criteria, namely marginal quantile, marginal mean, and mean absolute
difference. For the first two criteria, both one-stage and two-stage
estimation method are implemented. A doubly robust estimator for
estimating the quantile-optimal treatment regime is also included.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
