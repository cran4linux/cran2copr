%global packname  CopulaREMADA
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Copula Mixed Models for Multivariate Meta-Analysis of DiagnosticTest Accuracy Studies

License:          GPL (>= 2.10)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-mc2d 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-mc2d 

%description
The bivariate copula mixed model for meta-analysis of diagnostic test
accuracy studies in Nikoloulopoulos (2015) <doi:10.1002/sim.6595>. The
vine copula mixed model for meta-analysis of diagnostic test accuracy
studies accounting for disease prevalence in Nikoloulopoulos (2017)
<doi:10.1177/0962280215596769> and also accounting for non-evaluable
subjects in Nikoloulopoulos (2018) <arXiv:1812.03685>. The hybrid vine
copula mixed model for meta-analysis of diagnostic test accuracy
case-control and cohort studies in Nikoloulopoulos (2018)
<doi:10.1177/0962280216682376>. The D-vine copula mixed model for
meta-analysis and comparison of two diagnostic tests in Nikoloulopoulos
(2018) <doi:10.1177/0962280218796685>. The multinomial quadrivariate
D-vine copula mixed model for meta-analysis of diagnostic tests with
non-evaluable subjects in Nikoloulopoulos (2018) <arXiv:1812.05915>.

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
