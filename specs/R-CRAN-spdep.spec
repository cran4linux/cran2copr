%global packname  spdep
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Spatial Dependence: Weighting Schemes, Statistics and Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-boot >= 1.3.1
BuildRequires:    R-CRAN-sp >= 1.0
BuildRequires:    R-CRAN-spData >= 0.2.6.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-nlme 
Requires:         R-boot >= 1.3.1
Requires:         R-CRAN-sp >= 1.0
Requires:         R-CRAN-spData >= 0.2.6.0
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-deldir 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-LearnBayes 
Requires:         R-MASS 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-gmodels 
Requires:         R-nlme 

%description
A collection of functions to create spatial weights matrix objects from
polygon 'contiguities', from point patterns by distance and tessellations,
for summarizing these objects, and for permitting their use in spatial
data analysis, including regional aggregation by minimum spanning tree; a
collection of tests for spatial 'autocorrelation', including global
'Morans I' and 'Gearys C' proposed by 'Cliff' and 'Ord' (1973, ISBN:
0850860369) and (1981, ISBN: 0850860814), 'Hubert/Mantel' general cross
product statistic, Empirical Bayes estimates and 'Assunção/Reis' (1999)
<doi:10.1002/(SICI)1097-0258(19990830)18:16%3C2147::AID-SIM179%3E3.0.CO;2-I>
Index, 'Getis/Ord' G ('Getis' and 'Ord' 1992)
<doi:10.1111/j.1538-4632.1992.tb00261.x> and multicoloured join count
statistics, 'APLE' ('Li 'et al.' ) <doi:10.1111/j.1538-4632.2007.00708.x>,
local 'Moran's I' ('Anselin' 1995)
<doi:10.1111/j.1538-4632.1995.tb00338.x> and 'Getis/Ord' G ('Ord' and
'Getis' 1995) <doi:10.1111/j.1538-4632.1995.tb00912.x>, 'saddlepoint'
approximations ('Tiefelsdorf' 2002)
<doi:10.1111/j.1538-4632.2002.tb01084.x> and exact tests for global and
local 'Moran's I' ('Bivand et al.' 2009) <doi:10.1016/j.csda.2008.07.021>
and 'LOSH' local indicators of spatial heteroscedasticity ('Ord' and
'Getis') <doi:10.1007/s00168-011-0492-y>. The implementation of most of
the measures is described in 'Bivand' and 'Wong' (2018)
<doi:10.1007/s11749-018-0599-x>. 'spdep' >= 1.1-1 corresponds to
'spatialreg' >= 1.1-1, in which the model fitting functions are deprecated
and pass through to 'spatialreg', but will mask those in 'spatialreg'.
From versions 1.2-1, the functions will be made defunct in 'spdep'. For
now 'spatialreg' only has functions from 'spdep', where they are shown as
deprecated. 'spatialreg' only loads the namespace of 'spdep'; if you
attach 'spdep', the same functions in the other package will be masked.
Some feed through adequately, others do not.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
