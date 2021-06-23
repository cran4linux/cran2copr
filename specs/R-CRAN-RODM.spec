%global __brp_check_rpaths %{nil}
%global packname  RODM
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}%{?buildtag}
Summary:          R interface to Oracle Data Mining

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.1
Requires:         R-core >= 2.10.1
BuildArch:        noarch
BuildRequires:    R-CRAN-RODBC 
Requires:         R-CRAN-RODBC 

%description
This package implements an interface to Oracle Data Mining (ODM). It
provides an ideal environment for rapid development of demos and proof of
concept data mining studies. It facilitates the prototyping of vertical
applications and makes ODM and the RDBMS environment easily accessible to
statisticians and data analysts familiar with R but not fluent in SQL or
familiar with the database environment. It also facilitates the
benchmarking and testing of ODM functionality including the production of
summary statistics, performance metrics and graphics. It enables the
scripting and control of production data mining methodologies from a
high-level environment. Oracle Data Mining (ODM) is an option of Oracle
Relational Database Management System (RDBMS) Enterprise Edition (EE). It
contains several data mining and data analysis algorithms for
classification, prediction, regression, clustering, associations, feature
selection, anomaly detection, feature extraction, and specialized
analytics. It provides means for the creation, management and operational
deployment of data mining models inside the database environment. For more
information consult the entry for "Oracle Data Mining" in Wikipedia
(en.wikipedia.org).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
