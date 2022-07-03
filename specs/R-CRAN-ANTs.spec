%global __brp_check_rpaths %{nil}
%global packname  ANTs
%global packver   0.0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.16
Release:          1%{?dist}%{?buildtag}
Summary:          Animal Network Toolkit Software

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-rstudioapi 

%description
How animals interact and develop social relationships in face of
sociodemographic and ecological pressures is of great interest. New
methodologies, in particular Social Network Analysis (SNA), allow us to
elucidate these types of questions. However, the different methodologies
developed to that end and the speed at which they emerge make their use
difficult. Moreover, the lack of communication between the different
software developed to provide an answer to the same/different research
questions is a source of confusion. The R package Animal Network Toolkit
'ANTs' was developed with the aim of implementing in one package the
different social network analysis techniques currently used in the study
of animal social networks. Hence, ANT is a toolkit for animal research
allowing among other things to: 1) measure global, dyadic and nodal
networks metrics; 2) perform data randomization: pre- and post-network
(node and link permutations); 3) perform statistical permutation tests as
correlation test (<doi:10.2307/2332226>), t-test (<doi:10.1037/h0041412>),
General Linear Model (<doi:10.2307/2346786>), General Linear Mixed Model
(<doi:10.2307/2346786>), deletion simulation
(<doi:10.1098/rsbl.2003.0057>), 'Matrix TauKr correlations'
(<doi:10.1016/S0022-5193(05)80036-0>). The package is partially coded in
C++ using the R package 'Rcpp' for an optimal coding speed. The package
gives researchers a workflow from the raw data to the achievement of
statistical analyses, allowing for a multilevel approach
(<doi:10.1007/978-3-319-47829-6_1882-1>): from the individual's position
and role within the network, to the identification of interaction
patterns, and the study of the overall network properties. Furthermore,
ANT also provides a guideline on the SNA techniques used: 1) from the
appropriate randomization technique according to the data collected; 2) to
the choice, the meaning, the limitations and advantages of the network
metrics to apply, 3) and the type of statistical tests to run. The ANT
project is multi-collaborative, aiming to provide access to advanced
social network analysis techniques and to create new ones that meet
researchers' needs in future versions.  The ANT project is
multi-collaborative, aiming to provide access to advanced social network
analysis techniques and to create new ones that meet researchers' needs in
future versions.

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
