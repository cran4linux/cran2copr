%global packname  blockmodeling
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          2%{?dist}
Summary:          Generalized and Classical Blockmodeling of Valued Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-parallel 

%description
This is primarily meant as an implementation of generalized blockmodeling
for valued networks. In addition, measures of similarity or dissimilarity
based on structural equivalence and regular equivalence (REGE algorithms)
can be computed and partitioned matrices can be plotted: Žiberna
(2007)<doi:10.1016/j.socnet.2006.04.002>, Žiberna
(2008)<doi:10.1080/00222500701790207>, Žiberna
(2014)<doi:10.1016/j.socnet.2014.04.002>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
