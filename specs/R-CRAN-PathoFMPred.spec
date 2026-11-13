%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PathoFMPred
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tumour Feature Models from Pathology Representations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6.0
Requires:         R-core >= 4.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fastPLS >= 0.4
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fastPLS >= 0.4
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-utils 

%description
Builds and applies portable cancer-specific partial least squares (PLS)
regression and partial least squares with linear discriminant analysis
(PLS-LDA) model collections from pathology foundation-model
representations. Feature and outcome tables are linked by explicit patient
identifiers, repeated slide rows are pooled at patient level, and model
development uses nested cross-validation before final fitting. The source
package contains no fitted foundation-model parameters, embeddings,
patient-level data, or atlas registry. Users may download a separately
licensed, checksum-verified Prov-GigaPath collection after installation,
or load authorized collections from local files. Outputs are research
estimates without external-validation or clinical-use claims. The methods
build on Wold et al. (2001) <doi:10.1016/S0169-7439(01)00155-1> and Barker
and Rayens (2003) <doi:10.1002/cem.785>.

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
