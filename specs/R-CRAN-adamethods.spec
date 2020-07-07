%global packname  adamethods
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Archetypoid Algorithms and Anomaly Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Anthropometry 
BuildRequires:    R-CRAN-archetypes 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tolerance 
BuildRequires:    R-CRAN-univOutl 
BuildRequires:    R-utils 
Requires:         R-CRAN-Anthropometry 
Requires:         R-CRAN-archetypes 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-nnls 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-tolerance 
Requires:         R-CRAN-univOutl 
Requires:         R-utils 

%description
Collection of several algorithms to obtain archetypoids with small and
large databases and with both classical multivariate data and functional
data (univariate and multivariate). Some of these algorithms also allow to
detect anomalies (outliers).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
