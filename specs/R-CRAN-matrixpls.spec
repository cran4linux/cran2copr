%global packname  matrixpls
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          Matrix-Based Partial Least Squares Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-assertive 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-assertive 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-lavaan 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-psych 

%description
Partial Least Squares Path Modeling algorithm and related algorithms. The
algorithm implementations aim for computational efficiency using matrix
algebra and covariance data. The package is designed toward Monte Carlo
simulations and includes functions to perform simple Monte Carlo
simulations.

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
