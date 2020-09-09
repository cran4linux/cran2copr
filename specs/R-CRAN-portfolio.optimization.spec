%global packname  portfolio.optimization
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Contemporary Portfolio Optimization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-modopt.matlab 
Requires:         R-CRAN-xts 
Requires:         R-MASS 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-modopt.matlab 

%description
Simplify your portfolio optimization process by applying a contemporary
modeling way to model and solve your portfolio problems. While most
approaches and packages are rather complicated this one tries to simplify
things and is agnostic regarding risk measures as well as optimization
solvers. Some of the methods implemented are described by Konno and
Yamazaki (1991) <doi:10.1287/mnsc.37.5.519>, Rockafellar and Uryasev
(2001) <doi:10.21314/JOR.2000.038> and Markowitz (1952)
<doi:10.1111/j.1540-6261.1952.tb01525.x>.

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
