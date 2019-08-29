%global packname  gma
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Granger Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-car 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-CRAN-car 

%description
Performs Granger mediation analysis (GMA) for time series. This package
includes a single level GMA model and a two-level GMA model, for time
series with hierarchically nested structure. The single level GMA model
for the time series of a single participant performs the causal mediation
analysis which integrates the structural equation modeling and the Granger
causality frameworks. A vector autoregressive model of order p is employed
to account for the spatiotemporal dependencies in the data. Meanwhile, the
model introduces the unmeasured confounding effect through a nonzero
correlation parameter. Under the two-level model, by leveraging the
variabilities across participants, the parameters are identifiable and
consistently estimated based on a full conditional likelihood or a
two-stage method. See Zhao, Y., & Luo, X. (2017), Granger Mediation
Analysis of Multiple Time Series with an Application to fMRI,
<arXiv:1709.05328> for details.

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
%{rlibdir}/%{packname}/INDEX
