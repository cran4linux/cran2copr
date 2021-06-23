%global __brp_check_rpaths %{nil}
%global packname  archetypes
%global packver   2.2-0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Archetypal Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nnls >= 1.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-modeltools 
Requires:         R-CRAN-nnls >= 1.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-modeltools 

%description
The main function archetypes implements a framework for archetypal
analysis supporting arbitrary problem solving mechanisms for the different
conceptual parts of the algorithm.

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
