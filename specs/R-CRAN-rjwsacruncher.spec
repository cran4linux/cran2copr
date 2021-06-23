%global __brp_check_rpaths %{nil}
%global packname  rjwsacruncher
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'JWSACruncher' of 'JDemetra+'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-XML 

%description
'JDemetra+' (<https://github.com/jdemetra/jdemetra-app>) is the seasonal
adjustment software officially recommended to the members of the European
Statistical System and the European System of Central Banks. Seasonal
adjustment models performed with 'JDemetra+' can be stored into
workspaces. 'JWSACruncher'
(<https://github.com/jdemetra/jwsacruncher/releases>) is a console tool
that re-estimates all the multi-processing defined in a workspace and to
export the result. 'rjwsacruncher' allows to launch easily the
'JWSACruncher'.

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
