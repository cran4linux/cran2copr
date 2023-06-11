%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  itsdm
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Isolation Forest-Based Presence-Only Species Distribution Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stars >= 0.6.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastshap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-isotree 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-outliertree 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROCit 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-stars >= 0.6.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastshap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-isotree 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-outliertree 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROCit 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Collection of R functions to do purely presence-only species distribution
modeling with isolation forest (iForest) and its variations such as
Extended isolation forest and SCiForest. See the details of these methods
in references: Liu, F.T., Ting, K.M. and Zhou, Z.H. (2008)
<doi:10.1109/ICDM.2008.17>, Hariri, S., Kind, M.C. and Brunner, R.J.
(2019) <doi:10.1109/TKDE.2019.2947676>, Liu, F.T., Ting, K.M. and Zhou,
Z.H. (2010) <doi:10.1007/978-3-642-15883-4_18>, Guha, S., Mishra, N., Roy,
G. and Schrijvers, O. (2016)
<https://proceedings.mlr.press/v48/guha16.html>, Cortes, D. (2021)
<arXiv:2110.13402>. Additionally, Shapley values are used to explain model
inputs and outputs. See details in references: Shapley, L.S. (1953)
<doi:10.1515/9781400881970-018>, Lundberg, S.M. and Lee, S.I. (2017)
<https://dl.acm.org/doi/abs/10.5555/3295222.3295230>, Molnar, C.  (2020)
<ISBN:978-0-244-76852-2>, Štrumbelj, E. and Kononenko, I. (2014)
<doi:10.1007/s10115-013-0679-x>. itsdm also provides functions to diagnose
variable response, analyze variable importance, draw spatial dependence of
variables and examine variable contribution. As utilities, the package
includes a few functions to download bioclimatic variables including
'WorldClim' version 2.0 (see Fick, S.E. and Hijmans, R.J. (2017)
<doi:10.1002/joc.5086>) and 'CMCC-BioClimInd' (see Noce, S., Caporaso, L.
and Santini, M. (2020) <doi:10.1038/s41597-020-00726-5>.

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
