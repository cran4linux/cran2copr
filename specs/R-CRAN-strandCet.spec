%global packname  strandCet
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Estimation of Biological Parameters from Stranded Cetaceans

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-corpcor 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-boot 
Requires:         R-CRAN-minpack.lm 
Requires:         R-stats 

%description
Analysis of biological data from stranded marine mammals: mortality-at-age
(Heligman, L. and Pollard, J.H. 1980 <doi:10.1017/S0020268100040257>),
life tables, Leslie matrices, etc.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
