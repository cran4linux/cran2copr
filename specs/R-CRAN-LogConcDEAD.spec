%global packname  LogConcDEAD
%global packver   1.6-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          3%{?dist}
Summary:          Log-Concave Density Estimation in Arbitrary Dimensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tkrplot 
Requires:         R-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tkrplot 

%description
Software for computing a log-concave (maximum likelihood) estimator for
i.i.d. data in any number of dimensions. For a detailed description of the
method see Cule, Samworth and Stewart (2010, Journal of Royal Statistical
Society Series B, <doi:10.1111/j.1467-9868.2010.00753.x>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
