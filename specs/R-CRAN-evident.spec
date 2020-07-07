%global packname  evident
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Evidence Factors in Observational Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sensitivity2x2xk 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sensitivitymult 
BuildRequires:    R-CRAN-sensitivitymv 
BuildRequires:    R-CRAN-senstrat 
BuildRequires:    R-CRAN-DOS2 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-sensitivity2x2xk 
Requires:         R-graphics 
Requires:         R-CRAN-sensitivitymult 
Requires:         R-CRAN-sensitivitymv 
Requires:         R-CRAN-senstrat 
Requires:         R-CRAN-DOS2 

%description
Contains a collection of examples of evidence factors in observational
studies; e.g., Rosenbaum (2017) <doi:10.1214/17-STS621>.  The examples are
collected to aid readers of a book in preparation, "Replication and
Evidence Factors in Observational Studies".

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
