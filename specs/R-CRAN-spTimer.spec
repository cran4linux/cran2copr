%global packname  spTimer
%global packver   3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Bayesian Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-extraDistr 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits, spatially predicts and temporally forecasts large amounts of
space-time data using [1] Bayesian Gaussian Process (GP) Models, [2]
Bayesian Auto-Regressive (AR) Models, and [3] Bayesian Gaussian Predictive
Processes (GPP) based AR Models for spatio-temporal big-n problems. Bakar
and Sahu (2015) <doi:10.18637/jss.v063.i15>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
