%global packname  boxcoxmix
%global packver   0.28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.28
Release:          1%{?dist}%{?buildtag}
Summary:          Box-Cox-Type Transformations for Linear and Logistic Models with Random Effects

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-statmod >= 1.4.27
BuildRequires:    R-CRAN-qicharts >= 0.5.4
BuildRequires:    R-CRAN-npmlreg >= 0.46.1
Requires:         R-CRAN-statmod >= 1.4.27
Requires:         R-CRAN-qicharts >= 0.5.4
Requires:         R-CRAN-npmlreg >= 0.46.1

%description
Box-Cox-type transformations for linear and logistic models with random
effects using non-parametric profile maximum likelihood estimation. The
main functions are optim.boxcox() for linear models with random effects
and boxcoxtype() for logistic models with random effects.

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
