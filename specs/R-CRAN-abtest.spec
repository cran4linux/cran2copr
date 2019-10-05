%global packname  abtest
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Bayesian A/B Testing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-plotrix 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-Matrix 
Requires:         R-parallel 

%description
Provides functions for Bayesian A/B testing including prior elicitation
options based on Kass and Vaidyanathan (1992)
<doi:10.1111/j.2517-6161.1992.tb01868.x>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
