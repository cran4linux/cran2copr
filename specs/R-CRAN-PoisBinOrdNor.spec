%global packname  PoisBinOrdNor
%global packver   1.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          1%{?dist}
Summary:          Data Generation with Poisson, Binary, Ordinal and NormalComponents

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-GenOrd 
Requires:         R-Matrix 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-GenOrd 

%description
Generation of multiple count, binary, ordinal and normal variables
simultaneously given the marginal characteristics and association
structure. The details of the method are explained in Demirtas et al.
(2012) <DOI:10.1002/sim.5362>.

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
