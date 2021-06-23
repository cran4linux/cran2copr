%global __brp_check_rpaths %{nil}
%global packname  easyVerification
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          3%{?dist}%{?buildtag}
Summary:          Ensemble Forecast Verification for Large Data Sets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-SpecsVerification >= 0.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-SpecsVerification >= 0.5
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-pbapply 

%description
Set of tools to simplify application of atomic forecast verification
metrics for (comparative) verification of ensemble forecasts to large data
sets. The forecast metrics are imported from the 'SpecsVerification'
package, and additional forecast metrics are provided with this package.
Alternatively, new user-defined forecast scores can be implemented using
the example scores provided and applied using the functionality of this
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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
