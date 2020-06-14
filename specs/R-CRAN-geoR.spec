%global packname  geoR
%global packver   1.8-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.1
Release:          2%{?dist}
Summary:          Analysis of Geostatistical Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-RandomFields 
Requires:         R-graphics 

%description
Geostatistical analysis including variogram-based, likelihood-based and
Bayesian methods. Software companion for Diggle and Ribeiro (2007)
<doi:10.1007/978-0-387-48536-2>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
