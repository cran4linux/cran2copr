%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mMARCH.AC
%global packver   3.2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Processing of Accelerometry Data with 'GGIR' in mMARCH

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-denseFLMM 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-cosinor 
BuildRequires:    R-CRAN-cosinor2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-accelerometry 
BuildRequires:    R-CRAN-ActCR 
BuildRequires:    R-CRAN-ActFrag 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-GGIR 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-denseFLMM 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-cosinor 
Requires:         R-CRAN-cosinor2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-accelerometry 
Requires:         R-CRAN-ActCR 
Requires:         R-CRAN-ActFrag 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-GGIR 

%description
Mobile Motor Activity Research Consortium for Health (mMARCH) is a
collaborative network of studies of clinical and community samples that
employ common clinical, biological, and digital mobile measures across
involved studies. One of the main scientific goals of mMARCH sites is
developing a better understanding of the inter-relationships between
accelerometry-measured physical activity (PA), sleep (SL), and circadian
rhythmicity (CR) and mental and physical health in children, adolescents,
and adults. Currently, there is no consensus on a standard procedure for a
data processing pipeline of raw accelerometry data, and few open-source
tools to facilitate their development. The R package 'GGIR' is the most
prominent open-source software package that offers great functionality and
tremendous user flexibility to process raw accelerometry data. However,
even with 'GGIR', processing done in a harmonized and reproducible fashion
requires a non-trivial amount of expertise combined with a careful
implementation. In addition, novel accelerometry-derived features of
PA/SL/CR capturing multiscale, time-series, functional, distributional and
other complimentary aspects of accelerometry data being constantly
proposed and become available via non-GGIR R implementations.  To address
these issues, mMARCH developed a streamlined harmonized and reproducible
pipeline for loading and cleaning raw accelerometry data, extracting
features available through 'GGIR' as well as through non-GGIR R packages,
implementing several data and feature quality checks, merging all features
of PA/SL/CR together, and performing multiple analyses including Joint
Individual Variation Explained (JIVE), an unsupervised machine learning
dimension reduction technique that identifies latent factors capturing
joint across and individual to each of three domains of PA/SL/CR.  In
detail, the pipeline generates all necessary R/Rmd/shell files for data
processing after running 'GGIR' for accelerometer data. In module 1, all
csv files in the 'GGIR' output directory were read, transformed and then
merged. In module 2, the 'GGIR' output files were checked and summarized
in one excel sheet. In module 3, the merged data was cleaned according to
the number of valid hours on each night and the number of valid days for
each subject. In module 4, the cleaned activity data was imputed by the
average Euclidean norm minus one (ENMO) over all the valid days for each
subject. Finally, a comprehensive report of data processing was created
using Rmarkdown, and the report includes few exploratory plots and
multiple commonly used features extracted from minute level actigraphy
data.  Reference: Guo W, Leroux A, Shou S, Cui L, Kang S, Strippoli MP,
Preisig M, Zipunnikov V, Merikangas K (2022) Processing of accelerometry
data with GGIR in Motor Activity Research Consortium for Health (mMARCH)
Journal for the Measurement of Physical Behaviour, 6(1): 37-44.

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
