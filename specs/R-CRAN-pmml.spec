%global packname  pmml
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          3%{?dist}
Summary:          Generate PMML for Various Models

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-XML 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 

%description
The Predictive Model Markup Language (PMML) is an XML-based language which
provides a way for applications to define machine learning, statistical
and data mining models and to share models between PMML compliant
applications. More information about the PMML industry standard and the
Data Mining Group can be found at <http://www.dmg.org>. The generated PMML
can be imported into any PMML consuming application, such as Zementis
Predictive Analytics products, which integrate with web services,
relational database systems and deploy natively on Hadoop in conjunction
with Hive, Spark or Storm, as well as allow predictive analytics to be
executed for IBM z Systems mainframe applications and real-time, streaming
analytics platforms. The package isofor (used for anomaly detection) can
be installed with devtools::install_github("Zelazny7/isofor").

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
