%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ibmdbR
%global packver   1.51.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.51.0
Release:          1%{?dist}%{?buildtag}
Summary:          IBM in-Database Analytics for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-methods 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rpart.plot 

%description
Functionality required to efficiently use R with IBM(R) Db2(R) Warehouse
offerings (formerly IBM dashDB(R)) and IBM Db2 for z/OS(R) in conjunction
with IBM Db2 Analytics Accelerator for z/OS. Many basic and complex R
operations are pushed down into the database, which removes the main
memory boundary of R and allows to make full use of parallel processing in
the underlying database. For executing R-functions in a multi-node
environment in parallel the idaTApply() function requires the 'SparkR'
package (<https://spark.apache.org/docs/latest/sparkr.html>). The optional
'ggplot2' package is needed for the plot.idaLm() function only.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
