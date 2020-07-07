%global packname  YPInterimTesting
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Interim Monitoring Using Adaptively Weighted Log-Rank Test inClinical Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 

%description
For any spending function specified by the user, this package provides
corresponding boundaries for interim testing using the adaptively weighted
log-rank test developed by Yang and Prentice (2010
<doi:10.1111/j.1541-0420.2009.01243.x>). The package uses a re-sampling
method to obtain stopping boundaries at the interim looks.The output
consists of stopping boundaries and observed values of the test statistics
at the interim looks, along with nominal p-values defined as the
probability of the test exceeding the specific observed test statistic
value or critical value, regardless of the test behavior at other looks.
The asymptotic validity of the stopping boundaries is established in Yang
(2018 <doi:10.1002/sim.7958>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
