%global __brp_check_rpaths %{nil}
%global packname  CIAAWconsensus
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Isotope Ratio Meta-Analysis

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-Matrix 

%description
Calculation of consensus values for atomic weights, isotope amount ratios,
and isotopic abundances with the associated uncertainties using
multivariate meta-regression approach for consensus building.

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
