%global __brp_check_rpaths %{nil}
%global packname  REQS
%global packver   0.8-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.12
Release:          1%{?dist}%{?buildtag}
Summary:          R/EQS Interface

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-gtools 

%description
This package contains the function run.eqs() which calls an EQS script
file, executes the EQS estimation, and, finally, imports the results as R
objects. These two steps can be performed separately: call.eqs() calls and
executes EQS, whereas read.eqs() imports existing EQS outputs as objects
into R. It requires EQS 6.2 (build 98 or higher).

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
