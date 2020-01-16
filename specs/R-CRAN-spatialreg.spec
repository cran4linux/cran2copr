%global packname  spatialreg
%global packver   1.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Spatial Regression Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-spData 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-boot 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-gmodels 
Requires:         R-CRAN-spData 
Requires:         R-Matrix 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-boot 
Requires:         R-splines 
Requires:         R-CRAN-LearnBayes 
Requires:         R-nlme 
Requires:         R-CRAN-gmodels 

%description
A collection of all the estimation functions for spatial cross-sectional
models (on lattice/areal data using spatial weights matrices) contained up
to now in 'spdep', 'sphet' and 'spse'. These model fitting functions
include maximum likelihood methods for cross-sectional models proposed by
'Cliff' and 'Ord' (1973, ISBN:0850860369) and (1981, ISBN:0850860814),
fitting methods initially described by 'Ord' (1975)
<doi:10.1080/01621459.1975.10480272>. The models are further described by
'Anselin' (1988) <doi:10.1007/978-94-015-7799-1>. Spatial two stage least
squares and spatial general method of moment models initially proposed by
'Kelejian' and 'Prucha' (1998) <doi:10.1023/A:1007707430416> and (1999)
<doi:10.1111/1468-2354.00027> are provided. Impact methods and MCMC
fitting methods proposed by 'LeSage' and 'Pace' (2009)
<doi:10.1201/9781420064254> are implemented for the family of
cross-sectional spatial regression models. Methods for fitting the log
determinant term in maximum likelihood and MCMC fitting are compared by
'Bivand et al.' (2013) <doi:10.1111/gean.12008>, and model fitting methods
by 'Bivand' and 'Piras' (2015) <doi:10.18637/jss.v063.i18>; both of these
articles include extensive lists of references. 'spatialreg' >= 1.1-*
correspond to 'spdep' >= 1.1-1, in which the model fitting functions are
deprecated and pass through to 'spatialreg', but will mask those in
'spatialreg'. From versions 1.2-*, the functions will be made defunct in
'spdep'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
