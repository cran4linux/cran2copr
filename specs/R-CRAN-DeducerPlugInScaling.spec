%global packname  DeducerPlugInScaling
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Reliability and factor analysis plugin

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Deducer 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-mvnormtest 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-klaR 
Requires:         R-CRAN-Deducer 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-mvnormtest 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-klaR 

%description
A Deducer plug-in for factor analysis, reliability analysis and
discriminant analysis, using psych, GPArotation and mvnormtest packages.

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
