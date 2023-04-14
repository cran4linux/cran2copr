%global __brp_check_rpaths %{nil}
%global packname  CoxR2
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          R-Squared Measure Based on Partial LR Statistic, for the Cox PHRegression Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-stats 
Requires:         R-survival 
Requires:         R-stats 

%description
Calculate the R-squared, aka explained randomness, based on the partial
likelihood ratio statistic under the Cox Proportional Hazard model [J
O'Quigley, R Xu, J Stare (2005) <doi:10.1002/sim.1946>].

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
