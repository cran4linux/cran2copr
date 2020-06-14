%global packname  DTWBI
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Imputation of Time Series Based on Dynamic Time Warping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-lsa 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-rlist 
Requires:         R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-lsa 

%description
Functions to impute large gaps within time series based on Dynamic Time
Warping methods. It contains all required functions to create large
missing consecutive values within time series and to fill them, according
to the paper Phan et al. (2017), <DOI:10.1016/j.patrec.2017.08.019>.
Performance criteria are added to compare similarity between two signals
(query and reference).

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
