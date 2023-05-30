%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlpsem
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Nonlinear Longitudinal Process in Structural Equation Modeling Framework

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-OpenMx 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-readr 

%description
Provides computational resources for nonlinear longitudinal models,
specifically those that are intrinsically nonlinear, in four distinct
contexts: (1) univariate longitudinal processes represented by latent
variables, with an option of incorporating covariates such as
time-invariant covariates (TICs) and time-varying covariates (TVCs); (2)
multivariate longitudinal sequences that facilitate the assessment of
correlations or causative relationships between longitudinal variables;
(3) multiple-group structures for models found in scenarios (1) and (2),
allowing for the exploration of disparities among manifested classes; and
(4) mixture models for scenarios (1) and (2), premised on the assumption
that trajectories are from multiple latent classes. The methods
implemented are based on Peugh & Fan (2015)
<doi:10.1080/10705511.2014.919823>, Lubke & Muthén (2007)
<doi:10.1080/10705510709336735>, Casella & Berger (2002, ISBN:
9780534243128), Madansky (1965) <https://www.jstor.org/stable/1266390>,
Matthews (1988) <https://www.jstor.org/stable/2336444>, Efron & Tibshirani
(1994, ISBN: 9780412042317>, Estabrook & Neale (2013)
<doi:10.1080/00273171.2012.730072>, Priestley & Subba Rao (1975)
<doi:10.1080/00207177508922050>, Dumenci (2011)
<doi:10.1177/1094428110374649>, Landis & Koch (1977)
<doi:10.2307/2529310>, Agresti (2012, ISBN: 9780470463635), Liu & Perera
(2023) <arXiv:2201.00470v6>, Liu (2022) <arXiv:2210.16916>, Grimm, Zhang,
Hamagami & Mazzocco (2013) <doi:10.1080/00273171.2012.755111>, Liu,
Perera, Kang, Sabo, and Kirkpatrick (2021)
<doi:10.3102/10769986211052009>, Sterba (2014)
<doi:10.1080/10705511.2014.919828>, Liu & Perera (2021)
<doi:10.1037/met0000309>, Blozis (2004) <doi:10.1037/1082-989X.9.3.334>,
Liu & Perera (2022) <doi:10.3758/s13428-022-01940-2>, MacKinnon (2008,
ISBN: 9780805864298), Cheong, MacKinnon & Khoo (2003)
<doi:10.1207/S15328007SEM1002_5>, Soest & Hagtvet (2011)
<doi:10.1080/10705511.2011.557344>, Liu & Perera (2022)
<doi:10.1037/met0000436>, Liu & Perera (2022) <doi:10.1037/met0000500>,
and Liu (2023) <arXiv:2301.06014>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
