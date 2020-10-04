%global packname  valorate
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Velocity and Accuracy of the LOg-RAnk TEst

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-survival 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-survival 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 

%description
The algorithm implemented in this package was designed to quickly
estimates the distribution of the log-rank especially for heavy unbalanced
groups. VALORATE estimates the null distribution and the p-value of the
log-rank test based on a recent formulation. For a given number of
alterations that define the size of survival groups, the estimation
involves a weighted sum of distributions that are conditional on a
co-occurrence term where mutations and events are both present. The
estimation of conditional distributions is quite fast allowing the
analysis of large datasets in few minutes
<http://bioinformatica.mty.itesm.mx/valorate>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
