%global packname  mgm
%global packver   1.2-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.10
Release:          2%{?dist}%{?buildtag}
Summary:          Estimating Time-Varying k-Order Mixed Graphical Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-gtools 

%description
Estimation of k-Order time-varying Mixed Graphical Models and mixed VAR(p)
models via elastic-net regularized neighborhood regression. For details
see Haslbeck & Waldorp (2020) <doi:10.18637/jss.v093.i08>.

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
