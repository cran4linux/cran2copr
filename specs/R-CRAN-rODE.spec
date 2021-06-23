%global __brp_check_rpaths %{nil}
%global packname  rODE
%global packver   0.99.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.6
Release:          1%{?dist}%{?buildtag}
Summary:          Ordinary Differential Equation (ODE) Solvers Written in R Using S4 Classes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-data.table 

%description
Show physics, math and engineering students how an ODE solver is made and
how effective R classes can be for the construction of the equations that
describe natural phenomena. Inspiration for this work comes from the book
on "Computer Simulations in Physics" by Harvey Gould, Jan Tobochnik, and
Wolfgang Christian. Book link:
<http://www.compadre.org/osp/items/detail.cfm?ID=7375>.

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
