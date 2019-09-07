%global packname  SimMultiCorrData
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Simulation of Correlated Data with Multiple Variable Types

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-GenOrd 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-GenOrd 
Requires:         R-CRAN-psych 
Requires:         R-Matrix 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Generate continuous (normal or non-normal), binary, ordinal, and count
(Poisson or Negative Binomial) variables with a specified correlation
matrix.  It can also produce a single continuous variable.  This package
can be used to simulate data sets that mimic real-world situations (i.e.
clinical or genetic data sets, plasmodes).  All variables are generated
from standard normal variables with an imposed intermediate correlation
matrix.  Continuous variables are simulated by specifying mean, variance,
skewness, standardized kurtosis, and fifth and sixth standardized
cumulants using either Fleishman's third-order (<DOI:10.1007/BF02293811>)
or Headrick's fifth-order (<DOI:10.1016/S0167-9473(02)00072-5>) polynomial
transformation.  Binary and ordinal variables are simulated using a
modification of the ordsample() function from 'GenOrd'. Count variables
are simulated using the inverse cdf method.  There are two simulation
pathways which differ primarily according to the calculation of the
intermediate correlation matrix.  In Correlation Method 1, the
intercorrelations involving count variables are determined using a
simulation based, logarithmic correlation correction (adapting Yahav and
Shmueli's 2012 method, <DOI:10.1002/asmb.901>).  In Correlation Method 2,
the count variables are treated as ordinal (adapting Barbiero and
Ferrari's 2015 modification of GenOrd, <DOI:10.1002/asmb.2072>). There is
an optional error loop that corrects the final correlation matrix to be
within a user-specified precision value of the target matrix.  The package
also includes functions to calculate standardized cumulants for
theoretical distributions or from real data sets, check if a target
correlation matrix is within the possible correlation bounds (given the
distributions of the simulated variables), summarize results (numerically
or graphically), to verify valid power method pdfs, and to calculate lower
standardized kurtosis bounds.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
