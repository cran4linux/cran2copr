%global packname  FSMUMI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Imputation of Time Series Based on Fuzzy Logic

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FuzzyR 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lsa 
Requires:         R-CRAN-FuzzyR 
Requires:         R-stats 
Requires:         R-CRAN-lsa 

%description
Filling large gaps in low or uncorrelated multivariate time series uses a
new fuzzy weighted similarity measure. It contains all required functions
to create large missing consecutive values within time series and then
fill these gaps, according to the paper Phan et al. (2018),
<DOI:10.1155/2018/9095683>. Performance indicators are also provided to
compare similarity between two univariate signals (incomplete signal and
imputed signal).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
