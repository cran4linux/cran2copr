%global packname  faoutlier
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Influential Case Detection Methods for Factor Analysis andStructural Equation Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply >= 1.3.0
BuildRequires:    R-CRAN-mirt >= 1.24
BuildRequires:    R-CRAN-sem 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-MASS 
Requires:         R-CRAN-pbapply >= 1.3.0
Requires:         R-CRAN-mirt >= 1.24
Requires:         R-CRAN-sem 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-CRAN-lavaan 
Requires:         R-MASS 

%description
Tools for detecting and summarize influential cases that can affect
exploratory and confirmatory factor analysis models as well as structural
equation models more generally.

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
