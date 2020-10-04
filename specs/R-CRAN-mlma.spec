%global packname  mlma
%global packver   5.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-lme4 
Requires:         R-splines 
Requires:         R-CRAN-car 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-abind 

%description
Do multilevel mediation analysis with generalized additive multilevel
models. The analysis method is described in Yu and Li (2020),
"Third-Variable Effect Analysis with Multilevel Additive Models",
submitted.

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
