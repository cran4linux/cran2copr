%global packname  multilevelTools
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Multilevel and Mixed Effects Model Diagnostics and Effect Sizes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-JWileymisc >= 1.1.0
BuildRequires:    R-CRAN-extraoperators >= 0.1.1
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-JWileymisc >= 1.1.0
Requires:         R-CRAN-extraoperators >= 0.1.1
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-nlme 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-zoo 

%description
Effect sizes, diagnostics and performance metrics for multilevel and mixed
effects models. Includes marginal and conditional 'R2' estimates for
linear mixed effects models based on Johnson (2014)
<doi:10.1111/2041-210X.12225>.

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

%files
%{rlibdir}/%{packname}
