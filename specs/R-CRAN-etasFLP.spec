%global packname  etasFLP
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}
Summary:          Mixed FLP and ML Estimation of ETAS Space-Time Point Processesfor Earthquake Description

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-maps 

%description
Estimation of the components of an ETAS (Epidemic Type Aftershock
Sequence) model for earthquake description. Non-parametric background
seismicity can be estimated through FLP (Forward Likelihood Predictive).
New version 2.0.0: covariates have been introduced to explain the effects
of external factors on the induced seismicity; the parametrization has
been changed; Chiodi, Adelfio (2017)<doi:10.18637/jss.v076.i03>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/libs
