%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Capsule
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Reproducibility Framework for R and Bioinformatics Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-utils 

%description
A comprehensive reproducibility framework designed for R and
bioinformatics workflows. Automatically captures the entire analysis
environment including R session info, package versions, external tool
versions ('Samtools', 'STAR', 'BWA', etc.), 'conda' environments,
reference genomes, data provenance with smart checksumming for large
files, parameter choices, random seeds, and hardware specifications.
Generates executable scripts with 'Docker', 'Singularity', and 'renv'
configurations. Integrates with workflow managers ('Nextflow',
'Snakemake', 'WDL', 'CWL') to ensure complete reproducibility of
computational research workflows.

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
