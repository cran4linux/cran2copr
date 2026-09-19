%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biocohort
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cohort Objects for Subjects and Samples in Omics Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-S7 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 

%description
Keeps the subjects, samples, and analysis outputs of a study in one
validated object. It starts from a sample manifest with one row per
sample, which is read, checked, and split into a subject table and a
sample map. Species and assay are plain values in those tables rather than
fixed types, so the same object serves any organism and any omics assay.
From that object the package writes the sample sheet a pipeline expects,
pairs tumor and normal samples on demand, and records where each analysis
writes its output so the files can be loaded back in by subject or by
pair. Manual corrections are kept in an audit trail. Results can also be
translated across genome builds or species, with liftover for coordinates
and ortholog mapping for genes.

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
