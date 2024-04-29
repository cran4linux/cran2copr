%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sisti
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Real-Time PCR Data Sets by Sisti et al. (2010)

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tibble 

%description
This data package contains four datasets of quantitative PCR (qPCR)
amplification curves that were used as supplementary data in the research
article by Sisti et al. (2010), <doi:10.1186/1471-2105-11-186>. The
primary dataset comprises a ten-fold dilution series spanning copy numbers
from 3.14 × 10^7 to 3.14 × 10^2, with twelve replicates per concentration.
These samples are based on a pGEM-T Promega plasmid containing a 104 bp
fragment of the mitochondrial gene NADH dehydrogenase 1 (MT-ND1),
amplified using the ND1/ND2 primer pair. The remaining three datasets
contain qPCR results in the presence of specific PCR inhibitors: tannic
acid, immunoglobulin G (IgG), and quercetin, respectively, to assess their
effects on the amplification process. These datasets are useful for
researchers interested in PCR kinetics. The original raw data file is
available as Additional File 1:
<https://static-content.springer.com/esm/art%%3A10.1186%%2F1471-2105-11-186/MediaObjects/12859_2009_3643_MOESM1_ESM.XLS>.

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
