%global packname  Myrrix
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Interface to Myrrix. Myrrix is a Complete, Real-Time, ScalableClustering and Recommender System, Evolved from Apache Mahout

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.6.3
BuildRequires:    R-CRAN-Myrrixjars 
BuildRequires:    R-methods 
Requires:         R-CRAN-rJava >= 0.6.3
Requires:         R-CRAN-Myrrixjars 
Requires:         R-methods 

%description
Recommendation engine based on 'Myrrix'. 'Myrrix' is a complete,
real-time, scalable clustering and recommender system, evolved from
'Apache Mahout'. It uses Alternating Least Squares to build a
recommendation engine.

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
%doc %{rlibdir}/%{packname}/dev
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
