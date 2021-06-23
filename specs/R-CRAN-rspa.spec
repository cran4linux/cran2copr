%global __brp_check_rpaths %{nil}
%global packname  rspa
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Adapt Numerical Records to Fit (in)Equality Restrictions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-validate 
BuildRequires:    R-CRAN-lintools 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-validate 
Requires:         R-CRAN-lintools 

%description
Minimally adjust the values of numerical records in a data.frame, such
that each record satisfies a predefined set of equality and/or inequality
constraints. The constraints can be defined using the 'validate' package.
The core algorithms have recently been moved to the 'lintools' package,
refer to 'lintools' for a more basic interface and access to a version of
the algorithm that works with sparse matrices.

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
