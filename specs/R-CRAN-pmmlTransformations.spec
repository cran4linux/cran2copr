%global packname  pmmlTransformations
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Transforms Input Data from a PMML Perspective

License:          GPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Allows for data to be transformed before using it to construct models.
Builds structures to allow functions in the PMML package to output
transformation details in addition to the model in the resulting PMML
file. The Predictive Model Markup Language (PMML) is an XML-based language
which provides a way for applications to define machine learning,
statistical and data mining models and to share models between PMML
compliant applications. More information about the PMML industry standard
and the Data Mining Group can be found at <http://www.dmg.org>. The
generated PMML can be imported into any PMML consuming application, such
as Zementis Predictive Analytics products, which integrate with web
services, relational database systems and deploy natively on Hadoop in
conjunction with Hive, Spark or Storm, as well as allow predictive
analytics to be executed for IBM z Systems mainframe applications and
real-time, streaming analytics platforms.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
