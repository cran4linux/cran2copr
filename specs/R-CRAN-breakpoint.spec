%global __brp_check_rpaths %{nil}
%global packname  breakpoint
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          An R Package for Multiple Break-Point Detection via theCross-Entropy Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5
Requires:         R-core >= 2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach >= 1.2.0
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-msm >= 1.0.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
Requires:         R-CRAN-foreach >= 1.2.0
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-msm >= 1.0.1
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-MASS 
Requires:         R-parallel 

%description
Implements the Cross-Entropy (CE) method, which is a model based
stochastic optimization technique to estimate both the number and their
corresponding locations of break-points in continuous and discrete
measurements (Priyadarshana and Sofronov (2015), Priyadarshana and
Sofronov (2012a), Priyadarshana and Sofronov (2012b)).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
