%global packname  bmscstan
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multilevel Single Case Models using 'Stan'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-logspline 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-logspline 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-coda 

%description
Analyse single case analyses against a control group. Its purpose is to
provide a flexible, with good power and low first type error approach that
can manage at the same time controls' and patient's data. The use of
Bayesian statistics allows to test both the alternative and null
hypothesis. Scandola, M., & Romano, D. (2020, August 3).
<doi:10.31234/osf.io/sajdq>.

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
