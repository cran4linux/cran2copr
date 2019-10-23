%global packname  drsmooth
%global packver   1.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.0
Release:          1%{?dist}
Summary:          Dose-Response Modeling with Smoothing Splines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-DTK 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-pgirmess 
BuildRequires:    R-stats 
Requires:         R-boot 
Requires:         R-CRAN-car 
Requires:         R-mgcv 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-DTK 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-pgirmess 
Requires:         R-stats 

%description
Provides tools for assessing the shape of a dose-response curve by testing
linearity and non-linearity at user-defined cut-offs. It also provides two
methods of estimating a threshold dose, or the dose at which the
dose-response function transitions to significantly increasing: bi-linear
(based on pkg 'segmented') and smoothed with splines (based on pkg
'mgcv').

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
