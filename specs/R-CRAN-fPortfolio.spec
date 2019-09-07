%global packname  fPortfolio
%global packver   3042.83
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3042.83
Release:          1%{?dist}
Summary:          Rmetrics - Portfolio Selection and Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-fAssets 
BuildRequires:    R-CRAN-fCopulae 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-rneos 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-fAssets 
Requires:         R-CRAN-fCopulae 
Requires:         R-CRAN-robustbase 
Requires:         R-MASS 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-rneos 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a collection of functions to optimize portfolios and to analyze
them from different points of view.

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
%license %{rlibdir}/%{packname}/LICENSE_AMPL
%license %{rlibdir}/%{packname}/LICENSE_DONLP2
%license %{rlibdir}/%{packname}/LICENSE_GLPK
%license %{rlibdir}/%{packname}/LICENSE_QUADPROG
%license %{rlibdir}/%{packname}/LICENSE_SOCP
%license %{rlibdir}/%{packname}/LICENSE_SOLNP
%doc %{rlibdir}/%{packname}/obsolete
%doc %{rlibdir}/%{packname}/ReferenceCard.txt
%{rlibdir}/%{packname}/INDEX
