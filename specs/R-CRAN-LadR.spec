%global packname  LadR
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Routines for Fit, Inference and Diagnostics in LAD Models

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-L1pack 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-L1pack 

%description
LAD (Least Absolute Deviations) estimation for linear regression,
confidence intervals, tests of hypotheses, methods for outliers detection,
measures of leverage, methods of diagnostics for LAD regression, special
diagnostics graphs and measures of leverage. The algorithms are based in
Dielman (2005) <doi:10.1080/0094965042000223680>, Elian et al. (2000)
<doi:10.1080/03610920008832518> and Dodge (1997)
<doi:10.1006/jmva.1997.1666>. This package also has two datasets "houses"
and "pollution", respectively, from Narula and Wellington (1977)
<doi:10.2307/1268628> and Santos et al. (2016)
<doi:10.1371/journal.pone.0163225>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
