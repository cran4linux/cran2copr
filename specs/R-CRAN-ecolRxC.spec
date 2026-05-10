%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecolRxC
%global packver   0.1.1-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Inference of RxC Tables by Latent Structure Approaches

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 

%description
Estimates RxC (R by C) vote transfer matrices (ecological contingency
tables) from aggregate data building on Thomsen (1987) and Park (2008)
approaches. References: Park, W.-H. (2008). ''Ecological Inference and
Aggregate Analysis of Election''. PhD Dissertation. University of
Michigan.
<https://deepblue.lib.umich.edu/bitstream/handle/2027.42/58525/wpark_1.pdf>
Pavía, J.M. and Thomsen, S.R. (2025) ''ecolRxC: Ecological inference
estimation of RxC tables using latent structure approaches''. Political
Science Research and Methods, 13(4), 943-961. <doi:10.1017/psrm.2024.57>
Thomsen, S.R. (1987, ISBN:87-7335-037-2). ''Danish Elections 1920 79: a
Logit Approach to Ecological Analysis and Inference''. Politica, Aarhus,
Denmark. Acknowledgements: The authors wish to thank Generalitat
Valenciana (Conselleria de Educacion, Cultura y Universidades), grant
CIACIO/2023/031, and Ministerio de Economia e Innovacion, grant
PID2021-128228NB-I00, for supporting this research.

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
