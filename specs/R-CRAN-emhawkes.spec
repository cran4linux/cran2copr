%global packname  emhawkes
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          2%{?dist}
Summary:          Exponential Multivariate Hawkes Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-methods 
Requires:         R-CRAN-maxLik 
Requires:         R-methods 

%description
Simulate and fitting exponential multivariate Hawkes model. This package
simulates a multivariate Hawkes model, introduced by Hawkes (1971)
<doi:10.1093/biomet/58.1.83>, with an exponential kernel and fits the
parameters from the data. Models with the constant parameters, as well as
complex dependent structures, can also be simulated and estimated. The
estimation is based on the maximum likelihood method, introduced by
introduced by Ozaki (1979) <doi:10.1007/BF02480272>, with 'maxLik'
package.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
