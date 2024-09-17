%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diversityForest
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Innovative Complex Split Procedures in Random Forests Through Candidate Split Sampling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-sgeostat 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-MapGAM 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-sgeostat 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-MapGAM 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-rlang 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-patchwork 

%description
Implementations of three diversity forest (DF) (Hornung, 2022,
<doi:10.1007/s42979-021-00920-1>) variants. The DF algorithm is a
split-finding approach that allows complex split procedures to be realized
in random forest variants. The three DF variants implemented are: 1.
interaction forests (IFs) (Hornung & Boulesteix, 2022,
<doi:10.1016/j.csda.2022.107460>): Model quantitative and qualitative
interaction effects using bivariable splitting. Come with the Effect
Importance Measure (EIM), which can be used to identify variable pairs
that have well-interpretable quantitative and qualitative interaction
effects with high predictive relevance. 2. multi forests (MuFs) (Hornung &
Hapfelmeier, 2024, <doi:10.48550/arXiv.2409.08925>): Model multi-class
outcomes using multi-way and binary splitting. Come with two variable
importance measures (VIMs): The multi-class VIM measures the degree to
which the variables are specifically associated with one or more outcome
classes, and the discriminatory VIM, similar to conventional VIMs,
measures the overall influence strength of the variables. 3. the basic
form of diversity forests that uses conventional univariable, binary
splitting (Hornung, 2022). Except for multi forests, which are tailored
for multi-class outcomes, all included diversity forest variants support
categorical, metric, and survival outcomes. The package also includes
plotting functions that make it possible to learn about the forms of the
effects identified using IFs and MuFs. This is a fork of the R package
'ranger' (main author: Marvin N. Wright), which implements random forests
using an efficient C++ implementation.

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
