%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pooledpeaks
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Genetic Analysis of Pooled Samples

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Fragman 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Fragman 
Requires:         R-graphics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Analyzing genetic data obtained from pooled samples. This package can read
in Fragment Analysis output files, process the data, and score peaks, as
well as facilitate various analyses, including cluster analysis,
calculation of genetic distances and diversity indices, as well as
bootstrap resampling for statistical inference. Specifically tailored to
handle genetic data efficiently, researchers can explore population
structure, genetic differentiation, and genetic relatedness among samples.
We updated some functions from Covarrubias-Pazaran et al. (2016)
<doi:10.1186/s12863-016-0365-6> to allow for the use of new file formats
and referenced the following to write our genetic analysis functions: Long
et al. (2022) <doi:10.1038/s41598-022-04776-0>, Jost (2008)
<doi:10.1111/j.1365-294x.2008.03887.x>, Nei (1973)
<doi:10.1073/pnas.70.12.3321>, Foulley et al. (2006)
<doi:10.1016/j.livprodsci.2005.10.021>, Chao et al. (2008)
<doi:10.1111/j.1541-0420.2008.01010.x>.

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
