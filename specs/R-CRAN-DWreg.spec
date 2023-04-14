%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  DWreg
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Parametric Regression for Discrete Response

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-DiscreteWeibull 
BuildRequires:    R-CRAN-Ecdat 
BuildRequires:    R-survival 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-DiscreteWeibull 
Requires:         R-CRAN-Ecdat 
Requires:         R-survival 

%description
Regression for a discrete response, where the conditional distribution is
modelled via a discrete Weibull distribution.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
