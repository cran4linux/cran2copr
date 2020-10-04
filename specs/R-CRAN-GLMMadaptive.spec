%global packname  GLMMadaptive
%global packver   0.7-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          2%{?dist}%{?buildtag}
Summary:          Generalized Linear Mixed Models using Adaptive GaussianQuadrature

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-matrixStats 

%description
Fits generalized linear mixed models for a single grouping factor under
maximum likelihood approximating the integrals over the random effects
with an adaptive Gaussian quadrature rule; Jose C. Pinheiro and Douglas M.
Bates (1995) <doi:10.1080/10618600.1995.10474663>.

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
