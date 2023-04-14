%global __brp_check_rpaths %{nil}
%global packname  EMSaov
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}%{?buildtag}
Summary:          The Analysis of Variance with EMS

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-graphics 

%description
Provides the analysis of variance table including the expected mean
squares (EMS) for various types of experimental design. When some
variables are random effects or we use special experimental design such as
nested design, repeated-measures design, or split-plot design, it is not
easy to find the appropriate test, especially denominator for F-statistic
which depends on EMS.

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
