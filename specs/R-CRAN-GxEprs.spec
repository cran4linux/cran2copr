%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GxEprs
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genotype-by-Environment Interaction in Polygenic Score Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
A novel PRS model is introduced to enhance the prediction accuracy by
utilising GxE effects. This package performs Genome Wide Association
Studies (GWAS) and Genome Wide Environment Interaction Studies (GWEIS)
using a discovery dataset. The package has the ability to obtain polygenic
risk scores (PRSs) for a target sample. Finally it predicts the risk
values of each individual in the target sample. Users have the choice of
using existing models (Li et al., 2015) <doi:10.1093/annonc/mdu565>,
(Pandis et al., 2013) <doi:10.1093/ejo/cjt054>, (Peyrot et al., 2018)
<doi:10.1016/j.biopsych.2017.09.009> and (Song et al., 2022)
<doi:10.1038/s41467-022-32407-9>, as well as newly proposed models for
genomic risk prediction (refer to the URL for more details).

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
