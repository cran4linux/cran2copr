%global packname  epiphy
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Plant Disease Epidemics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-transport 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-transport 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Rcpp 

%description
A toolbox to make it easy to analyze plant disease epidemics. It provides
a common framework for plant disease intensity data recorded over time
and/or space. Implemented statistical methods are currently mainly focused
on spatial pattern analysis (e.g., aggregation indices, Taylor and binary
power laws, distribution fitting, SADIE and mapcomp methods). See Madden
LV, Hughes G, van den Bosch F (2007, ISBN: 978-089054-354-2) for further
information on these methods. Several data sets that were mainly published
in plant disease epidemiology literature are also included in this
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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
