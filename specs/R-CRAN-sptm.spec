%global packname  sptm
%global packver   2019.11-25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.11.25
Release:          3%{?dist}
Summary:          SemiParametric Transformation Model Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-kyotil 
BuildRequires:    R-methods 
Requires:         R-survival 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-kyotil 
Requires:         R-methods 

%description
Implements semiparametric transformation model two-phase estimation using
calibration weights. The method in Fong and Gilbert (2015) Calibration
weighted estimation of semiparametric transformation models for two-phase
sampling. Statistics in Medicine <DOI:10.1002/sim.6439>.

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
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
