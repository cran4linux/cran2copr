%global packname  HeterFunctionalData
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Test of No Main and/or Interaction Effects in Functional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Distribution free heteroscedastic tests for functional data. The following
tests are included in this package: test of no main treatment or contrast
effect and no simple treatment effect given in Wang, Higgins, and Blasi
(2010) <doi:10.1016/j.spl.2009.11.016>, no main time effect, and no
interaction effect based on original observations given in Wang and
Akritas (2010a) <doi:10.1080/10485250903171621> and tests based on ranks
given in Wang and Akritas (2010b) <doi:10.1016/j.jmva.2010.03.012>.

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
