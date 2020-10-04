%global packname  pedprobr
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          2%{?dist}%{?buildtag}
Summary:          Probability Computations on Pedigrees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-pedmut 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-pedmut 

%description
An implementation of the Elston-Stewart algorithm for calculating pedigree
likelihoods given genetic marker data (Elston and Stewart (1971)
<doi:10.1159/000152448>). The standard algorithm is extended to allow
inbred founders. Mutation modelling is supported by the 'pedmut' package.
'pedprobr' is part of the ped suite, a collection of packages for pedigree
analysis in R, based on 'pedtools' for handling pedigrees and markers.

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
