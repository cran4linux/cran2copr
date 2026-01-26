%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  recluster
%global packver   3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Ordination Methods for the Analysis of Beta-Diversity Indices

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-alphahull 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-alphahull 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vegan 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-plotrix 

%description
The analysis of different aspects of biodiversity requires specific
algorithms. For example, in regionalisation analyses, the high frequency
of ties and zero values in dissimilarity matrices produced by
Beta-diversity turnover produces hierarchical cluster dendrograms whose
topology and bootstrap supports are affected by the order of rows in the
original matrix. Moreover, visualisation of biogeographical
regionalisation can be facilitated by a combination of hierarchical
clustering and multi-dimensional scaling. The recluster package provides
robust techniques to visualise and analyse pattern of biodiversity and to
improve occurrence data for cryptic taxa.

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
