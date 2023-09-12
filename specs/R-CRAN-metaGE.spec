%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaGE
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis for Detecting Genotype x Environment Associations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emdbook 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qqman 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emdbook 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qqman 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-viridis 

%description
Meta-analysis of genome-wide association studies for studying Genotype x
Environment interactions.  The 4 main functions of the package
metaGE.collect(), metaGE.cor(), metaGE.fit() and metaGE.test() correspond
to 4 steps to perform the meta-analysis: Collecting the results of
genome-wide association studies data from different files; Inferring the
inter-environment correlation matrix; Performing global test procedure for
quantitative trait loci detection (using a Fixed or Random effect model);
Performing tests of contrast or meta-regression using an environmental
co-factor. (De Walsche, A., et al. (2023)
<doi:10.1101/2023.03.01.530237>).

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
