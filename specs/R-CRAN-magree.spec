%global __brp_check_rpaths %{nil}
%global packname  magree
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Implements the O'Connell-Dobson-Schouten Estimators of Agreement for Multiple Observers

License:          GPL-3 | GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
Requires:         R-graphics 

%description
Implements an interface to the legacy Fortran code from O'Connell and
Dobson (1984) <DOI:10.2307/2531148>. Implements Fortran 77 code for the
methods developed by Schouten (1982)
<DOI:10.1111/j.1467-9574.1982.tb00774.x>. Includes estimates of average
agreement for each observer and average agreement for each subject.

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
