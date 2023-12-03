%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  erah
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Spectral Deconvolution, Alignment, and Metabolite Identification in GC/MS-Based Untargeted Metabolomics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-osd 
BuildRequires:    R-CRAN-HiClimR 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
Requires:         R-CRAN-osd 
Requires:         R-CRAN-HiClimR 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-quantreg 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 

%description
Automated compound deconvolution, alignment across samples, and
identification of metabolites by spectral library matching in Gas
Chromatography - Mass spectrometry (GC-MS) untargeted metabolomics.
Outputs a table with compound names, matching scores and the integrated
area of the compound for each sample. Package implementation is described
in Domingo-Almenara et al. (2016) <doi:10.1021/acs.analchem.6b02927>.

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
