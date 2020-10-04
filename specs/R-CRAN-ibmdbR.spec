%global packname  ibmdbR
%global packver   1.50.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.50.0
Release:          2%{?dist}%{?buildtag}
Summary:          IBM in-Database Analytics for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-MASS 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-RODBC 
Requires:         R-Matrix 
Requires:         R-CRAN-arules 
Requires:         R-MASS 
Requires:         R-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-ggplot2 

%description
Functionality required to efficiently use R with IBM(R) Db2(R) Warehouse
offerings (formerly IBM dashDB(R)) and IBM Db2 for z/OS(R) in conjunction
with IBM Db2 Analytics Accelerator for z/OS. Many basic and complex R
operations are pushed down into the database, which removes the main
memory boundary of R and allows to make full use of parallel processing in
the underlying database.

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
