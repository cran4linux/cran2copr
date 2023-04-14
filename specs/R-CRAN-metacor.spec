%global __brp_check_rpaths %{nil}
%global packname  metacor
%global packver   1.0-2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Correlation Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmeta 
BuildRequires:    R-CRAN-gsl 
Requires:         R-CRAN-rmeta 
Requires:         R-CRAN-gsl 

%description
Implement the DerSimonian-Laird (DSL) and Olkin-Pratt (OP) meta-analytical
approaches with correlation coefficients as effect sizes.

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
