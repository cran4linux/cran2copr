%global packname  rdpower
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Power Calculations for RD Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rdrobust 
Requires:         R-CRAN-rdrobust 

%description
The regression discontinuity (RD) design is a popular quasi-experimental
design for causal inference and policy evaluation. The 'rdpower' package
provides tools to perform power and sample size calculations in RD
designs: rdpower() calculates the power of an RD design and rdsampsi()
calculates the required sample size to achieve a desired power. See
Cattaneo, Titiunik and Vazquez-Bare (2018)
<https://sites.google.com/site/rdpackages/rdpower/Cattaneo-Titiunik-VazquezBare_2018_Stata.pdf>
for further methodological details.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
