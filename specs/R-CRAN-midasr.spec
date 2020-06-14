%global packname  midasr
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          2%{?dist}
Summary:          Mixed Data Sampling Regression

License:          GPL-2 | MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-methods 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-quantreg 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-Matrix 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-texreg 
Requires:         R-methods 

%description
Methods and tools for mixed frequency time series data analysis. Allows
estimation, model selection and forecasting for MIDAS regressions.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
